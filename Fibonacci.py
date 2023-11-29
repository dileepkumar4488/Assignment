n = 10
number1 = 0
number2 = 1

if(n==2):
    print(f"The fibonacci series of {n} is")
    print(number1)
    print(number2)
else:
    print(f"The fibonacci series of {n} is")
    print(number1)
    print(number2)
    for i in range(n-2):
        next_seed = number1+number2
        print(next_seed)
        number1 = number2
        number2 = next_seed
