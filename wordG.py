#pip install pyenchant
import enchant
from tkinter import *
import random

#def show_entry_fields():
  #print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
# Program to show various ways to read an
print(
"""
      Welcome to WORD JUMBLE!!!

      Unscramble the leters to make a word.
      (press the enter key at prompt to quit)
      """
      )
open_file = open('example.txt', 'r')
words_list =[]
contents = open_file.readlines()
for i in range(len(contents)):
    words_list.append(contents[i].strip('\n'))
open_file.close()  
#WORDS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")
while(1):
    word = random.choice(words_list)
    correct = word
    jumble = ""
    d = enchant.Dict("en_US")
    score=0;
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
    print("The jumble is:", jumble)
    guess = input("Your guess: ")
    if guess in open('example.txt').read():
        score=score+1
        print("Woo hoo !!! Correct Answer\n\n\tYOUR SCORE IS\t",score)
    else:
        while guess != correct and guess != "":
            if d.check(guess):
                print("Thank you For Teach Me A new Word\n");
                with open("example.txt", "a") as myfile:
                    myfile.write(guess);
                    myfile.close();
            else:
                print("Sorry Wrong Answer\nWant Hint (Y or N)");
                ch=input();
                if ch=='Y' or ch=='y':
                    print(d.suggest(guess));
            guess = input("Your guess: ")
print("Thanks for playing")
