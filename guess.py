import random  #imports the random library

guessesTaken = 0 #This is a variable that gives the number of guesses the player has taken

print('Hello! What is your name?')#Prints the statement onto the screen
myName = input() #The player inputs their name and the program puts it into this variable

number = random.randint(1,100) #Finds a random number between one and one hundred
print ('Well, ' + myName + ', I am thinking of a number between 1 and 100.') #Prints out the statement, with the name the player gave

while guessesTaken < 20: #this loops through the tabbed code while the player has taken fewer than 20 guesses
    print ('Take a guess.')#prints out the given statement
    guess = input() #The player input a guess which we set as the variable guess
    guess = int(guess) #input returns a string data type (think of that as an english word), but we need the guess to be a number, so change it's type to an int (short for integer, which is a whole positive or negative number or 0)

    guessesTaken = guessesTaken + 1 #The player has now taken one more guess, so we increment guessestaken by one

    if guess < number: #This is a condition statement that means if the guess is less than the number(this is the random number we picked earlier) then go into the tabbed code
        print ('Your guess is too low.') #we print that the user's guess is too high and now we go back to the top of the loop

    elif guess > number: #elif stands for else if, it means that this statment can only be true if the first statement was not, so the computer doesn't waste time doing something that will never happen
        print ('Your guess is too high.')

    else: #this case is only true when nothing else is, because of this we don't have to write anything but else
        break #This breaks us out of our while loop because in this case where the guess is neither less than or greater than the number, it must be equal to the number

if guess == number: #the case where the guess is equal to the number (== means equivalent to, while = means takes the value of [ex. x takes the value of 1(x=1), y takes the value of 1(y=1), x is equivalent to y(x==y)])
    guessesTaken = str(guessesTaken)#the variable guessestaken is currently an integer, but to print it out we have to change it into a string
    print ('Good job, ' + myName + '!  You guessed my number in ' + guessesTaken + ' guesses!') #print statement

if guess != number: #this is the case where we exited the while loop, but guess is not the correct number (meaning the user took more than 20 guesses)
    number = str(number)#we switch the correct number into a string
    print ('Nope.  The number I was thinking of was ' + number) #print statement
