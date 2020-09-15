def add(a, b):
    print(a + b)
    return a + b

add(1,2)

a = 3
b = add(1,2)

#add를 먼저 설계한다.

def say():
    return 'hi'

a = say()
print(a)
#입력값이 없어도 구현이 된다.
#파이썬은 return값이 없어도 된다

def add(a,b):
    print(a+b)

def add_many(*args): #args 여러개 들어간다라는 뜻
    result = 0
    print(type(args))
    print(args)
    for i in args:
        result = result + i
    return result

add_many(1,2,3,4,5)

#키워드 파라미터는 잘 안쓰임

def add_and_mul(a,b):
    return a+b, a*b

a, m = add_and_mul(1,2)
print(a,m)

print(add_and_mul(1,2))

'''
a=1 
def f(): 
a2=1 
return a2 
print(a)
전역변수, 지역변수 
'''
'''
a = 1

def vartest():
    c = a + 1
    print(c)
vartest()
print(a)
a = 1
'''
a = 1

def vartest():
    global a
    a = 2

vartest()
print(a)

#global은 지역변수가 전역변수를 건드리는 것


def hello():
    print("Hi")
hello()

def message() :
    print("A")
    print("B")

message()
print("C")
message()

def message() :
    print("A")
    print("B")

message()
print("C")
message()

print("A")

def message() :
    print("B")

print("C")
message()

def s(a):
    print(a)

s("python")

#매개변수를 지정해야한다.

def s(a='python'):
    print(a)

s()

#매개변수를 안넣을 경우에는 디폴트값을 준다.

def print_with_smile( a = "안녕"):
    print(a + ":D")

print_with_smile("잘가")

#디폴트값이 있으면 매개변수가 있더라도 값에 따라 나뉘게 된다.

def print_with_smile(*say):
    for s in say:
        print(s, end=' ')
    print(':D')

print_with_smile('안녕하세요~','오찬해 입니다~')

number = int(input("숫자를 입력하세요:", ))
print(number)

