# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 17:17:41 2018
@author: martin412
"""

L=[[0,0,0,0 ],
   
   [0,0,0,0],
   
   [0,0,0,0],
   
   [0,0,0,0]]

print(L[0])
print(L[1])
print(L[2])
print(L[3])
print("Score:0")
while L[0] or L[1] or L[2] or L[3]<2048: 
    a=input("Kam?(up=u,down=d,right=r,left=l,stop)" )
    Score = 0
    if a == "d" :
        L[3][0]=L[0][0]+L[1][0]+L[2][0]+L[3][0]
        Score = Score + L[0][0]+L[1][0]+L[2][0]+L[3][0]
        L[0][0]=0
        L[1][0]=0
        L[2][0]=0
        L[3][1]=L[0][1]+L[1][1]+L[2][1]+L[3][1]
        Score = Score + L[0][1]+L[1][1]+L[2][1]+L[3][1]
        L[0][1]=0
        L[1][1]=0
        L[2][1]=0
        L[3][2]=L[0][2]+L[1][2]+L[2][2]+L[3][2]
        Score = Score + L[0][2]+L[1][2]+L[2][2]+L[3][2]
        L[0][2]=0
        L[1][2]=0
        L[2][2]=0
        L[3][3]=L[0][3]+L[1][3]+L[2][3]+L[3][3]
        Score = Score + L[0][3]+L[1][3]+L[2][3]+L[3][3]
        L[0][3]=0
        L[1][3]=0
        L[2][3]=0
        if L[1][0]==0:
            L[1][0]=2
        else:
            pass
        if L[2][3]==0:
            L[2][3]=2
        else:
            pass
    if a == "u" :
        L[0][0]=L[3][0]+L[1][0]+L[2][0]+L[0][0]
        Score = Score + L[3][0]+L[1][0]+L[2][0]+L[0][0]
        L[3][0]=0
        L[1][0]=0
        L[2][0]=0
        L[0][1]=L[3][1]+L[1][1]+L[2][1]+L[0][1]
        Score = Score + L[3][1]+L[1][1]+L[2][1]+L[0][1]
        L[3][1]=0
        L[1][1]=0
        L[2][1]=0
        L[0][2]=L[3][2]+L[1][2]+L[2][2]+L[0][2]
        Score = Score + L[3][2]+L[1][2]+L[2][2]+L[0][2]
        L[3][2]=0
        L[1][2]=0
        L[2][2]=0
        L[0][3]=L[3][3]+L[1][3]+L[2][3]+L[0][3]
        Score = Score + L[3][3]+L[1][3]+L[2][3]+L[0][3]
        L[3][3]=0
        L[1][3]=0
        L[2][3]=0
        if L[1][3]==0:
            L[1][3]=2
        else:
            pass
        if L[2][2]==0:
            L[2][2]=2
        else:
            pass
    if a == "l" :
        L[0][0]=L[0][0]+L[0][1]+L[0][2]+L[0][3]
        Score = Score + L[0][0]+L[0][1]+L[0][2]+L[0][3]
        L[0][1]=0
        L[0][2]=0
        L[0][3]=0
        L[1][0]=L[1][0]+L[1][1]+L[1][2]+L[1][3]
        Score = Score + L[1][0]+L[1][1]+L[1][2]+L[1][3]
        L[1][1]=0
        L[1][2]=0
        L[1][3]=0
        L[2][0]=L[2][0]+L[2][1]+L[2][2]+L[2][3]
        Score = Score + L[2][0]+L[2][1]+L[2][2]+L[2][3]
        L[2][1]=0
        L[2][2]=0
        L[2][3]=0
        L[3][0]=L[3][0]+L[3][1]+L[3][2]+L[3][3]
        Score = Score + L[3][0]+L[3][1]+L[3][2]+L[3][3]
        L[3][1]=0
        L[3][2]=0
        L[3][3]=0
        if L[1][1]==0:
            L[1][1]=2
        else:
            pass
        if L[2][0]==0:
            L[2][0]=2
        else:
            pass
    if a == "r" :
        L[0][3]=L[0][0]+L[0][1]+L[0][2]+L[0][3]
        Score = Score + L[0][0]+L[0][1]+L[0][2]+L[0][3]
        L[0][1]=0
        L[0][2]=0
        L[0][0]=0
        L[1][3]=L[1][0]+L[1][1]+L[1][2]+L[1][3]
        Score = Score + L[1][0]+L[1][1]+L[1][2]+L[1][3]
        L[1][1]=0
        L[1][2]=0
        L[1][0]=0
        L[2][3]=L[2][0]+L[2][1]+L[2][2]+L[2][3]
        Score = Score + L[2][0]+L[2][1]+L[2][2]+L[2][3]
        L[2][1]=0
        L[2][2]=0
        L[2][0]=0
        L[3][3]=L[3][0]+L[3][1]+L[3][2]+L[3][3]
        Score = Score + L[3][0]+L[3][1]+L[3][2]+L[3][3]
        L[3][1]=0
        L[3][2]=0
        L[3][0]=0
        if L[0][1]==0:
            L[0][1]=2
        else:
            pass
        if L[3][1]==0:
            L[3][1]=2
        else:
            pass
    if a == "stop":
        print("Konec")
        break
    else:
        print("Neplatný příkaz!")
        pass
    

    print(L[0])
    print(L[1])
    print(L[2])
    print(L[3])
    print("Score:",Score)