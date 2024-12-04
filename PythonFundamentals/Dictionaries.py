#dictionaries are key: value, separated by comas.
juan = {
    "age":16,
    "favorite fruit":"Apple",
    "favorite game":"Hearts Of Iron 5"
}

print(juan)
#we get the value of a certain key by calling the key, which in this case, we're calling "age", to get 16.
print(f"edad: {juan["age"]}")

#to add something to our dictionary, we can do this:
juan["skin tone"] = "white"
print(juan)
#this will output the same dictionary we have from before, but there will be a new key called "skin tone",
#with the value of "white".

#to print only the keys, we can do this:
for key in juan:
    print(key)

#to print only the values, we can do this:
for key in juan:
    print(juan[key])

#to empty a dictionary, we can do this:
juan = {}
print(juan)
#output: empty dictionary



    
