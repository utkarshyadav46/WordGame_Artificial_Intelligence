import enchant
import speech_recognition as sr
from tkinter import *
import random
import os
import tkinter as tk
from gtts import gTTS
from PyDictionary import PyDictionary
import datetime
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import warnings
warnings.filterwarnings("ignore")
language = 'en'
x="white"
dictionary=PyDictionary()
open_file = open('example.txt', 'r')
words_list =[]
contents = open_file.readlines()
for i in range(len(contents)):
    words_list.append(contents[i].strip('\n'))
open_file.close()

bot=ChatBot('BOT')
bot.set_trainer(ListTrainer)
def chat():
       root.destroy()
       r=sr.Recognizer()
       print('WELCOME TO CHATBOX')
       bot=ChatBot('BOT')
       bot.set_trainer(ListTrainer)
       dictionary=PyDictionary()
       while True:
           mic=sr.Microphone()
           with mic as source:
               print("Speak anything!!")
               audio=r.listen(source)
               try:
                   message=r.recognize_google(audio)
                   print("YOU: {}".format(message))
               except:
                   print("Sorry could not recognize what you said please write it here\n")
                   message =input('YOU:')
           m=message.lower()
           if m.strip() == 'meaning':
                   print('ChatBot: Meanin of What? ')
                   word=input('YOU :')
                   print('ChatBot:')
                   print(dictionary.meaning(word))
           elif m.strip() == 'translation' or m.strip() == 'translate':
                   print('ChatBot: translate of What? ')
                   word=input('YOU :')
                   che=input('Chatbot:Translate into:')
                   print('ChatBot:')
                   print (dictionary.translate(word,che))
           elif m.strip()=='time' or m.strip()=='date':
                   now = datetime.datetime.now()
                   print ("ChatBot:Current date and time using str method of datetime object:")
                   print (now.strftime("%Y-%m-%d %H:%M"))
           elif m.strip()=='hi' or m.strip()=='hello':
                   reply='hello buddy'
                   print('ChatBot:'+reply)
           elif m.strip() != 'Bye':
                   reply=bot.get_response(message)
                   print('ChatBot:',reply) 
           elif m.strip() == 'bye':
                   reply=bot.get_response(message)
                   print('ChatBot:',reply)
                   break
                
           
    
                    
def game():
    root.destroy()
    myobj = gTTS(text='\nWELCOME to WORD JUMBLE!!\n Unscramble the leters to make a word.', lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg321 welcome.mp3") 
    while(1):
        gwind=tk.Tk()
        gwind.title('WORD GAME ARTIFICIAL INTELLIGENCE')
        gwind.geometry('500x600')
        gwind.configure(bg=x)
        buttonquit = tk.Button(text="X", bg="red",fg="WHITE",command=quit).pack(side=TOP)
        labl=Label(text='\nWELCOME to WORD JUMBLE!!\n Unscramble the leters to make a word.\n(press the enter key at prompt to quit)',bg=x,fg="darkgreen",font=12).pack()
        word = random.choice(words_list)
        correct = word.lower()
        jumble = ""
        d = enchant.Dict("en_US")
        while word:
            position = random.randrange(len(word))
            jumble += word[position]
            word = word[:position] + word[(position + 1):]
        textstr=StringVar()
        def get():
            gwind.destroy()
        def check():
            guess=textstr.get()
            if guess.lower() in open('example.txt').read():
                lab12=Label(text='Woo hoo !!! Correct Answer\n\n\t',bg=x,fg="cyan",font=8).pack()
                myobj = gTTS(text='Correct Answer\n\n\t', lang=language, slow=False)
                myobj.save("welcome.mp3")
                os.system("mpg321 welcome.mp3")
                buttonquit = tk.Button(gwind,text="NEXT" ,fg="red",command=get).pack()
            elif d.check(guess):
                checkword=Label(text='\n\t\tThanks For Teaching us a New Word but ztry again to get score \t',fg="blue",font=9).pack()
                myobj = gTTS(text='\nThanks For Teaching us a New Word but try again to get score \t', lang=language, slow=False)
                myobj.save("welcome.mp3")
                os.system("mpg321 welcome.mp3")
                with open("example.txt", "a") as myfile:
                    myfile.write('\n'+guess.lower());
                    myfile.close();
            else:
                ch=tk.Tk()
                lab12=Label(ch,text='SORRY !!! WRONG ANSWER \t',fg="red",font=8).pack()
                myobj = gTTS(text='SORRY !!! WRONG ANSWER.DO YOU NEED HINT ?? \t', lang=language, slow=False)
                myobj.save("welcome.mp3")
                os.system("mpg321 welcome.mp3")
                def get1():
                    ch.destroy()
                def choice():
                    ch.destroy()
                    lab12=Label(text=d.suggest(jumble),fg='Brown',bg=x,font=5).pack()
                    myobj = gTTS(text='Here Are Some Hints', lang=language, slow=False)
                    myobj.save("welcome.mp3")
                    os.system("mpg321 welcome.mp3")
                option=Label(ch,text='\nDO YOU NEED HINT ?? \t\n\n\n',fg="brown",font=10).pack()
                button = tk.Button(ch,text="NO",width=25, fg="red",command=get1)
                button.pack(side=tk.LEFT)
                sugbutton = tk.Button(ch,width=25,text="YES",command=choice)
                sugbutton.pack(side=tk.LEFT)
        ques=Label(text="\n"+jumble.lower()+"\n\n",bg=x,fg="blue",font=20).pack()
        text=Entry(textvariable=textstr).pack()
        ques2=Label(text="\n",bg=x,fg="blue",font=20).pack()
        button1=Button(text='CHECK' ,fg="Black" ,command=check).pack()
        gwind.mainloop()   #Binding the root
root = tk.Tk()
frame =tk.Frame(root)
root.configure(bg=x)
frame.pack()
textstr=StringVar()
button = tk.Button(frame, text="X",bg="red", fg="WHITE",command=quit)
button.pack(side=tk.LEFT)
game_button = tk.Button(frame,text="WORD GAME",command=game)
game_button.pack(side=tk.LEFT)
chat_button = tk.Button(frame,text="CHAT BOX",command=chat)
chat_button.pack(side=tk.LEFT)
root.geometry('350x350')    
root.mainloop()
