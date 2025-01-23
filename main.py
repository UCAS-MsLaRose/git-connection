# Ms. LaRose and Vienna, git connection 
import random

def number():
    return random.randint(1,100)

def hello(name):
    print(f"Hello {name}! Welcome to our program.")



def main():
    hello("Vienna")
    print(number())

main()

