x = 5 
y = 7
print(x+y)
#output 12

x = 10
y = "John"
print(str(x)+y)
#redefining x as a string value, and then concatenating both x and y
#output 10John

x = "2"
y = 1
print(int(x)+y)
#redefining x as an integer, so adding with y works.
#output 3

x = "Sam"
y = "Cheese"
print(f"my username is {x} {y}")
#output my username is Sam Cheese

print("thanks for using this program")
pet_name = input("what is your pet's name? ")
born_city = input("in which city were you born in? ")
print(f"your new twitter handle and bio @cyber{pet_name} from {born_city}")
#thanks the user for using this program, and then asks for his pet's name and city they were born in
#to then print out a message with that data.