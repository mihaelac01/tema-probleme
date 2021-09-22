ora=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
t=[2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,6,9,7,6,5]
print('Temperatura medie= ', round(sum(t)/24,1))
print('Maximul= ',max(t))
print('Minimul= ',min(t))
print('Ora la care s-a inregistrat temperatura maxima: ',ora[t.index(max(t))])
print('Ora la care s-a inregistrat temperatura minima: ',ora[t.index(min(t))])