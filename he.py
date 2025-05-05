#!/usr/env python
# Prompt user to enter his/her name.
print("What is your Name?")
Name = input()
# Prompt user to enter his/her age.
print("What is your age?")
Age = input()
# Print Greeting message.
print(f"Hello {Name.title()},you are {Age} years old.")
print("Hello " + Name.title() + ", you are " + Age + " years old.")

name = ""
while name == "":
    print("Enter your name:")
    name = input()

print(f"You are welcome {name}")

