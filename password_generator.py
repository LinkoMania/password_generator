# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 15:39:26 2022

@author: Colmanos - LinkoLabs
Generator of password
Step 1 : Create the choixe of password
Step 3 : generate the password
Step 4 : Print the password
Step 5 : Create the boucle while for restart the menu or exit
"""
from random import shuffle
global caracter_tab, character_maj,numerique_tab,special_char, choice_menu, x
    
caracter_tab = ["a","b","c","d","e","f",
                      "g","h","i","j","k","l",
                      "m","n","o","p","q","u",
                      "r","s","t","u","v","w",
                      "x","y","z"]

character_maj = ["A","B","C","D","E","F",
                      "G","H","I","J","K","L",
                      "M","N","O","P","Q","U",
                      "R","S","T","U","V","W",
                      "X","Y","Z"]
      
numerique_tab = [1,2,3,4,5,6,7,8,9,0]


special_char = ["|","@","#","{","[","^",
                    "!",")","-",":", "/","?",
                    ".","+","="]



def title_and_choice():
    global choice_menu
    print("------------------------------------------------")
    print("         Generator of password                  ")
    print("------------------------------------------------")
    print("     Select the choice for generated password   ")
    print("1 : Numerique Password. exemple :123456")
    print("2 : easy password. exemple :Ap1YhfF0 ")
    print("3 : Strong Password. exemple : 1|p@Hd7")
    print("4 : exit the programme")
    choice_menu = int(input("       Enter the number of index in your choice : "))
  
      
def passwordgenerator(choice_menu) :   
    global x
    shuffle(numerique_tab)
    shuffle(special_char)
    shuffle(character_maj)
    shuffle(caracter_tab)
    x = choice_menu
   # while True:
    if choice_menu == 1 :
            
          # print(caracter_tab)
          # print(numerique_tab[0:9]).split(",")
          # print("Votre mot de passe est : {}").format(numerique_tab[1])
            print("\n\n\n")
            print("\n       Votre mot de passe est : {}{}{}{}{}{}{}{}{}".format(numerique_tab[0],numerique_tab[1],numerique_tab[2],numerique_tab[3],numerique_tab[4],numerique_tab[5],numerique_tab[6],numerique_tab[7],numerique_tab[8]))
            print("\n\n\n")
            
    elif choice_menu == 2 :
            
            #print("Votre mot de passe est : {}").format(aleatoire_2)
            print("\n\n\n")
            print("\n           Votre mot de passe est : {}{}{}{}{}{}{}{}{}".format(caracter_tab[0],character_maj[1],numerique_tab[2],caracter_tab[3],character_maj[4],caracter_tab[5],numerique_tab[6],character_maj[7],numerique_tab[8]))
            print("\n\n\n")
                    
    elif choice_menu == 3 :
            print("\n\n\n")
            print("\n           Votre mot de passe est : {}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(caracter_tab[0],special_char[1],numerique_tab[2],special_char[3],numerique_tab[4],character_maj[5],special_char[6],numerique_tab[7],special_char[8],character_maj[0],caracter_tab[1],special_char[2],numerique_tab[3],caracter_tab[4],special_char[5],character_maj[6],numerique_tab[7],special_char[8]))
            print("\n\n\n")
    elif choice_menu == 4 :
            print("exit the programme")
            quit()
            False
            
            
    elif choice_menu > 4 or choice_menu != 2 or choice_menu != 1 or choice_menu != 3:
            print("Enter a number 1, 2 or 3 please")
            

while True:
    title_and_choice()
    if choice_menu <= 5:
        
        passwordgenerator(choice_menu)
        True
    else:
        False   
        break