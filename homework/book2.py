class Book:
    def register(self):
        name = input("책 이름을 입력하세요: ")
        code = input("코드를 입력하세요: ")  # '1234' -> int() 1234
        f = open("도서관리시스템.txt", 'a', encoding='utf-8')
        f.write(name + ':' + code + '\n')
        f.close()
        print('-' * 30)
        print("책이 입력 되었습니다.")
        print(':', code)
        print('-' * 30)

    def select(self):
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


#clss는 함수들의 집합, 함수는 기능을 담당하는 무언가 한 곳에 모아둔 집약체가 clss


