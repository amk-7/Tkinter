
def estPremier(n):
	#n = int(input("n: "))
	nbDiviseur = 0
	for div in range(1,50):
		if n%div==0:
			#print(n, "--------------", div)
			nbDiviseur += 1
			
	if nbDiviseur == 2:
		return True
	return False

# générateur des 10 premier nombre premier

def nombresPremier():
	compteur = 0
	nombre = 2
	listNbPremier = []
	while compteur <= 5 :
		if estPremier(nombre):
			#print(nombre)
			listNbPremier.append(nombre)
			compteur += 1
		nombre += 1
		
	#print(listNbPremier)
	return listNbPremier
	
# decomposition 

def decomposerNombre(n):

	facteursPremier = []
	nombresPremiers = nombresPremier()
	
	for i in range(len(nombresPremiers)):
		while n%nombresPremiers[i] == 0 :
			#print(n, "--------------", nombresPremiers[i])
			facteursPremier.append(nombresPremiers[i])
			n = n//nombresPremiers[i]
		i += 1
	if n != 1:
		facteursPremier.append(n)
		#print(n)
	
	nombresPremiers = facteursPremier
	facteursPremier = {}
	#print(nombresPremiers)
	
	for item in nombresPremiers:
		if item not in facteursPremier:
			facteursPremier[item] = nombresPremiers.count(item)
	
	print(facteursPremier)
	return facteursPremier

def ppcm(a,b):
	puissancesPremiereA = decomposerNombre(a)
	puissancesPremiereB = decomposerNombre(b)
	valeurPpcm = 1
	
	#print(puissancesPremiereA, "\n", puissancesPremiereB)
	
	dictSmale = {}
	dictBig = {}
	
	if len(puissancesPremiereA) <= len(puissancesPremiereB):
		dictSmale = puissancesPremiereA
		dictBig = puissancesPremiereB
	else:
		dictSmale = puissancesPremiereB
		dictBig = puissancesPremiereA
	
	#print(dictSmale)
	for key in dictSmale:
		if key in dictBig:
			print(key," = ",max(dictSmale[key],dictBig[key]))
			valeurPpcm *= key**max(dictSmale[key],dictBig[key])
		
	print(valeurPpcm)	
	return valeurPpcm
	

