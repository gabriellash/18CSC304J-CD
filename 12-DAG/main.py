a = input().split()
strings = {'T1' : ' ','T2' : ' ','T5' : ' ','a' : ' '}
for i in a:
    if i[0] in ['-', '+']:
        strings['T1'] = i
        break
for i in range(len(a)):
    if (a[i] =='*'):
        strings['T2'] = f'{a[i - 1]}*T1'
        break
strings['T5'] = 'T2+T2'
strings['a']='T3'
for key, value in strings.items():
    print(key, '=', value)