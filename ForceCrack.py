from itertools import permutations

alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j','k','l','m', 'n', 'o', 'p', 'q', 'r','s','t','u','v', 'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9']
case = input('add test pw: ')
case.lower()
tries = 0
status = 'ongoing'
pw =''

def case_test (pw,status,case,tries,alp):
	lenn = int(input('How many characters you want to try?'))
	if lenn < len(case):
		print("The password has more characters than that")
		return
	guess = ''
	while status != 'done' :
		pw = permutations(alp,lenn)
		for i in pw:
			guess = ''.join(i)
			print(guess)
			tries +=1
			if guess == case:
				status = 'done'
				print('the password is ' + guess + ' , that took {} tries '.format(tries))
				break

case_test(pw,status,case,tries,alp)


