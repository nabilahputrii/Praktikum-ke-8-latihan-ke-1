# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 13:05:21 2021

@judul : Praktikum ke-8 latihan ke-1
@NIM : 065002100002
@author: Nabilah Putri


"""

def cekbilangan(number):
    if number == 1:
        print(f"angka {number} merupakan bilangan prima")
    
    elif number == 2:
        print(f"angka {number} merupakan bilangan prima")
        
    else:
       
        global x 
        
        for x in range(2, number):
            
            if number % x == 0:
                
                stat = 0 
                
                break
            
            else:
                stat = 1 
        cekstat(stat)
        
def cekstat(stat):
    
    if stat == 0:
        print(f"angka {number} bukan merupakan bilangan prima")
        print(f"{x} kali {number//x} = {number}")
    
    else:
        print(f"{number} merupakan bilangan prima")

a = 1

while a == 1:
   
    number = int(input("silahkan anda masukan angka : "))
    cekbilangan(number)  
    break     
    
    
number = int(input("silahkan anda masukan angka : "))
cekbilangan(number)