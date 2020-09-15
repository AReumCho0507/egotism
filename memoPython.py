'''
f = open("아름.txt", 'w')
f.close()

f = open("오찬해.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
'''

f = open("오찬해.txt", 'w', encoding='utf-8')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

f = open("오찬해.txt", 'r',encoding='utf-8')
data = f.read()
print(data)
lines = f.readlines()
for line in lines:
    print(line)
#폰노이만



