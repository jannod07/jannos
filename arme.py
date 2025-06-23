#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Jul 19 02:15:00 2023

@author: estelle
"""

class weapen:
    
    def __init__(self,name_arm,damage):
        self.name_arm = name_arm
        self.damage = damage
        
    def get_name_arm(self):
        return self.name_arm
    
    def get_damage(self):
        return self.damage