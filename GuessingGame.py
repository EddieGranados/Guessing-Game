import random
import sys

Random = (random.randint(1,10))

def main():
    Answer = int(input("Guess the number!: ")) 
    if Answer == Random:
        print("Contragulations you won!")
    else:
        if Answer > Random:
            TooHigh()
        elif Answer < Random:
            TooLow()
        else:                
            print("Please enter a number!")

def TooHigh():
    print("Your guess is to high, please try again.")
    main()

def TooLow():
    print("Your guess is to low, please try again.")
    main()

if __name__ == "__main__":
    main()




        

        
        