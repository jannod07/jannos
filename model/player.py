#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 19:15:55 2023

@author: estelle
"""

class Player:
    
   def __init__(self, pseudo,health,attack):
       self.pseudo = pseudo
       self.health = health
       self.attack = attack
       print("bienvenu au joueur", pseudo ," / nombre de vie:", health, "/ nombre attack:",attack)
       
   def get_pseudo(self):
       return self.pseudo
   
   def get_health(self):
       return self.health
   
   def get_attack(self):
       return self.attack
   
   def damage(self, damage):
        self.health -= damage
        print("Aie!!! vous venez de subir", damage, "degats")
        
   def attack_player(self, target_player) :
       
       target_player.damage(self.attack)