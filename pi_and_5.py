from math import sin, pi

def scientific_notation(number):
	tens = 0
	while number < 1:
		number *= 10
		tens += 1
	return [number, tens]

def Approximation_of_pi():
	while TRUE:
		inp = input("Please enter the number of 5s or 'e' to exit: ")
		if inp == 'e':
			print("Have a good time")
			return
		quantity_of_5 = int(inp)
		denominator = int('5' * quantity_of_5)
		scientified = scientific_notation(sin(pi/(denominator*180)))
		print("the digits are: ",scientified[0],'*10^(-',scientified[1],')',sep='')
		print("pi is: ", pi)
		error = (scientified[0]-pi)
		print("difference between the digits and pi is:",error)

if __name__ == "__main__":
	Approximation_of_pi()
