#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 17:27:22 2023

@author: estelle
"""

# programmation oriente bjet


from player import Player
        
       
    
player1 = Player("jannos", 20,3)
player2 = Player( "job", 20,5)

player1.attack_player(player2)

print("le joueur ", player1.get_pseudo(), "attaque le joueur", player2.get_pseudo())
print("bienvenu au joueur", player1.get_pseudo() ," / nombre de vie:", player1.get_health(), "/ nombre attack:",player1.get_attack())
print("bienvenu au joueur", player2.get_pseudo() ," / nombre de vie:", player2.get_health(), "/ nombre attack:",player2.get_attack())
     



#player1.attack_player(player2)
#player1.damage(2)
#print(" vous possedez deqormain", player1.get_health (), "de vie")
#print("joueur:", player1.get_pseudo())
