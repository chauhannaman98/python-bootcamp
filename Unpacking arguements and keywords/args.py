def multiply(*args):
    print(args)
    product = 1
    for arg in args:
        product *= arg
    
    return product

def apply(*args, operator):
    if operator=='+':
        return sum(args)
    if operator=='*':
        return multiply(*args)
    else:
        print("Invalid operator")

print(apply(1,2,3, operator="+"))

# *args = ((1,2,3),)    
# args = (1,2,3)