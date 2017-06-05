import random

def msg(room):
    if room['msg'] == '': # There is no custom message
        return "You have entered the  " + room['name'] + '.'
    else:
        return room['msg']

def get_choice(room,walk):
    if walk == 'N':
        choice = 0
    elif walk == 'E':
        choice = 1
    elif walk == 'S':
        choice = 2
    elif walk == 'W':
        choice = 3
    else:
        return -1

    if room['directions'][choice] == 0:
        return 4
    else:
        return choice

def main():
    dirs = (0,0,0,0) # default directionals

    entrance = {"name": "Entrance Way", "directions": dirs, "msg":""}
    livingroom = {"name": "Living Room", "directions": dirs, "msg":""}
    hallway = {"name": "Hallway", "directions": dirs, "msg":""}
    kitchen = {"name": "Kitchen", "directions": dirs, "msg":""}
    diningroom = {"name": "Dining Room", "directions": dirs, "msg":""}
    family_room = {"name": "Family Room", "directions": dirs, "msg":""}

    # DIRECTION ARE TUPLES:  ROOMS TO THE (N, E, S, W)
    entrance["directions"] = (kitchen, livingroom, 0, 0)
    livingroom["directions"] = (diningroom, 0, 0, entrance)
    hallway["directions"] = (0, kitchen, 0, family_room)
    kitchen["directions"] = (0, diningroom, entrance, hallway)
    diningroom["directions"] = (0, 0, livingroom, kitchen)
    family_room["directions"] = (0, hallway, 0, 0)

    # Rooms where the bomb might be
    rooms =[livingroom,hallway,kitchen,diningroom,family_room]
    room_with_bomb = random.choice(rooms)
    bomb_delivered = False
    room = entrance
    print("Welcome, Mr. Bond...can you plant the bomb and get out without being seen?")

    while True:
        if bomb_delivered and room["name"] == "Entrance Way":
            print("You've planetd the bomb and made it back to the entrance!")
            break;
        elif not bomb_delivered and room["name"] == room_with_bomb["name"]:
            bomb_delivered = True
            print(msg(room) + "You plant the bomb in the room you need to.  GET OUT!")

            room["msg"] = ("You are back in the " + room["name"] + "and have already planted the bomb.  Get out before the terrorist wakes up!")

        else:
            print(msg(room))
            room["msg"] = "You are back in the " + room["name"]


        stuck = True
        while stuck:
            walk = input("Which direction would you like to go: N, E, S, or W? ")
            choice = get_choice(room,walk)
            if choice == -1:
                print("Please enter N, E, S, or W.")
            elif choice == 4:
                print("You can't go in that direction.")
            else:
                room = room['directions'][choice]
                stuck = False

main()



