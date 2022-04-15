import numpy as np 
n = input()
l_n = n.split(' ')
l_n = [ int( i) 
for i in l_n] 
print(  min(  l_n)) 
print(  max(  l_n)) 
print( np. average( l_n)) 
print( np. std( l_n)) 
print( np. var( l_n))
