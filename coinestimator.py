#Modify code to display 'mass' for grams and 'weight' for pounds
tokens = {'pennies' : {'mass' : 0,
					  'coin_mass' : 2.500,
					  'coins' : 0,
					  'cpw' : 50,
					  'wrappers' : 0,
					  'coin_value' : .01,
					  'value' : 0},
		 'nickels' : {'mass' : 0,
					  'coin_mass' : 5.000,
					  'coins' : 0,
					  'cpw' : 40,
					  'wrappers' : 0,
					  'coin_value' : .05,
					  'value' : 0},
		 'dimes' : {'mass' : 0,
					'coin_mass' : 2.268,
					'coins' : 0,
					'cpw' : 50,
					'wrappers' : 0,
					'coin_value' : .1,
					'value' : 0},
		 'quarters' : {'mass' : 0,
					   'coin_mass' : 5.670,
					   'coins' : 0,
					   'cpw' : 40,
					   'wrappers' : 0,
					   'coin_value' : .25,
					   'value' : 0}}

def set_unit():
	selection = input("Unit of measurement:\n\n" \
					  " a)Grams\n" \
					  " b)Pounds\n\n" \
					  "Please make a selection: ")
	
	if len(selection) == 1 and selection in "ab":
		if selection == 'a':
			return 1
		else:
			return 453.592
	else:
		print("Please try again.\n")
		set_unit()

def set_attribs(c):
	m = input("Enter the mass of {}: ".format(c))
	if m.isnumeric():
		tokens[c]['mass'] = int(m) * conversion
		tokens[c]['coins'] = int(tokens[c]['mass'] // tokens[c]['coin_mass'])
		tokens[c]['wrappers'] = int(tokens[c]['coins'] // tokens[c]['cpw'])
		tokens[c]['value'] = tokens[c]['coins'] * tokens[c]['coin_value']
	else:
		set_attribs(c)
		
conversion = set_unit()

for c in tokens:
	set_attribs(c)

wrapper_totals = [tokens[t]['wrappers'] for t in tokens]
wrapper_totals = [sum(wrapper_totals)] + wrapper_totals
coin_totals = [tokens[t]['coins'] for t in tokens]
coin_totals = [sum(coin_totals)] + coin_totals
money_totals = [tokens[t]['value'] for t in tokens]
money_totals = [sum(money_totals)] + money_totals

print("You will need {0:,} wrappers; {1:,} penny, {2:,} nickel, {3:,} dime and {4:,} quarter wrappers.".format(*wrapper_totals))
print("You have {0:,} coins; {1:,} pennies, {2:,} nickels, {3:,} dimes and {4:,} quarters.".format(*coin_totals))
print("You have ${0:,.2f}; ${1:,.2f} in pennies, ${2:,.2f} in nickels, ${3:,.2f} in dimes and ${4:,.2f} in quarters.".format(*money_totals))