# The 6 Elements of Simplicity (Ability)

def evaluate_ability_chain(user, task):
    """
    Checks the 6 elements of Ability. If even ONE element fails, 
    the user cannot complete the task, and we must adapt.
    """
    print(f"\nEvaluating if {user['name']} can do: '{task['name']}'")
    
    # 1. TIME
    if task['time_required_mins'] > user['time_available_mins']:
        return {"can_do": False, "failed_element": "Time", "reason": "Task takes too long."}
        
    # 2. MONEY
    if task['cost_dollars'] > user['budget_dollars']:
        return {"can_do": False, "failed_element": "Money", "reason": "User cannot afford it."}
        
    # 3. PHYSICAL EFFORT (Scale 1-10)
    if task['physical_effort'] > user['physical_energy']:
        return {"can_do": False, "failed_element": "Physical Effort", "reason": "User is too physically tired."}
        
    # 4. BRAIN CYCLES (Scale 1-10: How much thinking is required?)
    if task['cognitive_load'] > user['mental_bandwidth']:
        return {"can_do": False, "failed_element": "Brain Cycles", "reason": "User is mentally exhausted (Brain dead)."}
        
    # 5. SOCIAL DEVIANCE (Does it make them look weird in public?)
    if task['is_socially_awkward'] and user['is_in_public']:
         return {"can_do": False, "failed_element": "Social Deviance", "reason": "User is in public; won't do awkward tasks."}
         
    # 6. NON-ROUTINE (Does it break their normal habits?)
    if task['breaks_routine'] and not user['is_flexible_today']:
         return {"can_do": False, "failed_element": "Non-Routine", "reason": "User is stuck in their daily routine."}

    # If they pass all 6 checks, the chain is intact!
    return {"can_do": True, "failed_element": None, "reason": "All 6 elements align."}

# --- MOCK DATA ---
# The Task: Record a 10-minute video testimonial for an app (Free, but takes time and is awkward in public)
primary_task = {
    "name": "Record Video Testimonial",
    "time_required_mins": 10,
    "cost_dollars": 0,
    "physical_effort": 2, # Just holding the phone
    "cognitive_load": 0,  # Have to think about what to say
    "is_socially_awkward": True, # Talking to a camera out loud
    "breaks_routine": True
}

# User A: Just got off work, sitting on the train surrounded by people.
user_on_train = {
    "name": "Marcus",
    "time_available_mins": 30, # Has time
    "budget_dollars": 100,
    "physical_energy": 5,
    "mental_bandwidth": 0,     # Tired from work
    "is_in_public": True,      # On a crowded train!
    "is_flexible_today": False
}


# --- THE EXECUTION ALGORITHM ---

result = evaluate_ability_chain(user_on_train, primary_task)

if result["can_do"]:
    print("Result: 📲 Sending prompt for Video Testimonial!")
else:
    print(f"FAILED on link: {result['failed_element']} - {result['reason']}")
    print("Adapting the system...")
    
    # ADAPTIVE LOGIC: Fix the specific broken link
    if result["failed_element"] == "Social Deviance":
        print("📲 Adaptive Prompt: 'Hey Marcus, want to leave a quick *written* 5-star review instead?'")
    elif result["failed_element"] == "Brain Cycles":
        print("📲 Adaptive Prompt: 'Hey Marcus, just click one of these 3 pre-written reviews to submit!'")