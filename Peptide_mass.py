
# coding: utf-8

# In[3]:

import re

AAmass = 'A 71.037114,R 156.101111,N 114.042927,D 115.026943,C 103.009185,E 129.042593,Q 128.058578,G 57.021464,H 137.058912,I 113.084064,L 113.084064,K 128.094963,M 131.040485,F 147.068414,P 97.052764,S 87.032028,T 101.047679,W 186.079313,Y 163.06332,V 99.068414,'

peptide = 'NIPKNFEDVGHSTDAR'

mass = 0

masslist = []

for aa in peptide:
    
    mass = mass + float(''.join(re.findall(aa + r'\s(\S*?)\,', AAmass)))
    
    masslist.append(mass)
    
print mass
print '\n'

print masslist[0]
print ''.join(re.findall('(\w)\s' + str(masslist[0]), AAmass)[0])



i = 1

while i < (len(masslist)):
    
    aamass = str(masslist[i]-masslist[i-1])
    print aamass
    print ''.join(re.findall('(\w)\s' + str(aamass), AAmass)[0])
    i = i + 1


# In[ ]:



