
def maxi(num1,num2):
	if num2 < num1:
		return num1
	elif num2 > num1:
		return num2
	else:
		res = 'son iguales'
		return res

def len_me(e):
	for i,el in enumerate(e):
		last = i
	return last +1

def is_vocal(e):
	if e == 'a' or e == 'e' or e == 'i' or e == 'o' or e == 'u':
		return True
	else:
		return False
		
def sum_me(lista):
	total = 0
	for num in lista:
		total = total + num
	return total
def mult(lista):
	total = 1
	for num in lista:
		total = total * num
	return total
		
def inverse (stri):
	new_str = ''
	i = 1
	while i <= len(stri):
		new_str += stri[-i]
		i += 1
	return new_str

def is_palindromo(stri):
	new_str = inverse(stri)
	if new_str == stri:
		return True
	else: 
		return False

def superposicion(list1,list2):
	res = False
	for e1 in list1:
		for e2 in list2:
			if e1 == e2:
				res = True
				break
		if res == True:
			break
	return res

def n_char(num,char):
	res = char * num
	return res

def procedimiemto (lista):
	for e in lista:
		res = '*' * e
		print(res)
