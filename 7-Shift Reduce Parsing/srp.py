gram = {
	"E":["E*E","E+E","i"]
}
starting_terminal = "E"
inp = "i+i*i"

stack = "$"
print(f"{'Stack': <15}|" + f"{'Input Buffer': <15}" + "|" + 'Parsing Action')
print(f'{"-":-<50}')

while True:
	action = True
	i = 0
	while i<len(gram[starting_terminal]):
		if gram[starting_terminal][i] in stack:
			stack = stack.replace(gram[starting_terminal][i],starting_terminal)
			print(
				f'{stack: <15}|'
				+ f'{inp: <15}'
				+ "|"
				+ f'Reduce S->{gram[starting_terminal][i]}'
			)
			i=-1
			action = False
		i+=1
	if len(inp)>1:
		stack+=inp[0]
		inp=inp[1:]
		print(f'{stack: <15}|' + f'{inp: <15}' + "|" + 'Shift')
		action = False

	if inp == "$" and stack == f"${starting_terminal}":
		print(f'{stack: <15}|' + f'{inp: <15}' + "|" + 'Accepted')
		break

	if action:
		print(f'{stack: <15}|' + f'{inp: <15}' + "|" + 'Rejected')
		break