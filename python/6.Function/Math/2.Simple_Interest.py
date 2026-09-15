def si(p,r,t):
    return p * r * t / 100 
Simple_Interest = si(95000, 5.5, 1)

input = print("")

def p(si,r,t):
    return 100 * si / r * t
principal = p(10000, 5, 1)
print(principal)