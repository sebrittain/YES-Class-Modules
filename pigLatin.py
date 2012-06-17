vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y'] #list of all capital and lowercase vowels

def pig_latin(string): #this defines a function with the name pig_latin
    newstring = '' #we initialize an empty string with the name new_string
    s = string.split(' ') #we split our input string by spaces, so that each word is seperated
    for word in s: #this loops through every word in our string
        if word[0] in vowels: #this access the first element of the word (in this case the first letter) and checks if it is a vowel
            newstring = newstring + word + 'ay' + ' '#this takes our word adds 'ay' to the end and puts it into a new string
        else: #if the first letter is not a vowel
            newword = '' #This is an empty string we initialize to hold our new word
            w = list(word) #we switch our current word into a list so that we can perform more operations on it
            w.remove(word[0]) #we remove the first letter off the list
            for letter in w: #now we have to put the word back together
                newword = newword + letter #this individually puts the letters back into a string because a string can be changed into a list, but a list cannot be changed into a string
            newstring = newstring + newword + word[0] + 'ay' + ' ' #now we put our new word onto our string plus the first letter of the word(the letter we cut off earlier) and add 'ay' to the end
    return newstring #returns our pig latin string, which will put it on the screen when run


#to run this program type in something of the format pig_latin('name') or
#pig_latin('Brad Pitt') or pig_latin('she sells seashells down by the sea shore')


#there is a better implimentation
#in the else statment you shouldn't take the the first letter, but all the letters before the
#first vowel to deal with cases where the first letters are 'sh', 'th', 'st', etc.
