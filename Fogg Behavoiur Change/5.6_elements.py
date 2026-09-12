
def evaluate_ability_chain(user, task):
    
    print(f"\nEvaluating if {user['name']} can do: '{task['name']}'")
    
    
    if task['time_required_mins'] > user['time_available_mins']:
        return {"can_do": False, "failed_element": "Time", "reason": "Task takes too long."}
        
    
    if task['cost_dollars'] > user['budget_dollars']:
        return {"can_do": False, "failed_element": "Money", "reason": "User cannot afford it."}
        
    
    return {"can_do": True, "failed_element": None, "reason": "All 6 elements align."}



primary_task = {
    "name": "Record Video Testimonial",
    "time_required_mins": 10,
    "cost_dollars": 0,
}


user_on_train = {
    "name": "Marcus",
    "time_available_mins": 30, 
    "budget_dollars": 100,
}




result = evaluate_ability_chain(user_on_train, primary_task)

if result["can_do"]:
    print("Result: 📲 Sending prompt for Video Testimonial!")
else:
    print(f"FAILED on link: {result['failed_element']} - {result['reason']}")
    print("Adapting the system...")
    
    
    if result["failed_element"] == "Social Deviance":
        print("📲 Adaptive Prompt: 'Hey Marcus, want to leave a quick *written* 5-star review instead?'")
    elif result["failed_element"] == "Brain Cycles":
        print("📲 Adaptive Prompt: 'Hey Marcus, just click one of these 3 pre-written reviews to submit!'")