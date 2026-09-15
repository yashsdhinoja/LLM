#  IQ = (Mental Age / Chronological Age) × 100

# Mental Age (MA): The intellectual performance level measured by a test.Chronological Age.
# Chronological Age (CA): The actual number of years a person has lived.
# Example: If a child has a mental age of 12 and an actual age of 10, the calculation is (12 / 10) × 100 = 120 IQ.

def calculate_qi(mental_age, chronological_age):
    return (mental_age / chronological_age) * 100

print("*=*=*=*=*=*=*=*=*=*>>>>> IQ TEST <<<<<<*=*=*=*=*=*=*=*=*=*\n")

mental_age = float(input("Enter Mental Age (How you Think) in years: "))
chronological_age = float(input("Enter Chronological Age (Real Age) in years: "))

if chronological_age <= 0:
    print("Error: Chronological Age must be greater than 0")
else:
    iq = calculate_qi(mental_age, chronological_age)

if iq < 70:
    print(f"IQ Score: {iq:.2f} || Category: Extremely low / Borderline intellectual functioning")
elif iq <= 89:
    print(f"IQ Score: {iq:.2f} || Category: Below Average")
elif iq <= 109:
    print(f"IQ Score: {iq:.2f} || Category: Average intelligence (majority of population)")
elif iq <= 119:
    print(f"IQ Score: {iq:.2f} || Category: Above average / High Average")
elif iq <= 129:
    print(f"IQ Score: {iq:.2f} || Category: Superior / Bright")
else:
    print(f"IQ Score: {iq:.2f} || Category: Very superior / Gifted intelligence (Top 2%)")