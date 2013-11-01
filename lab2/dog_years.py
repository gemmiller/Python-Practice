# Simple interactive script figures out a person's age in dog years

name = raw_input("What's your name? ")
age = input("How old are you? ")
dog_years = age / 7
conclusion = "Well, " + name + ", in dog years you are only " + str(dog_years) + "!"
print conclusion
