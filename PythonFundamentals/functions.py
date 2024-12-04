#takes 2 numbers, x and y, and checks if the numbers between them, including x and excludin y
#are divisible by 3, divisible by 5, or divisable by both.
#if they dont meet those "requirements", it will just print out the number.
def function():
    start = int(input("what number will be the start? (Included): "))
    finish = int(input("what number will be the end? (Excluded): "))
    for number in range (start,finish):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
    
    
def printName():
    name = input("What is your name?")
    print(f"hello {name}")
