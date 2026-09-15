import yaml
import re
import json
from pydantic import BaseModel, ValidationError

# ==========================================
# 1. DEFINE OUR OUTPUT SCHEMA (PYDANTIC)
# ==========================================
# This tells our system: "The AI MUST return these exact fields, with these exact data types."
class ExpectedAIResponse(BaseModel):
    summary: str
    confidence_score: float

# ==========================================
# 2. THE MAIN GATEWAY CLASS
# ==========================================
class GuardrailsGateway:
    def __init__(self, policy_file_path="policies.yaml"):
        self.policy_file_path = policy_file_path
        self.rules = self.load_policies()

    def load_policies(self):
        try:
            with open(self.policy_file_path, "r") as file:
                return yaml.safe_load(file)
        except Exception as e:
            return {"banned_topics": [], "system_requirements": {}}

    def check_input_guardrails(self, user_prompt):
        """Phase 1: Protect the AI from the user."""
        credit_card_pattern = r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b'
        if re.search(credit_card_pattern, user_prompt):
            return False, "Request blocked. Potential PII leak detected."

        banned_list = self.rules.get("banned_topics", [])
        clean_prompt = user_prompt.lower()
        for topic in banned_list:
            if topic.lower() in clean_prompt:
                return False, f"Request blocked. The topic '{topic}' is not allowed."
                
        return True, "Passed input guardrails."

    def validate_output_guardrails(self, llm_response_text):
        """Phase 2: Protect the User from the AI."""
        try:
            # Step 1: Did the AI actually return JSON, or did it return plain text?
            data = json.loads(llm_response_text)
            
            # Step 2: Does the JSON match our exact Pydantic format?
            validated_data = ExpectedAIResponse(**data)
            
            # If we get here, it passed! Return the clean data.
            return True, validated_data.model_dump()
            
        except json.JSONDecodeError:
            return False, "AI Error: Output was not valid JSON."
        except ValidationError as e:
            return False, f"AI Error: Missing required fields.\nDetails: {e}"

    # ==========================================
    # 3. THE AUTO-RETRY ENGINE
    # ==========================================
    def process_request(self, user_prompt):
        """This runs the entire lifecycle of the request."""
        
        # 1. Run Input Guardrails
        passed_input, msg = self.check_input_guardrails(user_prompt)
        if not passed_input:
            return {"status": "blocked", "message": msg}

        # 2. Set up our Auto-Retry parameters
        max_retries = 3
        current_prompt = user_prompt

        print("\n[Gateway] Sending to LLM...")

        for attempt in range(1, max_retries + 1):
            print(f"  -> Attempt {attempt}/{max_retries}")
            
            # 3. Call the AI (Using our fake mock AI for testing)
            ai_response = self._mock_call_llm(current_prompt, attempt)
            print(f"  <- AI Said: {ai_response}")
            
            # 4. Check the Output Guardrails
            is_valid, result = self.validate_output_guardrails(ai_response)

            if is_valid:
                print("  [Gateway] Output is Safe and Valid!")
                return {"status": "success", "data": result}
            else:
                print(f"  [Gateway] Output Failed Validation: {result}")
                # 5. THE FIX: Auto-append instructions to the prompt so the AI corrects itself!
                current_prompt += f"\n\nSYSTEM ERROR: Your previous response failed: {result}. Please output ONLY valid JSON matching the schema."

        # 6. Safe Fallback if it fails 3 times
        return {"status": "error", "message": "Safe Fallback: AI failed to generate valid output."}

    def _mock_call_llm(self, prompt, attempt):
        """A fake AI to simulate making mistakes and correcting them."""
        # On attempt 1, the AI forgets the confidence score (Invalid Schema)
        if attempt == 1:
            return '{"summary": "The user is asking a safe question."}'
        # On attempt 2, the AI reads our automated correction and fixes it!
        else:
            return '{"summary": "The user is asking a safe question.", "confidence_score": 0.99}'