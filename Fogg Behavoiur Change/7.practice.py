def practice(user, ability):

    # 1 defined the name of person and name of task
    print(f"\n Mr. {user['name']} your task is to : '{ability['name']}'")
    
    # 2 time_required_avaiable_conditions...
    if ability['time_required_mins'] > user['time_avaible_mins']:
        print("why_","❌ failed_element","Task can takes long Time to Complete !!!")
    else:
        print("✅ Success_element","He can complete the work.")
    
    # 3 payment_and_free...
    if ability['cost_dollars'] > user['cost_price']:
        print("why_","❌ failed_element","Too costly Game. !!!")
    else:
        print("✅ Success_element","Let's Play Game. ")

    # 4 physical_health_for_work...
    if ability['physical_power'] > user['physical_energy']:
        print("why_","❌ failed_element","Game is compliance or I am tired !!!")
    else:
        print("✅ Success_element","Easy to Play Game")
    
ability_task = {
    "name": "playing game",
    "time_required_mins": 18,
    "cost_dollars":10,
    "physical_power": 9
}

user_task = {
    "name": "Dhinoja",
    "time_avaible_mins": 15,
    "cost_price":50,
    "physical_energy": 7
}

Ans = practice(user_task, ability_task)

if Ans is not None and Ans.get("why_") is not None:
    print("Result: Sending More Prompt for Continous playing game")
else:
    print(f"FAILED on link : ")
    print("Adapting the system... ")

    if Ans["why_"] == "time_avaible_mins":
        print(f"📲 Adaptive Prompt: 'Hey {user_task['name']}, want to leave a quick *written* 5-star review instead?'")
    elif Ans["why_"] == "physical_energy":
        print(f"📲 Adaptive Prompt: 'Hey {user_task['name']}, just click one of these 3 pre-written reviews to submit!'")