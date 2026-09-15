# --- MOCK USERS (Declared at the top of the file) ---

# Emma really wants to save for a trip (High Motivation), 
# but she is 2 days away from payday and her account is low (Low Ability).
user_emma = {
    "name": "Emma",
    "motivation": 9,
    "ability": 2  
}

# David just got paid so he has plenty of cash (High Ability), 
# but he wants to buy video games, not save (Low Motivation).
user_david = {
    "name": "David",
    "motivation": 3,
    "ability": 9  
}

# Sophia just got paid and is highly focused on her goals.
user_sophia = {
    "name": "Sophia",
    "motivation": 8,
    "ability": 8
}

# --- THE PERSUASION ALGORITHM ---

def send_savings_nudge(user):
    """
    Analyzes a user's financial context to send a persuasive savings prompt.
    The default goal is to get the user to save $50 today.
    """
    print(f"\n--- Analyzing Saver: {user['name']} ---")

    motivation = user['motivation']
    ability = user['ability']
    score = motivation + ability

    if score < 10:
        print(f"Diagnosis: Score is {score}. Standard $50 savings prompt will fail.")
        
        if ability < 5:
            # Low Ability = They don't have $50 to spare right now.
            # Strategy: Micro-commitments. Ask for an amount they won't even notice.
            print("Strategy: Decrease friction (Micro-savings).")
            print(f"Result: 📲 Notification: 'Hey {user['name']}, things are tight before payday! Just stash away $1 today to keep your savings habit going.'")
            
        else:
            # Low Motivation = They have money, but want to spend it on fun stuff.
            # Strategy: Visualization / Future Pacing. Remind them WHY they are saving.
            print("Strategy: Increase motivation (Future Pacing).")
            print(f"Result: 📲 Notification: 'Hey {user['name']}, you have cash to spare! If you save $50 today, you'll reach your Hawaii Vacation goal a week early!'")
            
    else:
        # High Motivation AND High Ability
        print(f"Diagnosis: Score is {score}. Perfect conditions.")
        print("Strategy: Standard prompt.")
        print(f"Result: 📲 Notification: 'Payday feels good, {user['name']}! Tap here to securely transfer your $50 weekly savings.'")

# --- EXECUTING THE CODE ---
# Running the function for all three users
send_savings_nudge(user_emma)
send_savings_nudge(user_david)
send_savings_nudge(user_sophia)