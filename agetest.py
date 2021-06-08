driving = input('have you ever driven a car?')
if driving != 'yes' and driving != 'no':
	print('you can only enter yes or no')
	raise SystemExit
age = input('What is your age?')
age = int(age)
if driving == 'yes' or driving == 'y':
	if age >= 18:
		print('you have passed the test!')
	else:
		print('it is weird, how can you even drive?')
elif driving == 'no' or driving == 'n':
	if age >= 18:
		print('you can get a driving license')
	else:
		print('oups')
else: 
	print('you can only enter yes or no')