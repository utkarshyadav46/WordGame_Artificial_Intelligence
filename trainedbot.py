from tkinter import *    #Adding the graphics libraries from Tkinter
import os   
import PIL  #Adding the PIL library in the program for editing the images
import tkinter.messagebox
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from gtts import gTTS
bot=ChatBot('BOT')
bot.set_trainer(ListTrainer)
while True:
    message =input('YOU:')
    if message.strip() != 'Bye':
        reply=bot.get_response(message)
        print('ChatBot:',reply) 
    elif message.strip() == 'Bye':
        print('ChatBot: Bye Bye')
        break
