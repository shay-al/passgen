# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 11:53:32 2023

@author: shaya
"""
class Passgen():
   
    def __init__(self, length=8 , alpha_use_uppers=True , alpha_use_lowers=True , numeric_use_numbers=True):
        self.length = length
        self.alpha_use_uppers=alpha_use_uppers
        self.alpha_use_lowers=alpha_use_lowers
        self.numeric_use_numbers=numeric_use_numbers
        
        
        self.alpha=[ chr(i) for i in range(ord('a'),ord('z')+1)]
        self.numerix=[ str(i) for i in range(10)]
        self.alpha_numerix=[self.alpha,self.numerix]
        
            
    def gen(self):
        ret_str=''
        pick_end=1
        
        if not self.numeric_use_numbers: 
            pick_end=0
        use_alpha = self.alpha_use_uppers or self.alpha_use_lowers
        if not use_alpha and pick_end==0:
            return ''
        from random import randint as rnd
        act=[]
        if self.alpha_use_uppers:
            act.append(str.upper)
        if self.alpha_use_lowers:
            act.append(str.lower)
        
        #lanumerix [rnd(0,len(numerix)-1)]
                   
        for i in range (self.length):
            if not use_alpha and pick_end==1:
                #use only numbers
                arr=self.alpha_numerix[1]
                ch=str(arr [rnd(0,len(arr)-1)])
                ret_str+=ch
            else:
                arr=self.alpha_numerix[rnd(0,pick_end)]
                ch=str(arr [rnd(0,len(arr)-1)])
                if arr[0].isalpha():
                    ch=act[rnd(0,len(act)-1)](ch)
                ret_str+=ch
        return ret_str
    
            
        
    
    