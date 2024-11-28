### if statement ###

first_number = input("what is the first number? ")
second_number = input("What is the second number? ")

if first_number > second_number:
    print("the first number is greater than the second number.")
elif second_number > first_number:
    print("the second number is greater than the first number.")
else:
    print("the numbers are the same.")
    

score = int(input("what is your score (out of 100)? "))
if 0 <= score <= 100:
    if score >= 90:
        print("your grade is A.")
    elif score >= 80:
        print("your grade is B.")
    elif score >= 70:
        print("your grade is C.")
    else:
        print("your grade is F.")
else:
    print("score has to be larger or equal to 0 and less or equal to 100.")







