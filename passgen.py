# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:34:11 2023

@author: shaya
"""

def passgen( length=8, lowers=True , uppers = True, must_include_digits=True):
    import random
    from utils import md5Hash as md5
    def test_lower(x):
        try: 
            return x.islower() 
        except AttributeError: 
            return False
    def test_upper(x):
        try: 
            return x.isupper() 
        except AttributeError: 
            return False
    def test_digits(x):
        try:
            str(x)
        except:
            return False
        try: 
            return x.isdigit() 
        except AttributeError: 
            return False
    while True:
        raw =  md5(str(random.randint(1,1000000)), length)
    
        list_raw = list(raw)
        
        l_arr = list(map(test_lower,list_raw))
        l_any_score = any(l_arr)
        u_arr = list(map(test_upper,list_raw))
        u_any_score = any(u_arr)
        d_arr = list(map(test_digits,list_raw))
        d_any_score = any(d_arr)
        
        if lowers and uppers and must_include_digits:
            if l_any_score and u_any_score and d_any_score:
                return raw
        
        if lowers:
            if not l_any_score:
                if u_any_score:
                    if uppers:
                        if u_arr.count(True)>1:
                            raw[u_any_score.index[True]]=raw[u_any_score.index[True]].lower()
                            u_arr = list(map(test_upper,list_raw))
                            u_any_score = any(u_arr)
                        else
        else:
            if l_any_score:
                for i in range(len(l_arr)):
                    if l_arr[i]:
                        raw[i]=raw[i].upper()
        
        
                    
                        
        
                        
                
        
             any(list(map(test_lower,raw[:]))):
            print(f'{raw} has no lowers')
            continue
        if uppers and not any(list(map(test_upper,raw[:]))):
            if raw[:].count()
            print(f'{raw} has no uppers')
            continue
        if must_include_digits and not any(list(map(test_digits,raw[:]))):
            print(f'{raw} has no digits')
            continue
        return raw
        
 

    
    