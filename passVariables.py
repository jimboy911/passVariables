#Passing variables app
 
#main function handles everything
def main():
    #grabs name from user and stores it into yourName variable
    yourName = nameGet()
    yourNumber = "4" #trying out a second variable
 
    #then pass yourName and yourNumber variables into the printName() function
    printName(yourName, yourNumber)
 
#function to get name from user
def nameGet():
    yourName = input("What is your name? ") #asks user for input
    return yourName #returns the variable in the function
 
#function to print your name, taking yourName and yourNumber as variables 
def printName(yourName, yourNumber):
    print(f"Your name is {yourName}. Your number is {yourNumber}")
 
main() #runs the program
