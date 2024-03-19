import random 

nice_things = ["You are doing great!", "You are an inspiration to others!", "Keep up the good work!"]

def say_something_nice():
    return random.choice(nice_things)

print(say_something_nice())
