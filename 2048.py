# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 17:17:41 2018

@author: martin412
"""
import random
L=[[2,0,0,2 ],
   
   [2,2,0,2],
   
   [0,2,2,0],
   
   [0,0,2,0]]

print(L[0])
print(L[1])
print(L[2])
print(L[3])

while L[0][0] or L[0][1] or L[0][2] or L[0][3] or L[1][0] or L[1][1] or L[1][2] or L[1][3] or L[2][0] or L[2][1] or L[2][2] or L[2][3] or L[3][0] or L[3][1] or L[3][2] or L[3][3] <2048: 
    a=input("Kam?(up,down,right,left,stop)" )
    if a == "down" :
        L[3][0]=L[0][0]+L[1][0]+L[2][0]+L[3][0]
        L[0][0]=0
        L[1][0]=0
        L[2][0]=0
        L[3][1]=L[0][1]+L[1][1]+L[2][1]+L[3][1]
        L[0][1]=0
        L[1][1]=0
        L[2][1]=0
        L[3][2]=L[0][2]+L[1][2]+L[2][2]+L[3][2]
        L[0][2]=0
        L[1][2]=0
        L[2][2]=0
        L[3][3]=L[0][3]+L[1][3]+L[2][3]+L[3][3]
        L[0][3]=0
        L[1][3]=0
        L[2][3]=0
    if a == "up" :
        L[0][0]=L[3][0]+L[1][0]+L[2][0]+L[0][0]
        L[3][0]=0
        L[1][0]=0
        L[2][0]=0
        L[0][1]=L[3][1]+L[1][1]+L[2][1]+L[0][1]
        L[3][1]=0
        L[1][1]=0
        L[2][1]=0
        L[0][2]=L[3][2]+L[1][2]+L[2][2]+L[0][2]
        L[3][2]=0
        L[1][2]=0
        L[2][2]=0
        L[0][3]=L[3][3]+L[1][3]+L[2][3]+L[0][3]
        L[3][3]=0
        L[1][3]=0
        L[2][3]=0
    if a == "left" :
        L[0][0]=L[0][0]+L[0][1]+L[0][2]+L[0][3]
        L[0][1]=0
        L[0][2]=0
        L[0][3]=0
        L[1][0]=L[1][0]+L[1][1]+L[1][2]+L[1][3]
        L[1][1]=0
        L[1][2]=0
        L[1][3]=0
        L[2][0]=L[2][0]+L[2][1]+L[2][2]+L[2][3]
        L[2][1]=0
        L[2][2]=0
        L[2][3]=0
        L[3][0]=L[3][0]+L[3][1]+L[3][2]+L[3][3]
        L[3][1]=0
        L[3][2]=0
        L[3][3]=0
    if a == "right" :
        L[0][3]=L[0][0]+L[0][1]+L[0][2]+L[0][3]
        L[0][1]=0
        L[0][2]=0
        L[0][0]=0
        L[1][3]=L[1][0]+L[1][1]+L[1][2]+L[1][3]
        L[1][1]=0
        L[1][2]=0
        L[1][0]=0
        L[2][3]=L[2][0]+L[2][1]+L[2][2]+L[2][3]
        L[2][1]=0
        L[2][2]=0
        L[2][0]=0
        L[3][3]=L[3][0]+L[3][1]+L[3][2]+L[3][3]
        L[3][1]=0
        L[3][2]=0
        L[3][0]=0
    if a == "stop":
        print("Konec")
        break
    
    print(L[0])
    print(L[1])
    print(L[2])
    print(L[3])
    
    