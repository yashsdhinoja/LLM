def send_personalized_motivation_nudge(username):
    # """
    # Simulates Fogg's 3 Core Motivators.
    # The user profiles are declared inside the starting lines of the function.
    # """

    # 1. DECLARING USERS INSIDE THE STARTING OF THE FUNCTION
    if username == "Toby":
        user = {
            "name": "Toby",
            "primary_motivator": "Anticipation",  # Hope vs. Fear
            "sub_state": "Fear",                  # Afraid of losing progress
            "days_active": 14,
            "has_unlocked_rewards": True
        }

        
    elif username == "Chloe":
        user = {
            "name": "Chloe",
            "primary_motivator": "Belonging",     # Acceptance vs. Rejection
            "sub_state": "FOMO ",     # Wants to feel included in a group
            "days_active": 2,
            "has_unlocked_rewards": False
        }
    elif username == "Alex":
        user = {
            "name": "Alex",
            "primary_motivator": "Sensation",     # Pleasure vs. Pain
            "sub_state": "Pleasure",              # Seeks instant gratification
            "days_active": 5,
            "has_unlocked_rewards": False
        }
    else:
        # Default fallback user
        user = {
            "name": "Guest",
            "primary_motivator": "Sensation",
            "sub_state": "Pleasure",
            "days_active": 0,
            "has_unlocked_rewards": False
        }

    print(f"\n--- Analyzing Motivation for: {user['name']} ---")
    print(f"Targeting Core Motivator: {user['primary_motivator']} ({user['sub_state']})")

    # 2. THE PERSUASIVE LOGIC FOR CORE MOTIVATORS
    
    # LEVEL 1: SENSATION (Pleasure vs. Pain)
    if user["primary_motivator"] == "Sensation":
        if user["sub_state"] == "Pleasure":
            print("Psychological Lever: Instant reward, satisfying audio/visual cues.")
            print(f"📲 Nudge: 'Hey {user['name']}, complete today's task to hear that satisfying *DING* and get double XP points!'")
        else: # Pain
            print("Psychological Lever: Avoiding uncomfortable tasks/friction.")
            print(f"📲 Nudge: 'Hey {user['name']}, let's do the easy task first so you don't get overwhelmed later.'")

    # LEVEL 2: ANTICIPATION (Hope vs. Fear)
    elif user["primary_motivator"] == "Anticipation":
        if user["sub_state"] == "Fear": # Fear of Loss (Loss Aversion)
            print("Psychological Lever: Loss Aversion (Fear of losing streak/progress).")
            print(f"📲 Nudge: 'Hey {user['name']}, your {user['days_active']}-day streak is going to expire in 1 hour! Tap to save it.'")
        else: # Hope
            print("Psychological Lever: Optimism (Anticipation of a future reward).")
            print(f"📲 Nudge: 'Hey {user['name']}, you are only 1 task away from unlocking your Mystery Badge!'")

    # LEVEL 3: BELONGING (Social Acceptance vs. Rejection)
    elif user["primary_motivator"] == "Belonging":
        if user["sub_state"] == "Social Acceptance":
            print("Psychological Lever: Community, peer connection, and status.")
            print(f"📲 Nudge: 'Hey {user['name']}, 4 people in your study group are online right now. Join them!'")
        else: # Social Rejection / FOMO (Fear of Missing Out)
            print("Psychological Lever: Fear of Missing Out (FOMO).")
            print(f"📲 Nudge: 'Hey {user['name']}, your friends are climbing the leaderboard. Don't fall behind!'")


# --- RUNNING THE FLOW ---
# We pass the username to the function, and it builds the user profile inside!
send_personalized_motivation_nudge("Toby")
send_personalized_motivation_nudge("Chloe")
send_personalized_motivation_nudge("Alex")