# The Fogg Behavior Model formula: Behavior = Motivation + Ability + Prompt (B=MAP)

# 1. Let's define two different users
user_1 = {
    "name": "Jordan",
    "motivation_level": 2, # Low motivation (Tired, doesn't want to exercise)
    "ability_level": 9,    # High ability (The gym is right next door)
}

user_2 = {
    "name": "Mia",
    "motivation_level": 8, # High motivation (Really wants to get fit)
    "ability_level": 3,    # Low ability (She is very busy today)
}

# 2. The "Action Line" 
# In psychology, Motivation + Ability must be high enough to work.
# Let's say their combined score needs to be at least 10.
ACTION_LINE = 10 

def send_prompt(user):
    """
    This function decides whether or not to send a notification (The Prompt)
    based on the user's current psychology.
    """
    print(f"\n--- Analyzing User: {user['name']} ---")
    
    # Calculate their current psychological state
    current_state = user["motivation_level"] + user["ability_level"]
    
    # 3. The Logic (This is Persuasive Tech in action)
    if current_state >= ACTION_LINE:
        print(f"Score: {current_state} (Above Action Line)")
        print(f"Result: 📲 Sent notification to {user['name']}! They will likely click it.")
    else:
        print(f"Score: {current_state} (Below Action Line)")
        print(f"Result: 🛑 Skipped {user['name']}. If we notify them now, it will just annoy them.")

# Let's test our two users!
send_prompt(user_1)
send_prompt(user_2)

# --- HOW TO FIX FAILED PROMPTS ---
# If Mia's score is too low because Ability is a 3 (she's busy), 
# Persuasive Tech says we shouldn't yell at her to work out harder. 
# Instead, we increase her ABILITY by making the workout easier (e.g., a 5-minute stretch).