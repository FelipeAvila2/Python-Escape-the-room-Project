# Python Escape the Room Project

Repository for the first Data Analytics Project - Python

This project consisted in creating a 'Escape-the-room' minigame.

### Brief Wiki Description:

An escape room, also known as an escape game, puzzle room or exit game, is a game in which a team of players discover clues, solve puzzles, and accomplish tasks in one or more rooms in order to accomplish a specific goal in a limited amount of time. The goal is often to escape from the site of the game. Most escape games are cooperative but competitive variants exist. Escape rooms became popular in North America, Europe and East Asia in the 2010s. Permanent escape rooms in fixed locations were first opened in Asia and followed later in Hungary, Serbia, Australia, New Zealand, Russia and South America.

![image](https://user-images.githubusercontent.com/83870535/129184843-4986bef7-dedd-48ea-97c9-608c729b2d87.png)


## Overview

The goal of this project was to apply the Python programming skills in solving a real problem.

## How to run the game

1. Either fork or download the repository into your computer.
2. Install all the requirements (none - for this project we used pure python or native libraries).
3. Open " Python-Escape-the-room-Project/your-code/final-version/ironhack-game.py " in a console.

## How to play the game

1. Run the " ironhack-game.py " in a console.
2. Insert your name and gender in the command line.
3. In each room you have two options: "explore" or "examine"
3.1. Explore: When you select explore you see all the object in the room
3.2. Examine: When you select examine you can interact with the objects
4. When you examine a character that has a key you can advance to the next room via a door.
5. The goal is to escape all rooms!

## Created content

Besided the general gaming mechanic some special features where created:

- play_again
  - after the game ends you get a option to play the game again

```python
def play_again():
    play = input("Do you want to do it again? 'yes' or 'no': ")
    if play == "yes":
        start_game()
```


- user
  - you get a unique user for every person that plays

```python
def user():
    user_data["name"] = input("Hi! Welcome to our little IronHack-game. Please, give us your name: ")
    user_data["user_gender"] = input(
        "We're sorry, but our bathrooms have a binary system, what is your gender? 'M or 'F: ")
    linebreak()
    print("Ok! Now lets start this journey!")
```


- user_object
  - this user is a object itself and has propertys like gender

```python
user_data = {
    "name": "",
    "user_gender": "",
}
```


## The map of the game

![image](https://user-images.githubusercontent.com/83870535/129184782-4b5f187d-8293-419b-bee3-ebabab39bf03.png)


