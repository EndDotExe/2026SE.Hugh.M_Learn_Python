def main():
	dollars = dollars_to_float(input("How much was the meal? "))
	percent = percent_to_float(input("What percentage would you like to tip? "))
	tip = dollars * percent
	print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
	# convert the dollars into a float
	result = d.replace ('$', '')
	return float (result)

def percent_to_float(p):
	# convert the tip percentage into a float
	tipp = p.replace('%', '')
	return float (tipp) / 100
main()