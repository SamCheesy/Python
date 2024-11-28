#takes 2 numbers, x and y, and checks if the numbers between them, including x and excludin y
#are divisible by 3, divisible by 5, or divisable by both.
#if they dont meet those "requirements", it will just print out the number.

start = int(input("what number will be the start? (Included): "))
finish = int(input("what number will be the end? (Excluded): "))

def function(x, y):
    for number in range (x,y):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
    
function(start, finish)