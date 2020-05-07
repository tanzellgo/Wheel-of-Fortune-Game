import string
import random
from tkinter import *
from tkinter import scrolledtext
from tkinter import simpledialog
from tkinter import messagebox

class player1:
    def __init__(self, name):
        self.__name = name
        self.__roundcash = 0
        self.__totalcash = 0 

    def addcash(self, amnt):
        self.__roundcash += amnt
        
    def subcash(self, amnt):
        self.__roundcash -= amnt
        
    def total(self, amnt):
        self.__totalcash += amnt
        
    def getname(self):
        return self.__name
    
    def gettotal(self):
        return self.__totalcash
    
    def getrcash(self):
        return self.__roundcash
        
    def reset(self):
        self.__roundcash = 0
        
class player2:
    def __init__(self, name):
        self.__name = name       
        self.__roundcash = 0
        self.__totalcash = 0

    def addcash(self, amnt):
        self.__roundcash += amnt
        
    def subcash(self, amnt):
        self.__roundcash -= amnt
        
    def total(self, amnt):
        self.__totalcash += amnt
        
    def getname(self):
        return self.__name
    
    def gettotal(self):
        return self.__totalcash
    
    def getrcash(self):
        return self.__roundcash
        
    def reset(self):
        self.__roundcash = 0

