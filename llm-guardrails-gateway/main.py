from gateway import GuardrailsGateway

# Initialize our updated gateway
gateway = GuardrailsGateway()

#let's ask a completely safe question
safe_prompt = "what is the capital of france ?"

print("=== STARTING GATEWAY PROCESS ===")
final_result = gateway.process_request(safe_prompt)

print("\n === FINAL DELIVERED RESULT ===")
print(final_result)