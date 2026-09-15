while True:
    print(" ============ EMI Calculate ============ ")
    print(" ")
    print(" 1. Compound Interest ")
    print(" 2. Simple Interest ")
    print(" 3. Principal_Amount ")
    print(" 4. Rate (%) ")
    print(" 5. Time (period) ")
    print(" 6. Exit ")
    print(" ")
    print(" ============ End ============ ")
    print(" ")

    try:
        choice = int(input(" Enter the number between ==>> (1 - 6) "))
    except ValueError:
        print("try again")
        continue

    # Compound Interest
    if choice == 1:
        def Compound_Interest(principal_amount, rate, interest, time):

            rate = rate / 100
            return principal_amount * (1 + rate / interest) ** (interest * time)

    
        print("  ")
        print(" -------------------------------------------------------- ")
        print(" ====== Welcome to Calculate the Compound Interest ====== ")
        print(" -------------------------------------------------------- ")
        print("  ")

        principal_amount = float(input("Enter Principal Amount = "))
        rate = float(input("Enter Rate (%) = "))
        interest = float(input("Enter Number of Times Interest is Compounded Per Year = "))

        print("\nSelect Time Duration")
        print("1. 12 Months")
        print("2. 24 Months")
        print("3. 36 Months")
        print("4. 48 Months")

        choice = int(input("Enter Choice = "))

        match choice:
                case 1:
                    months = 12
                case 2:
                    months = 24
                case 3:
                    months = 36
                case 4:
                    months = 48
                case _:
                    print("Invalid Choice")
                    exit()

        time = months / 12
        final_amount = Compound_Interest(principal_amount, rate, interest, time)    
        compound_interest = final_amount - principal_amount

        print("\n---------------- Result ----------------")
        print(f"Principal Amount  : {principal_amount:.2f}")
        print(f"Compound Interest : {compound_interest:.2f}")
        print(f"Final Amount      : {final_amount:.2f}")

        print("\nMonth-wise Growth")
        print("--------------------------------------------------------------")
        print("Month | Interest Earned | Current Amount")
        print("--------------------------------------------------------------")

        current_amount = principal_amount
        monthly_rate = (rate / 100) / 12

        for month in range(1, months + 1):
            
            monthly_interest = current_amount * monthly_rate

            current_amount += monthly_interest

            print(f"{month:5d} | "f"{monthly_interest:15.2f} | "f"{current_amount:14.2f}")

    
    # Simple Interest
    elif choice == 2:
        def Simple_Interest(principal_amount, rate, time):
            return principal_amount * rate * time / 100

        print("------------------------------------------------")
        print("      Simple Interest Calculator")
        print("------------------------------------------------")
        
        principal_amount = float(input("Enter Principal Amount = "))
        rate = float(input("Enter Rate (%) = "))
        
        print("\nSelect Loan Duration")
        print("1. 12 Months")
        print("2. 24 Months")
        print("3. 36 Months")
        print("4. 48 Months")
        
        choice = int(input("Enter Choice = "))
        
        match choice:
            case 1:
                months = 12
            case 2:
                months = 24
            case 3:
                months = 36
            case 4:
                months = 48
            case _:
                print("Invalid Choice")
                exit()
        
        years = months / 12
        
        si = Simple_Interest(principal_amount, rate, years)
        total_amount = principal_amount + si
        monthly_interest = total_amount / months
        
        print("\n---------------- Result ----------------")
        print(f"Principal Amount : {principal_amount:.2f}")
        print(f"Simple Interest  : {si:.2f}")
        print(f"Total Amount     : {total_amount:.2f}")
        print(f"Monthly Payment  : {monthly_interest:.2f}")
        
        print("\nMonth-wise Remaining Amount")
        print("----------------------------------------")
        
        remaining = total_amount
        
        for month in range(1, months + 1):
            remaining -= monthly_interest
        
            if remaining < 0:
                remaining = 0
        
            print(f"|| Month = {month:2d} || "f"Payment = {monthly_interest:8.2f} || "f"Remaining = {remaining:10.2f} ||")

    # Principal Amount
    elif choice == 3:
        def Principal_Amount(simple_interest, rate, time):
    
            return simple_interest * 100 / rate * time

        print("  ")
        print(" -------------------------------------------------------- ")
        print(" ====== Welcome to Calculate the Principal_Amount ====== ")
        print(" -------------------------------------------------------- ")
        print("  ")

        simple_interest = float(input("Enter Number Simple_Interest = "))
        rate = float(input("Enter Number Rate (%) = "))

        print("\nSelect Loan Duration")
        print("1. 12 Months")
        print("2. 24 Months")
        print("3. 36 Months")
        print("4. 48 Months")

        choice = float(input("Enter Number of Years = "))

        match choice:
            case 1:
                months = 12
            case 2:
                months = 24
            case 3:
                months = 36
            case 4:
                months = 48
            case _:
                print(" Invalid Try ")

        years = months / 12
        principal_amount = (simple_interest * 100) / (rate * years)
        monthly_payment = principal_amount / months
        
        print("\n---------------- Result ----------------")
        print(f"Simple Interest  :  {simple_interest:.2f}")
        print(f"Rate             :  {rate:.2f}")
        print(f"Time             :  {years:.2f}")
        print(f"Principal_Amount :  {principal_amount:.2f}")

        remaining = principal_amount

        for month in range(1, months + 1):
            remaining -= monthly_payment

            if remaining < 0:
                remaining = 0

            print(f" month = {months} || --> " f"remaining = {remaining}")

    # Rate (%)
    elif choice == 4:
        def Rate(simple_interest, principal_amount, time):
            return 100 * simple_interest / principal_amount * time
    
    # Time (period)
    elif choice == 5:
        def Time(simple_interest, principal_amount,):
            return 100 * simple_interest / principal_amount * 6.57
        
        print("  ")
        print(" -------------------------------------------------------- ")
        print(" ====== Welcome to Calculate the Time ====== ")
        print(" -------------------------------------------------------- ")
        print("  ")

        simple_interest = float(input("Enter Number Simple_Interest = "))
        principal_amount = float(input("Enter Number Principal_amount = "))


        Time(simple_interest, principal_amount)
        print(Time)

    # Exit 
    elif choice == 6:
        break

    else:
        print("try again !!!")
        continue