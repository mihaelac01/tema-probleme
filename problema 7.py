zi = ['Luni', 'Marti', 'Miercuri', 'Joi', 'Vineri', 'Sambata', 'Duminica']
venit = [117,133,596,247,839,194,162] 
print(' Venitul saptamanal:', sum(venit))
print(' Media venitului zilnic:', sum(venit)/7)
print(' Ziua cu cel mai mare venit:',zi[venit.index(max(venit))])
print(' Ziua cu cel mai mic venit:',zi[venit.index(min(venit))])