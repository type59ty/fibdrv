expected = [0,1]

for i in range(2,101):
    expected.append(expected[i-1] + expected[i-2]);

i=0
fai=0
for row in open('result.txt'):
    if (expected[i]==int(row[:-1])):
        print('f({})   ok'.format(i))
    else:
        print('f({})   fail'.format(i))
        fai=fai+1
    i=i+1
print()
if (fai):
    print('=============FAIL=============')
    print('There are {} error'.format(fai))
else:
    print('=============PASS=============')

