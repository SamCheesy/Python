fruits = ["apple", "banana", "cherry"]

#print every fruit in the list of fruits
for i in fruits:
    print(i)
    
#same thing, but adds the Pie string
for i in fruits:
    print(i + " Pie")

#prints all the numbers from 1 to 9. this is because it includes the first number, but excludes the second one.
for num in range (1,10):
    print(num)
    
#prints all the numbers from 0 to 100, following the same rule, first included, second excluded.
#third number means the difference between each consecutive number in the range.
#here, it will start on 0, and have an increment of 2.
#so third argument means like, increment.
#so it prints out even numbers.
for num in range (0, 100, 2):
    print(num)

#does the same thing as with third argument, but using an if statement.
for num in range (0, 100):
    if num % 2 == 0:
        print(num)
