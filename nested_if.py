# Task 1: Code Correction
# You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.

# Buggy Code:

# place = input("Choose a place: forest or cave? ")

# if place == "forest":
#     action = input("climb a tree or cross a river?")
#     if action == "climb a tree":
#         print("You found a bird's nest!")
#     elif action == "cross a river":
#         print("You found a boat!")
# elif place == "cave":
#     print("You find a hidden treasure!")

# Task 2: Setting the Scene
# Based on the corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.
# place = input("Choose a place: forest or cave? ")

# if place == "forest":
#     action = input("climb a tree or cross a river?")
#     if action == "climb a tree":
#         print("You found a bird's nest!")
#     elif action == "cross a river":
#         print("You found a boat!")
# elif place == "cave":
#     action = input("light a torch or proceed in the dark ")
#     if action == "light a torch" or action == "torch":
#         print("you were able to avoid the pitfall and found the treasure room")
#     elif action == "proceed in the dark" or action == "dark" or action == 'proceed in dark':
#         print("you fell into a pit")


# Task 3: Default Path
# If the user makes an invalid choice at any point, use the pass statement for now. Later, you can enhance this to provide feedback or a different branch of the story.
# place = input("Choose a place: forest or cave? ")

# if place == "forest":
#     action = input("climb a tree or cross a river?")
#     if action == "climb a tree":
#         print("You found a bird's nest!")
#     elif action == "cross a river":
#         print("You found a boat!")
#     else:
#         pass
# elif place == "cave":
#     action = input("light a torch or proceed in the dark ")
#     if action == "light a torch" or action == "torch":
#         print("you were able to avoid the pitfall and found the treasure room")
#     elif action == "proceed in the dark" or action == "dark" or action == 'proceed in dark':
#         print("you fell into a pit")
#     else:
#         pass
# else:
#     pass


# 2. Quick Decisions: The Event Planner 🎉
# Objective:
# To practice the use of shorthand if statements in determining event-related decisions.

# Task 1: Code Correction
# You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

# Buggy Code:

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if int(attendees) > 100 else "conference room"
# print(venue)

# Task 2: Venue Selection
# Based on the corrected code from Task 1, further enhance the program to recommend additional facilities like "audio system" or "projector" based on the number of attendees.

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if int(attendees) > 100 else "gymnasium" if int(attendees) > 50 else "conference room" if int(attendees) > 20 else "classroom"
# print(venue)

# # Task 3: Catering Choices
# # Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".
# food_selections = input("would you like vegetarian food ")
# veggieDelightCaterers = 'you should go to Veggie Delight Caterers' if food_selections == "yes" else 'you should go to Gourmet Meals Caterers'
# print(veggieDelightCaterers)

# 3. Silent Failures: The Error Handler 🐞
# Objective:
# To practice the use of the pass statement in handling potential errors silently.

# Task 1: Code Correction
# You are provided with a Python script that is supposed to handle errors silently, but it has some mistakes. Identify and fix them.

# Buggy Code:

# try:
#     x = 1 / 0
# except ZeroDivisionError:
#     pass

# Task 2: Division Calculator
# Based on the corrected code from Task 1, enhance the program to handle other potential errors, such as ValueError when trying to divide a number by a string.
# try:
#     x = 1 / 0
# except ZeroDivisionError:
#     pass
# except ValueError:
#     pass

# # Task 3: File Reader
# # Ask the user for a filename to read. Try to open and read the file. If the file doesn't exist, use the pass statement to handle the error silently.
# file_name = input("Type a filename to open and read\n")
# try:
#     with open(file_name) as file:
#         print(file.read())
# except FileNotFoundError:
#     pass

# 4 Nested Quick Decisions: The Shopping Assistant 🛍️
# Objective:
# To practice the use of nested shorthand if statements in assisting a shopping decision.

# Task 1: Code Correction
# You are provided with a Python script that is supposed to assist in shopping, but it has errors. Identify and fix them.

# Buggy Code:

# weather = input("Enter the weather: sunny, rainy, or cold: ")
# clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather =="rainy" else "sweater"
# print(clothing)

# Task 2: Clothing Recommendation
# Based on the corrected code from Task 1, further enhance the program to recommend additional items like "hat" or "boots" based on the weather.
# weather = input("Enter the weather: sunny, rainy, or cold\n")
# clothing = "sunglasses and a hat" if weather == "sunny" else "umbrella and rain boots" if weather == "rainy" else "sweater"
# print(clothing)

# Task 3: Accessory Recommendation
# Based on the clothing recommendation, suggest an accessory. For instance, if "sunglasses" were recommended, suggest "sunscreen" as an accessory.
# weather = input("Enter the weather: sunny, rainy, cold ")

# if ( weather == 'sunny'):
#     clothing = 'wear sunglasses and a hat'
#     print(clothing)
#     if ('sunglasses' in clothing):
#         print('you should also wear sunscreen :p')
# elif ( weather == 'rainy'):
#     clothing = 'take an umbrella and wear rain boots'
#     print(clothing)
#     if ('umbrella' in clothing):
#         print("don't forget a pancho if you have one!")
# else:
#     clothing = 'wear a jacket or sweater'
#     print(clothing)
#     if ('sweater' in clothing):
#         print('I would also take gloves it may be chilly out')

# 5. The Silent Logger: System Monitor 🖥️
# Objective:
# To practice the use of the pass statement in a system monitoring context.

# Task 1: Code Correction
# You are provided with a Python script that is supposed to monitor system parameters, but it has some mistakes. Identify and fix them.

# Buggy Code:

import random

# cpu_usage = random.randint(0, 100)
# if cpu_usage > 90:
#     print("High CPU usage!")
# elif cpu_usage > 80 and cpu_usage <= 90:
#     pass
        
# Task 2: System Check
# Based on the corrected code from Task 1, enhance the program to also monitor memory usage and disk space, and provide alerts accordingly.
# cpu_usage = random.randint(0,100)
# memory_usuage = random.randint(0,100)
# disk_space = random.randint(0,100)

# if cpu_usage > 90:
#     print("High CPU usage!")
# elif cpu_usage > 80 and cpu_usage <= 90:
#     pass
# if memory_usuage > 70:
#     print("high memory usage")
# else:
#     pass
# if disk_space > 80:
#     print("warning low storage space")
# else:
#     pass


# Task 3: Alert System
# If any of the system parameters exceed a certain threshold, print an alert message. However, if the system parameter is within a "gray zone", use the pass statement to silently log this without alerting the user.
cpu_usage = random.randint(0,100)
memory_usuage = random.randint(0,100)
disk_space = random.randint(0,100)

cpu_threshold_danger = 90
cpu_threshold = 80

disk_space_threshold_danger = 80
disk_space_threshold = 70

memory_usuage_threshold_danger = 70
memory_usuage_threshold = 60

if cpu_usage > cpu_threshold_danger:
    print(cpu_usage, "High CPU Usage!")
elif cpu_usage > cpu_threshold_danger:
    pass
if disk_space > disk_space_threshold_danger:
    print(disk_space, "Low storage!!")
elif disk_space > disk_space_threshold:
    pass
if memory_usuage > memory_usuage_threshold:
    print(memory_usuage, "high memory usage")
else:
    pass