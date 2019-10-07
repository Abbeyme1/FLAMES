# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 21:24:47 2019

@author: Abhay
"""

import string

def same(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i]==l2[j]:
                c=l1[i]
                l1.remove(c)
                l2.remove(c)
                l=l1+['*']+l2
                return [l,True]
    l=l1+['*']+l2
    return [l,False]


p1=input("enter player1 name")
p2=input("enter player2 name")

p1.lower()
p2.lower()

p1.replace(" ","")
p2.replace(" ","")

l1=list(p1)
l2=list(p2)

p=True

while p:
    ret_list=same(l1,l2)
    con_list=ret_list[0]
    p=ret_list[1]
    index=con_list.index('*')
    l1=con_list[:index]
    l2=con_list[index+1:]
    
count=len(l1)+len(l2)
result=['Friends','Lovers','Affectionate','Marriage','Enemies','siblings']

while len(result)>1:
    sp_index=(count%len(result))-1
    if sp_index>=0:
        right=result[sp_index+1:]
        left=result[:sp_index]
        result=right+left
    else:
        result=result[:len(result)-1]

print(result[0])
        