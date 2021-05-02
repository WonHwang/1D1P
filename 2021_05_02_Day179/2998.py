binary = input()

octo = {
    '000' : '0',
    '001' : '1',
    '010' : '2',
    '011' : '3',
    '100' : '4',
    '101' : '5',
    '110' : '6',
    '111' : '7'
}

while len(binary) % 3:
    binary = '0' + binary

answer = ''
for i in range(0, len(binary), 3):
    tmp = binary[i:i+3]
    answer += octo[tmp]

print(answer)