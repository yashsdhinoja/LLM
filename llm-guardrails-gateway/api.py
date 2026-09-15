from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from gateway import GuardrailsGateway

# 1. Initialize the web application and our security gateway
app = FastAPI(title="LLM Guardrails Gateway")
gateway = GuardrailsGateway()

# 2. Define what the incoming request from a frontend should look like
class UserRequest(BaseModel):
    prompt: str

# 3. Create the API Endpoint
# When a frontend sends a POST request to "http://localhost:8000/api/chat", this runs.
@app.post("/api/chat")
async def chat_endpoint(request: UserRequest):
    print(f"\n[API] Received prompt: {request.prompt}")
    
    # Pass the frontend's text directly into the engine we built!
    response = gateway.process_request(request.prompt)
    
    # If our gateway blocked it, return an HTTP error code (400 Bad Request)
    if response["status"] == "blocked":
        raise HTTPException(status_code=400, detail=response["message"])
        
    # If the gateway's AI failed all 3 retries, return a 500 Internal Server Error
    if response["status"] == "error":
        raise HTTPException(status_code=500, detail=response["message"])
        
    # If successful, return the perfectly validated JSON back to the frontend!
    return {"success": True, "ai_response": response["data"]}