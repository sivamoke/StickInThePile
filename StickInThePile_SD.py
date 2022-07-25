#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 10:10:23 2022
Stick in the pile
@author: sivamokedissook
"""
import random

def AiPlay(remainStick):
    if remainStick >= 2:
        return random.randrange(1,2)
    else:
        return 1
    

name=input("what is your name?")
nstick=int(input("how many stick in the pile?"))

print("There are ", nstick ,"sticks in the pile")

loop_count = 0
while nstick > 0 :
  tstick = int(input(name + ", how many sticks you will take(1 or 2)"))
  if tstick < 1:
    print("No you cannot take less than 1 stick")
    continue
  elif tstick >2:
    print("No you cannot take more than 2 stick")
    continue
  elif nstick < tstick:
    print("There are not enough sticks to take.")
    continue
  else:
    nstick = nstick - tstick
    loop_count += 1
    if nstick == 0:
      print("YOU LOSE")  
      break
    aiStick = AiPlay(nstick)
    print("Ai is taking", aiStick, "from the pile")
    nstick = nstick - aiStick
    if nstick == 0:
      print("YOU WIN")  
      break
    print("there are", nstick, "sticks in the pile.")
    continue

print("OK. There is no stick left in the pile. You spent", loop_count, "times")
