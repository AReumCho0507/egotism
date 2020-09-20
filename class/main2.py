from homework.book2 import Book
if __name__== '__main__':
    b = Book()
    while True:
        x = '\n1. 종료\n 2. 선택\n 3. 등록'
        print(x)
        put = input("1~3 사이의 숫자를 입력하세요: ")
        if put == '1':
            print("프로그램을 종료합니다.")
            break

        elif put == '2':
            b.select()

        elif put == '3':
            b.register()