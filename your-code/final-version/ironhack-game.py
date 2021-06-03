# -*- coding: utf-8 -*-

# In[1]:


# define rooms and items
# All Objects (furniture)

career_hack_chairs = {
    "name": "career_hack_chairs",
    "type": "furniture",
}

dish_washer = {
    "name": "dish_washer",
    "type": "furniture",
}

eating_seats = {
    "name": "eating_seats",
    "type": "furniture",
}

toilet_m = {
    "name": "toilet_m",
    "type": "furniture",
}

toilet_f = {
    "name": "toilet_f",
    "type": "furniture",
}

# All Objects (human)

catarina = {
    "name": "catarina",
    "type": "furniture",
    "message": "Welcome to IronHack. I'm Catarina and will do my best to get your dream-job. You can now move to the "
               "next room "
}

david = {
    "name": "david",
    "type": "furniture",
}

fred = {
    "name": "fred",
    "type": "furniture",
}

# All Objects (door)

door_a = {
    "name": "door_a",
    "type": "door",
}

door_b = {
    "name": "door_b",
    "type": "door",
}

door_c = {
    "name": "door_c",
    "type": "door",
}

door_d = {
    "name": "door_d",
    "type": "door",
}

door_e = {
    "name": "door_e",
    "type": "door",
}

door_f = {
    "name": "door_f",
    "type": "door",
}

door_g = {
    "name": "door_g",
    "type": "door",
}

# All Objects (rooms)

presentation_room = {
    "name": "presentation_room",
    "type": "room",
}

dinning_room = {
    "name": "dinning_room",
    "type": "room",
}

corridor = {
    "name": "corridor",
    "type": "room",
}

hallway = {
    "name": "hallway",
    "type": "room",
}

data_analytics_room = {
    "name": "data_analytics_room",
    "type": "room",
}

web_dev_room = {
    "name": "web_dev_room",
    "type": "room",
}

conference_room = {
    "name": "conference_room",
    "type": "room",
}

outside = {
    "name": "outside",
    "type": "room"
}

# All Objects (keys)

key_1 = {
    "name": "careerhack",
    "type": "key",
    "target": door_a,
}
key_2 = {
    "name": "class",
    "type": "key",
    "target": door_b,
}
key_3 = {
    "name": "key_3",
    "type": "key",
    "target": door_c,
}
key_4 = {
    "name": "open",
    "type": "key",
    "target": door_d,
}
key_5 = {
    "name": "key_5",
    "type": "key",
    "target": door_e,
}
key_6 = {
    "name": "breakfast",
    "type": "key",
    "target": door_f,
}
key_7 = {
    "name": "diploma",
    "type": "key",
    "target": door_g,
}
all_rooms = [presentation_room,
             dinning_room,
             corridor,
             hallway,
             data_analytics_room,
             web_dev_room,
             conference_room,
             outside]

all_doors = [door_a, door_b, door_c, door_d, door_e, door_f, door_g]
# define which items/rooms are related
object_relations = {
    "presentation_room": [career_hack_chairs, catarina, door_a],
    "catarina": [key_1],

    "door_a": [presentation_room, dinning_room],
    "dinning_room": [dish_washer, eating_seats, door_a, door_b],
    "dish_washer": [key_2],
    "eating_seats": [key_6],
    "door_f": [data_analytics_room, corridor],
    "door_b": [dinning_room, corridor],
    "corridor": [door_b, door_c, door_d, door_e, door_f],
    "door_d": [corridor, hallway],
    "data_analytics_room": [david, fred, door_f],
    "david": [key_7],
    "door_g": [outside],
    "hallway": [toilet_m, toilet_f, door_d, door_g],
    "outside": [door_g]
}

INIT_GAME_STATE = {
    "current_room": presentation_room,
    "keys_collected": [key_4],
    "target_room": outside
}

user_data = {
    "name": "",
    "user_gender": "",
}


# In[2]:


def linebreak():
    """
    Print a line break
    """
    print("\n")


def user():
    user_data["name"] = input("Hi! Welcome to our little IronHack-game. Please, give us your name: ")
    user_data["user_gender"] = input(
        "We're sorry, but our bathrooms have a binary system, what is your gender? 'M or 'F: ")
    linebreak()
    print("Ok! Now lets start this journey!")


def play_again():
    play = input("Do you want to do it again? 'yes' or 'no': ")
    if play == "yes":
        start_game()


def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))


def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if (not current_room == room):
            return room


def start_game():
    """
    Start the game and calls for the user data
    """
    user()
    print(
        "This is your first day at IronHack! You fill excited, nervous and anxious with so many information! \nYou must explore each room to find the necessary keys to continue.")
    play_room(game_state["current_room"])


def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None

    for item in object_relations[current_room["name"]]:
        if (item["name"] == item_name):
            output = "You examine " + item_name + ". "
            if (item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if (key["target"] == item):
                        have_key = True
                if (have_key):
                    output += "You unlock it with a key you have."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "You're not supposed to go there."
            else:
                if (item["name"] in object_relations and len(object_relations[item["name"]]) > 0) or item["type"] == "furniture":
                    if item["name"] == "catarina":
                        item_found = object_relations[item["name"]].pop()
                        game_state["keys_collected"].append(item_found)
                        output += "Catarina says: Congrats!! I am here to help you. Here is your " + item_found[
                            "name"] + " Key to continue!"
                    elif item["name"] == "david":
                        item_found = object_relations[item["name"]].pop()
                        game_state["keys_collected"].append(item_found)
                        output += "David says: Hurry up! I've already started class!\nBut I see here that you have done it all so congrats and here is the " + \
                                  item_found["name"] + "!"  # FAZER
                    elif item["name"] == "fred":
                        output += "Fred says: Hi! I am Fred, your friendly TA! So happy you are here! Let's work!"
                    elif item["name"] == "dish_washer":
                        item_found = object_relations[item["name"]].pop()
                        game_state["keys_collected"].append(item_found)
                        output += "Good thing that you cleaned after yourself, now you can go to the " + item_found[
                            "name"] + "."
                    elif item["name"] == "eating_seats":
                        item_found = object_relations[item["name"]].pop()
                        game_state["keys_collected"].append(item_found)
                        output += "Here, have a " + item_found["name"] + ", relax and get ready for the class."
                    elif item["name"] == "toilet_f":
                        if user_data["user_gender"] == "F":
                            output += "You fell refreshed!"
                        elif user_data["user_gender"] == "M":
                            output += "You can't go in there, pervert!"
                    elif item["name"] == "toilet_m":
                        if user_data["user_gender"] == "M":
                            output += "You fell refreshed!"
                        elif user_data["user_gender"] == "F":
                            output += "You can't go there, pervert!"
                else:
                    output += "There isn't anything interesting about it."
            print(output)
            break

    if (output is None):
        print("The thing you requested is not found in the current room.")

    if (next_room and input("Do you want to go to the next room? Ener 'yes' or 'no'").strip() == 'yes'):
        play_room(next_room)
    else:
        play_room(current_room)


def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if (game_state["current_room"] == game_state["target_room"]):
        print("Congrats! You escaped IronHack, run while you can!")
    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 'explore' or 'examine'?").strip()
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            examine_item(input("What would you like to examine?").strip())
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'.")
            play_room(room)
        linebreak()


game_state = INIT_GAME_STATE.copy()
start_game()
play_again()