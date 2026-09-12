import random
import time

# ==========================================
# CONCEPT 1: COMPLEX USER PROFILES
# ==========================================
# We use a Class to define a user's unique psychological state.
class UserProfile:
    def __init__(self, name, primary_trigger):
        self.name = name
        # Each user has a unique internal trigger (e.g., 'loneliness', 'FOMO')
        self.primary_trigger = primary_trigger 
        
        # Concept 2 Variables: Habit Degradation trackers
        self.motivation = 10                  # Starts high, but can drop
        self.consecutive_boring_rewards = 0   # Tracks if the app is getting stale
        self.investment_score = 0             # Tracks "Sunk Cost"

def advanced_hook_simulation():
    print("=== Advanced Hook Model Simulator ===")
    print("Featuring: Complex Profiles & Habit Degradation\n")
    
    # We instantiate our complex user profile
    current_user = UserProfile(name="Alex", primary_trigger="social anxiety")
    print(f"User Loaded: {current_user.name} | Internal Trigger: {current_user.primary_trigger}")
    print("-" * 40)
    
    while True:
        # ==========================================
        # STEP 1: TRIGGER
        # ==========================================
        print(f"\n[TRIGGER] {current_user.name} feels a wave of {current_user.primary_trigger}.")
        print("A push notification arrives: 'See what your network is talking about!'")
        
        # ==========================================
        # STEP 2: ACTION & DEGRADATION (Friction)
        # ==========================================
        # We simulate "friction"—server lag, a confusing UI update, or requiring a password.
        friction = random.randint(1, 14)
        
        # Fogg Behavior Model: B=MAP. 
        # Action only occurs if Motivation + Ability (boosted by past investments) > Friction
        effective_motivation = current_user.motivation + (current_user.investment_score * 0.5)
        
        print(f"[ACTION] Attempting to open app... (Friction: {friction} vs Effective Motivation: {effective_motivation})")
        
        if friction > effective_motivation:
            # If the app is too hard to use right now, the user churns.
            print("\n[!] The app took too long to load or required a password.")
            print(f"[!] {current_user.name} gave up. Habit degraded and cycle broken!")
            break # Exits the while loop, ending the simulation
        
        print("-> Action successful! App opened.")
        time.sleep(1)
        
        # ==========================================
        # STEP 3: VARIABLE REWARD & DEGRADATION (Staleness)
        # ==========================================
        # We categorize rewards to measure when the app stops being engaging.
        rewards = [
            ("High", "Rewards of the Tribe: 5 friends loved your comment!"),
            ("Medium", "Rewards of the Hunt: Found an interesting new creator."),
            ("Low", "Nothing new. Just repetitive ads and old posts.")
        ]
        
        # random.choices allows us to weight the probabilities. 
        # We give "Low" rewards a 30% chance to simulate a boring session.
        reward_level, reward_text = random.choices(rewards, weights=[30, 40, 30], k=1)[0]
        print(f"[VARIABLE REWARD] {reward_text}")
        
        if reward_level == "Low":
            # The app failed to deliver a dopamine hit.
            current_user.consecutive_boring_rewards += 1
            current_user.motivation -= 2 
            print(f"-> Disappointing visit. Motivation dropped to {current_user.motivation}.")
        else:
            # The app delivered, so we reset the boredom counter and boost motivation.
            current_user.consecutive_boring_rewards = 0 
            current_user.motivation += 1 
            print(f"-> Dopamine hit! Motivation increased to {current_user.motivation}.")
            
        # If the user gets two "Low" rewards in a row, the variability is gone. They quit.
        if current_user.consecutive_boring_rewards >= 2:
            print("\n[!] Too many boring visits in a row. The reward became predictable.")
            print(f"[!] {current_user.name} uninstalled the app. Habit broken!")
            break
            
        # ==========================================
        # STEP 4: INVESTMENT
        # ==========================================
        print("\n[INVESTMENT] Would you like to write a new post to connect with people? (y/n)")
        choice = input("> ").strip().lower()
        
        if choice == 'y':
            # Increasing the investment score makes future 'Friction' easier to overcome
            current_user.investment_score += 1
            print(f"Post published! Sunk cost increased. (Investment Score: {current_user.investment_score})")
            print("-> This investment makes it easier to overcome friction in the next cycle.")
        else:
            print("Skipped investment. Your connection to the app remains weak.")
            
        print("\nWaiting for the next trigger...")
        time.sleep(2)

if __name__ == "__main__":
    try:
        advanced_hook_simulation()
    except KeyboardInterrupt:
        print("\nSimulation ended manually.")