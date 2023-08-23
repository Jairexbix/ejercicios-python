
numeros = []

i = 1
while i <= 100:
	
	div3 = i % 3
	div5 = i % 5
	
	if div3 == 0 and div5 == 0:
		numeros.append('fizzbuzz')
	elif div3 == 0:
		numeros.append('fizz')
	elif div5 == 0:
		numeros.append('buzz')
	else:
		numeros.append(i)
	
	i += 1


print(numeros)