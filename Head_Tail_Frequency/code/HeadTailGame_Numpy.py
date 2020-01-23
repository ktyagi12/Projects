'''
GAME: HEAD TAIL FREQUENCY 
A coin is tossed 100 times.
Random value of Head or Tail can come.
Create the dictionary for the same and count
{'H':valueH,'T': valueT}
Count how many times heads and tails comes,
Plot frequency graph (histogram)


USE: random library: choice function
'''

import random as rd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#game_list = []
#g1 = np.zeros(shape = (1,100),dtype = int)
g1 = np.zeros(100,dtype = int)
print g1

for i in range(0,100):
	ch = rd.randint(0,1)
	if ch == 0:
		g1[i] = 1
	else:
		g1[i] = 0

print 'Game List: ', g1
#plt.hist(game_list,histtype = 'bar', rwidth = 0.75)
plt.hist(g1,histtype = 'bar', rwidth = 0.75)
plt.show()