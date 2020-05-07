import string
import random

from tkinter import *
from tkinter import scrolledtext
from tkinter import simpledialog
from tkinter import messagebox

from classes import player1 as player1
from classes import player2 as player2

def consonant1():
    global rnd
    global turn
    i = rnd - 1
    phrase = phrases[i]
    list_phrase = lphrases[i]
    dash_phrase = dphrases[i]
    
    chosen_wheel = random.choice(wheel)
    
    if chosen_wheel != 'BANKRUPT':
        ans = simpledialog.askstring("Consonant", f"Wheel lands on {chosen_wheel}. Player 1 Enter your guess:").upper()
        if ans in phrase:
            dex_list = [ind for ind in range(len(list_phrase)) if list_phrase[ind] == ans]
            for i in dex_list:
                dash_phrase[i] = ans
                sdash_phrase = "".join(dash_phrase)
            conv.insert(INSERT, f"{ans} is found!\n")
            p1.addcash(chosen_wheel * len(dex_list))
        else:
            conv.insert(INSERT, f"{ans} is not found!\n")
        unused_consonants.remove(ans)
    else:
        sdash_phrase = "".join(dash_phrase)
        p1.reset()
        conv.insert(INSERT, f"The wheel lands on {chosen_wheel}. Tough luck prize pool resets to 0.\n")
    
    uc = "".join(unused_consonants)       
    money1.delete('1.0', 'end')    
    money1.insert(INSERT, p1.getrcash())
    gphrase.config(text = sdash_phrase)
    remainc.delete('1.0', 'end')
    remainc.insert(INSERT, uc)
    
    turn += 1
    
    if turn % 2 == 0:
        trn.config(text = "Player 2's turn")
        

def consonant2():
    global rnd
    global turn
    i = rnd - 1
    phrase = phrases[i]
    list_phrase = lphrases[i]
    dash_phrase = dphrases[i]
    
    chosen_wheel = random.choice(wheel)
    
    if chosen_wheel != 'BANKRUPT':
        ans = simpledialog.askstring("Consonant", f"Wheel lands on {chosen_wheel}. Player 2 enter your guess:").upper()
        if ans in phrase:
            dex_list = [ind for ind in range(len(list_phrase)) if list_phrase[ind] == ans]
            for i in dex_list:
                dash_phrase[i] = ans
                sdash_phrase = "".join(dash_phrase)
            conv.insert(INSERT, f"{ans} is found!\n")
            p2.addcash(chosen_wheel * len(dex_list))
        else:
            conv.insert(INSERT, f"{ans} is not found!\n")
        unused_consonants.remove(ans)
    else:
        sdash_phrase = "".join(dash_phrase)
        p2.reset()
        conv.insert(INSERT, f"The wheel lands on {chosen_wheel}. Tough luck prize pool resets to 0.\n")
    
    uc = "".join(unused_consonants)
    money2.delete('1.0', 'end')    
    money2.insert(INSERT, p2.getrcash())
    gphrase.config(text = sdash_phrase)
    remainc.delete('1.0', 'end')
    remainc.insert(INSERT, uc)
    
    turn += 1
    
    if turn % 1 == 0:
        trn.config(text = "Player 1's turn")

def vowel1():
    global rnd
    global turn
    i = rnd - 1
    phrase = phrases[i]
    list_phrase = lphrases[i]
    dash_phrase = dphrases[i]
    
    if p1.getrcash() < 250:
        messagebox.showwarning("Warning", "You don't have enough money to buy a vowel.")
        sdash_phrase = "".join(dash_phrase)
    else:
        vowel = simpledialog.askstring("Vowels", "Player 1 Enter your vowel:").upper()
        if vowel in phrase:
            dex_list = [ind for ind in range(len(list_phrase)) if list_phrase[ind] == vowel]
            for i in dex_list:
                dash_phrase[i] = vowel
                sdash_phrase = "".join(dash_phrase)
            messagebox.showinfo("Info", f"All {vowel}'s shown")  
        else:
            messagebox.showinfo("Info", f"All {vowel}'s shown")
        unused_vowels.remove(vowel)
        p1.subcash(250)
    
    uv = "".join(unused_vowels)
    money1.delete('1.0', 'end')    
    money1.insert(INSERT, p1.getrcash())
    gphrase.config(text = sdash_phrase)
    remainv.delete('1.0', 'end')
    remainv.insert(INSERT, uv)
    
    turn += 1
    
    if turn % 2 == 0:
        trn.config(text = "Player 1's turn")
        
def vowel2():
    global rnd
    global turn
    i = rnd - 1
    phrase = phrases[i]
    list_phrase = lphrases[i]
    dash_phrase = dphrases[i]
    
    if p2.getrcash() < 250:
        messagebox.showwarning("Warning", "You don't have enough money to buy a vowel.")
        sdash_phrase = "".join(dash_phrase)
    else:
        vowel = simpledialog.askstring("Vowels", "Player 2 Enter your vowel:").upper()
        if vowel in phrase:
            dex_list = [ind for ind in range(len(list_phrase)) if list_phrase[ind] == vowel]
            for i in dex_list:
                dash_phrase[i] = vowel
                sdash_phrase = "".join(dash_phrase)
            messagebox.showinfo("Info", f"All {vowel}'s shown")  
        else:
            messagebox.showinfo("Info", f"All {vowel}'s shown")
        unused_vowels.remove(vowel)
        p2.subcash(250)
        
    uv = "".join(unused_vowels)   
    money2.delete('1.0', 'end')    
    money2.insert(INSERT, p2.getrcash())
    gphrase.config(text = sdash_phrase)
    remainv.delete('1.0', 'end')
    remainv.insert(INSERT, uv)
    
    turn += 1
    
    if turn % 2 == 0:
        trn.config(text = "Player 1's turn")

def guess1():
    global rnd
    i = rnd - 1
    phrase = phrases[i]
    list_phrase = lphrases[i]
    dash_phrase = dphrases[i]
    sdash_phrase = sphrases[i]
    
    
    guess = simpledialog.askstring("Guess", "Player 1 Enter your guess:").upper()
    if guess == phrase:
        sdash_phrase = guess
        conv.insert(INSERT, f"CONGRATS {p1.getname()} GUESSED IT!\n")
    else:
        conv.insert(INSERT, "Nope, wrong...\n")
        
    gphrase.config(text = sdash_phrase)
        
def guess2():
    global rnd
    i = rnd - 1
    phrase = phrases[i]
    list_phrase = lphrases[i]
    dash_phrase = dphrases[i]
    sdash_phrase = sphrases[i]
    
    guess = simpledialog.askstring("Guess", "Player 2 Enter your guess:").upper()
    if guess == phrase:
        sdash_phrase = guess
        conv.insert(INSERT, f"CONGRATS {p2.getname()} GUESSED IT!\n")
    else:
        conv.insert(INSERT, "Nope, wrong...\n")
        
    gphrase.config(text = sdash_phrase)

def finish():
    global rnd 
    global gphrase
    global rv
    global rc
    global turn
    
    i = rnd - 1
    dash_phrase = dphrases[i]
    sdash_phrase = sphrases[i]
    
    unused_vowels = rv
    unused_consonants = rc
    
    remainv.delete("1.0", "end")
    remainv.insert(INSERT, unused_vowels )
    remainc.delete("1.0", "end")
    remainc.insert(INSERT, unused_consonants )
    
    
    conv.delete('1.0', 'end')
    money1.delete('1.0', 'end')
    money2.delete('1.0', 'end')
    
    p1.total(p1.getrcash())
    p2.total(p2.getrcash())
    p1.reset()
    p2.reset()
    
    rnd += 1
    
    if rnd == 4:
        fin.config(state = 'disable')
        
    
    r.delete('1.0', 'end')
    r.insert(INSERT, f"Round {rnd}" )
    
    tot1.config(text = f'P1 total: {p1.gettotal()}')
    tot2.config(text = f'P2 total: {p2.gettotal()}')
    
    if rnd < 4:
        gphrase.config(text = sphrases[rnd - 1])
    else:
        gphrase.config(text = "")
        r.delete('1.0', 'end')

    trn.config(text = "Player 1's turn")

def convertd(a):
    
    dash_phrase = []
    for letter in a:
        if letter in alphabet:
            dash_phrase.append("-")
        else:
            dash_phrase.append(letter)
    return dash_phrase    

def converts(a):
    
    sdash_phrase = "".join(a)
    return sdash_phrase

#############################################################################################################################

name1 = input("Player 1: ")
name2 = input("Player 2: ")

p1 = player1(name1)
p2 = player2(name2)
rnd = 1
turn = 1
refvowels = ['A', 'E', 'I', 'O', 'U']
refconsonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'] 
rc = "".join(refconsonants)
rv = "".join(refvowels)
unused_vowels = ['A', 'E', 'I', 'O', 'U']
unused_consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'] 
uc = "".join(unused_consonants)
uv = "".join(unused_vowels)
wheel = ['BANKRUPT', 500, 550, 600, 650, 700, 750, 800, 850, 2500]

window = Tk()
window.title('Wheel of Fortune')
window.geometry('620x500')
window.configure(background = "#03fcca")

lbl = Label(window, text = f'WELCOME {p1.getname()} AND {p2.getname()} !')
lbl.grid(row = 0, column = 2) 

trn = Label(window, text = "Player 1's turn")
trn.grid(row = 0, column = 3)

r = Text(window, width = 7, height = 1)
r.insert(INSERT, "Round 1" )
r.grid(row = 1, column = 2)

#############################################################################################################################

alphabet = list(string.ascii_uppercase)
phrase1 = input("Please enter 1st string for the players to guess: ").upper()
phrase2 = input("Please enter 2nd string for the players to guess: ").upper()
phrase3 = input("Please enter 3rd string for the players to guess: ").upper()
lphrases = [list(phrase1), list(phrase2), list(phrase3)]
phrases = [phrase1, phrase2, phrase3]
dphrases = []
sphrases = []

for a in phrases:
    dphrases.append(convertd(a))
    
for a in dphrases:
    sphrases.append(converts(a))

############################################################################################################################
    
gphrase = Label(window, text = sphrases[rnd - 1])
gphrase.grid(row = 2, column = 2)

remainc = Text(window, width = len(uc), height = 1)
remainc.insert(INSERT, uc)
remainc.grid(row = 5, column = 2)
remainv = Text(window, width = len(uv), height = 1)
remainv.insert(INSERT, uv)
remainv.grid(row = 6, column = 2)

txt1 = Text(window, width = 15, height = 1)
txt1.insert(INSERT, p1.getname())
txt1.grid(row = 7, column = 0)

money1 = Text(window, width = 6, height = 1)
money1.grid(row = 7, column = 1)

txt2 = Text(window, width = 15, height = 1)
txt2.insert(INSERT, p2.getname())
txt2.grid(row = 7, column = 3)

money2 = Text(window, width = 6, height = 1)
money2.grid(row = 7, column = 4)

v = StringVar()
r1 = Radiobutton(window, text = 'Guess a consonant', variable = v, value = 'op1', command = consonant1)
r1.grid(row = 8, column = 0)
r2 = Radiobutton(window, text = 'Buy a vowel', variable = v, value = 'op2', command = vowel1)
r2.grid(row = 9, column = 0)
r3 = Radiobutton(window, text = 'Guess the phrase', variable = v, value = 'op3', command = guess1)
r3.grid(row = 10, column = 0)
v.set('op4')

v2 = StringVar()
r12 = Radiobutton(window, text = 'Guess a consonant', variable = v2, value = 'op1', command = consonant2)
r12.grid(row = 8, column = 3)
r22 = Radiobutton(window, text = 'Buy a vowel', variable = v2, value = 'op2', command = vowel2)
r22.grid(row = 9, column = 3)
r32 = Radiobutton(window, text = 'Guess the phrase', variable = v2, value = 'op3', command = guess2)
r32.grid(row = 10, column = 3)
v2.set('op4')
    
conv = scrolledtext.ScrolledText(window, width = 30, height = 10)
conv.grid(row = 11, column = 2)

fin = Button(window, text = "FINISH", command = finish)
fin.grid(row = 12, column = 2)

tot1 = Label(window, text = f'P1 total: {p1.gettotal()}')
tot1.grid(row = 15, column = 0)
tot2 = Label(window, text = f'P2 total: {p2.gettotal()}') 
tot2.grid(row = 15, column = 3)

#render and display UI
window.mainloop()

#############################################################################################################################

