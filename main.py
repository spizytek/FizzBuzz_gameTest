for m in range(1, 101):
    if ( ((m % 3) == 0) and ((m % 5) == 0)):
        print("FizzBuzz")
    #fizz
    elif ( (m == 3) or ((m % 3) == 0)):
        print("Fizz")
    #buzz
    elif ((m == 5) or ((m % 5) == 0)):
        print("Buzz")
    else:
        print(m)