print(''' 																BULLS AND COWS
RULES:-
1) YOU HAVE TO GUESS A 4 DIGIT NUMBER
2) IF THE DIGIT OF YOUR NUMBER MATCHES THE DIGIT IN THE COMPUTER GENERATED NUMBER BUT NOT IN THE RIGHT PLACE, IT WILL BE A COW.
3) IF YOUR NUMBER HAS A DIGIT AT SAME PLACE AS THE COMPUTER GENERATED NUMBER IT WILL BE A BULL
4) THE LOWER CHANCES YOU TAKE TO GUESS THE NUMBER, THE BETTER
5) ALSO REMEMBER ALL THE DIGITS OF THE NUMBER ARE DIFFERENT''')
print()


def number():
	import random
	a = random.randint(1000, 9999)
	a = str(a)
	b = list(a)
	global chance
	chance = 0
	for j in range(len(b) - 1):
		if b.count(b[j]) > 1:
			return number()

	def game():
		global b
		t = list(a)
		b = t
	#	print(t)
		global chance

		while True:
			_input = str(input('Guess the number: '))
			t_input = list(_input)
			count_b = 0
			count_c = 0
			chance += 1
			if t_input == t:
				print('congratulations!! you guessed correctly in', chance, 'chances')
				enter = input('If you want to play again press "1" otherwise press any other key: ')
				if enter == '1':
					print()
					return number()
				else:
					break
			elif len(t_input) != 4:
				print('Enter a 4 digit number')
			else:

				for i in range(len(t)):
					if t_input.count(t_input[i]) > 1:
						print('All the numbers should be different')
						return game()
					elif t_input[i] == t[i]:
						count_b += 1
					elif t_input[i] in t and t_input[i] != t[i]:
						count_c += 1

				print('your guessed number has ', count_b, 'bulls and ', count_c, 'cows')
				return game()

	game()


number()
