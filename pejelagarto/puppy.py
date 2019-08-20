# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:26:02 2019

@author: JuanCarlos
"""

class Puppy:
    
    def __init__(self , a , b, k = 5):
        self.a = a
        self.b = b
        self.k = self._square(k)
    
    def _square(self, k):
        return k*k