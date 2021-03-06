# ThyPython
'''Suppose, there’s a sentence or word you don’t know the meaning of or don’t know how to pronounce it and you are too lazy to open a new tab in your browser for knowing the meaning of it,
Just copy the word to clipboard and press ‘/’ on keyboard and the program will give the translation in Hindi or any given language.
Or, if you want to know the pronunciation of the word, just press ‘`’ on the keyboard and it will speak it out.'''

import pyttsx3
from tkinter import Tk
import keyboard
from translate import Translator
from plyer import notification
print("The program has been initiated!")
t = Translator(to_lang = 'hindi')
e = pyttsx3.init()
e.setProperty('rate',120)
e.setProperty('volume',1)
def speak_it_out():
    x = Tk().clipboard_get()
    e.say(x)
    e.runAndWait()
def translate_it():
    x = Tk().clipboard_get()
    print("Copied word : ",x)
    translation = t.translate(x)
    notification.notify(
        title = x,
        message = translation
        )
while True:
    try:
        if keyboard.is_pressed('`'):  
            speak_it_out()
            pass;
        if keyboard.is_pressed('/'):
            translate_it()
            pass;
    except:
        print("Error")
        notification.notify(
            title = "Error",
            message = "Something went wrong!")
