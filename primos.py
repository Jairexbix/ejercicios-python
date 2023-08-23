def is_primo (n):
	for i in range(2,n):
		if (n%i) == 0:
			return False
	return True

def primos(num):
	res_primos = [1]
	contador = 2
	while len(res_primos) < num:
		result = is_primo(contador)
		if result == True:
			res_primos.append(contador)
		contador += 1
	return res_primos
resultado = primos(50)
print(resultado)