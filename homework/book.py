#도서관리시스템 register
#새로운 책을 등록하는 함수
#규격함수 : select
#메모장에서 읽어오는 것
#'ㄱ' 1234, 'ㄴ' 5678 'ㄷ' 910 'ㄹ' 1112
#없으면 없다고 나와야 함
#1을 집어 넣으면 종료가 되고 2를 집어 넣으면 선택 3을 집어 넣으면 책 등록하기
# 다른숫자 넣으면 다시 넣으세요

'''
f = open("도서관리시스템.txt", 'w',encoding='utf-8')
data = ['ㄱ: 1, 2, 3, 4\n', 'ㄴ: 5, 6, 7, 8\n', 'ㄷ: 9, 10\n', 'ㄹ: 11, 12\n']
for i in data:
    f.write(i)
f.close()
print(data)
#메모장에 값 넣기
'''

def register_book():
    name = input("책 이름을 입력하세요: ")
    code = input("코드를 입력하세요: ")  # '1234' -> int() 1234
    f = open("도서관리시스템.txt", 'a', encoding='utf-8')
    f.write(name + ':' + code + '\n')
    f.close()
    print('-' * 30)
    print("책이 입력 되었습니다.")
    print(':', code)
    print('-' * 30)

def select_book():
    name = input("책 이름을 입력하세요: ")
    f = open("도서관리시스템.txt", 'r', encoding='utf-8')
    lst = f.read()
    lst = lst.split('\n')
    for x in lst:
        name2 = ''
        code2 = ''
        for i, y in enumerate(x):
            if y == ':':
                name2 = x[:i]
                code2 = x[i + 1:]
                break

        if name == name2:
            print("책이름: ", name2)
            print("코드: ", code2)
            break
    else:
        print("책이 없습니다. 등록하시오.")
    f.close()

print('-'*30)
x = '\n1. 종료\n 2. 선택\n 3. 등록'

while True:
    print(x)
    put = input("1~3 사이의 숫자를 입력하세요: ")

    if put == '1':
        print("프로그램을 종료합니다.")
        break

    elif put == '2':
        select_book()

    elif put == '3':
        register_book()