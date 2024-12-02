def attack(ip, url):
    print(ip)

width_room = float(input("What is the width of the room?: "))
height_room = float(input("what is the height of the room?: "))

def sqft(width, height):
    sqft = width * height
    print(f"the square foot of the room is: {sqft}")

sqft(width_room, height_room)