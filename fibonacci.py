
cant = int(input('Cantidad de numeros fibonacci: '))
fibo_num = [1,1]

def fibo (n):
	for num in range(1,n):
		new_num = fibo_num[-1] + fibo_num[-2]
		fibo_num.append(new_num)
		
		
fibo(cant)
print(fibo_num)