print(" ")
print(" ")
print(" ============ Welcome to the Bank ============ ")
print(" ")
print(" 1. Compound Interest ")
print(" 2. Simple Interest ")
print(" 3. Principal_Amount ")
print(" 4. Rate (%) ")
print(" 5. Time ")
print(" ")
print(" ============ End ============ ")
print(" ")
print(" ")

nnn = int(input(" Enter the Calculate of Choice ==:== "))

match nnn:
    case 1: 
        def Compound_Interest(principal_amount, rate, interest, time):

            rate = rate / 100
            return principal_amount * (1 + rate / interest) ** (interest * time)

        print("  ")
        print(" -------------------------------------------------------- ")
        print(" ====== Welcome to Calculate the Compound Interest ====== ")
        print(" -------------------------------------------------------- ")
        print("  ")
       
        principal_amount = float(input("Enter Number Principal Amount = "))
        rate = float(input("Enter Number Rate (%) = "))
        interest = float(input("Enter Number of times Interest is Compounded per Year = "))
        time = float(input("Enter Number of Years = "))
        
        ci_total = Compound_Interest(principal_amount, rate, interest, time)
        print(ci_total)

    case 2:
        def Simple_Interest(principal_amount, rate, time):
            return principal_amount * rate * time / 100

        print("  ")
        print(" -------------------------------------------------------- ")
        print(" ====== Welcome to Calculate the Simple Interest ====== ")
        print(" -------------------------------------------------------- ")
        print("  ")

        principal_amount = float(input("Enter Number Principal Amount = "))
        rate = float(input("Enter Number Rate (%) = "))
        
        si_total = Simple_Interest(principal_amount, rate,time)
        print(si_total)

    case 3:
        def Principal_Amount(simple_interest, rate, time):
    
            return simple_interest * 100 / rate * time

        print("  ")
        print(" -------------------------------------------------------- ")
        print(" ====== Welcome to Calculate the Principal_Amount ====== ")
        print(" -------------------------------------------------------- ")
        print("  ")

        simple_interest = float(input("Enter Number Simple_Interest = "))
        rate = float(input("Enter Number Rate (%) = "))
        time = float(input("Enter Number of Years = "))

        Pri_total = Principal_Amount(simple_interest, rate, time)
        print(Pri_total)

    case 4:
        def Rate(simple_interest,principal_amount,time):
    
            return 100 * simple_interest / principal_amount * time

        print("  ")
        print(" -------------------------------------------------------- ")
        print(" ====== Welcome to Calculate the Rate (%) ====== ")
        print(" -------------------------------------------------------- ")
        print("  ")

        simple_interest = float(input("Enter Number Simple_Interest = "))
        principal_amount = float(input("Enter Number Principal Amount = "))
        time = float(input("Enter Number of Years = "))

        rate = Rate(simple_interest, principal_amount, time)
        print(rate)

    case 5:
        def Time(simple_interest, principal_amount, rate):

            return 100 * simple_interest / principal_amount * rate

        print("  ")
        print(" -------------------------------------------------------- ")
        print(" ====== Welcome to Calculate the Time Period ====== ")
        print(" -------------------------------------------------------- ")
        print("  ")

        simple_interest = float(input("Enter Number Simple_Interest = "))
        principal_amount = float(input("Enter Number Principal Amount = "))
        rate = float(input("Enter Number Rate (%) = "))

        time = Time(simple_interest, principal_amount, rate)
        print(time)

    case _:
        print(" =====>> No Matching <<===== ")