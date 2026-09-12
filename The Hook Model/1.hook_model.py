import random # We import the random module to create the "Variable Reward"
import time   # We import the time module to add slight pauses for realism

def run_hook_model_simulation():
    # We use a variable to track the user's "Investment" (stored value) over time
    user_content_created = 0
    
    print("Welcome to the Hook Model Simulator!")
    print("Press CTRL+C at any time to break the habit and exit.\n")
    
    # A while loop creates the continuous cycle of the habit-forming product
    while True:
        
        # ==========================================
        # STEP 1: TRIGGER (The Spark)
        # ==========================================
        # This simulates an external trigger (a notification) 
        # combining with an internal trigger (boredom).
        print("-" * 40)
        print("[TRIGGER] Your phone buzzes. You have a few minutes to kill.")
        
        # ==========================================
        # STEP 2: ACTION (The Behavior)
        # ==========================================
        # The action must be incredibly simple. 
        # Here, it requires just pressing the Enter key to 'open the app'.
        user_input = input("[ACTION] Press Enter to open the app and scroll... ")
        
        # We add a tiny delay to simulate the app loading and build anticipation
        time.sleep(1) 
        
        # ==========================================
        # STEP 3: VARIABLE REWARD (The Hook)
        # ==========================================
        # To make it habit-forming, the reward cannot be the same every time.
        # We create a list of possible outcomes (good, great, and boring).
        possible_rewards = [
            "1. Rewards of the Tribe: You got 15 new likes on your last photo!",
            "2. Rewards of the Hunt: You found an incredibly funny meme.",
            "3. Rewards of the Self: You cleared all your unread messages.",
            "4. Nothing exciting this time. Just a bunch of ads.",
            "5. Rewards of the Tribe: Your friend tagged you in a hilarious video."
        ]
        
        # We use random.choice() to pick one reward unpredictably (like a slot machine)
        actual_reward = random.choice(possible_rewards)
        print(f"[VARIABLE REWARD] {actual_reward}")
        
        # ==========================================
        # STEP 4: INVESTMENT (The Trap)
        # ==========================================
        # We ask the user to put something into the app to make it better for next time.
        print("\n[INVESTMENT] Would you like to post a quick update? (y/n)")
        investment_choice = input("> ").strip().lower() # Read user input and make it lowercase
        
        if investment_choice == 'y':
            # If they invest, we increase their stored value in the app
            user_content_created += 1
            print(f"Update posted! You now have {user_content_created} posts on your profile.")
            print("This investment makes you more likely to return for likes tomorrow.")
        else:
            print("You closed the app without posting.")
            
        # Pause before the loop starts again, simulating time passing between app usages
        print("\nWaiting for the next urge...\n")
        time.sleep(3) 

# This is the standard way to run a Python script
if __name__ == "__main__":
    try:
        # We call the function to start the simulation
        run_hook_model_simulation()
    except KeyboardInterrupt:
        # This handles the user pressing CTRL+C gracefully without throwing a massive error
        print("\n\nYou broke the cycle! Exiting the simulator.")