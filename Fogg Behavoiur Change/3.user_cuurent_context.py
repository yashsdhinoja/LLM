# Persuasive Technique: Adapting to User Context (Fogg Behavior Model)

def send_study_nudge(user):
    """
    Analyzes a user's current context to send the perfect study reminder.
    """
    print(f"\n--- Analyzing Learner: {user['name']} ---")

    motivation = user['motivation']
    ability = user['ability']

    # The Action Line (Motivation + Ability must be at least 10)
    score = motivation + ability

    # THE PERSUASIVE LOGIC
    if score < 10:
        print(f"Diagnosis: Score is {score}. Too low for a standard lesson.")
        
        if ability < 5:
            # Low Ability = They are busy or tired. 
            # Strategy: Decrease friction. Make the task incredibly small.
            print("Strategy: Lower the barrier to entry (Simplicity).")
            print(f"Result: 📲 Notification: 'Hey {user['name']}, too busy? Just do a quick 1-minute vocab review to keep your habit alive!'")
            
        else:
            # Low Motivation = They have time, but they are feeling lazy.
            # Strategy: Gamification or Loss Aversion (fear of losing something).
            print("Strategy: Increase motivation (Loss Aversion / Gamification).")
            print(f"Result: 📲 Notification: 'Hey {user['name']}, you are about to drop out of the Gold League! Do one quick lesson to secure your spot.'")
            
    else:
        # High Motivation AND High Ability
        # Strategy: Challenge them. They are in the perfect state of mind.
        print(f"Diagnosis: Score is {score}. Perfect state of mind.")
        print("Strategy: Standard prompt with a challenge.")
        print(f"Result: 📲 Notification: 'Ready to level up, {user['name']}? Your 10-minute Spanish challenge is waiting!'")

# --- MOCK USERS (Like Jordan and Mia) ---

# Leo is super motivated (loves Spanish) but is currently at work (low ability to study)
user_leo = {
    "name": "Leo",
    "motivation": 1,
    "ability": 3  
}

# Zoe has plenty of free time (chilling at home) but is feeling very lazy today (low motivation)
user_zoe = {
    "name": "Zoe",
    "motivation": 4,
    "ability": 1  
}

# # Sam is highly motivated and just got off work (high ability)
user_sam = {
    "name": "Sam",
    "motivation": 8,
    "ability": 8
}

# Let's run the algorithm on our learners!
send_study_nudge(user_leo)
# send_study_nudge(user_zoe)
# send_study_nudge(user_sam)