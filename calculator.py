num_1 = int(input("enter the number"))
num_2 = int(input("enter the another number"))


choice = input("enter the operation + - * /")
if choice == "+":

    sum = num_1 + num_2
    print(sum)

if choice == "-":
    
    diff = num_1 - num_2
    print(diff)

if choice == "*":
    mul = num_1 * num_2
    print(mul)

if choice == "/":
    div = num_1 / num_2
    print(div)