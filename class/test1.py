'''
money = True
if money:
    print('택시를 타고 가라')
else:
    print("걸어가라")

print(1==1)
print(1==2)

#==, <=, >=, !=

print(1!=2)

money = 3000
#6000원이면 탈 수 있음
if money >= 6000:
    print('택시 탈 수 있음')
elif money >= 2000: #else+if 아니면 만약에 합성어
    print('버스 타야함')
else:
    print('걸어가야함')


#and, or, not

x = 1
y = 1
# x==1 : True
# True and True 1개라도 false이면 작동하지 않음

if x== 1 and y==2:
    print('working')
else:
    print('working2')


#Tue of False, False or True, True or True // False or False
c = 100
y = 200
money = 150

if c >= moeny or y >= money:
    print('입장')
    

# not : 부정
# not True : False
# not False : True

if not False:
    print('working')
    
#부정일 경우 작동하지 않음


#and or not 꼭 알아두기

#in과 not in

w = [100, 500, 1000]

if 100 in w:
    print('있다')

if 5000 in w:
    print("집에서 가져와야 겠다")
#리스트나 어떠한 열거형을 구현할 수 있는 것들의 안에 있는지 없는지에 대한 사실을
#나타냄


if 5000 not in w:
    print('집에서 가져와야겠다.')
    



[91, 80, 72, 64, 59]
 90점 이상 : 아주 잘했어요
 80점 이상 : 잘했어요
 70점 이상 : 노력하세요
 60점 이상 : 공부하세요
 60점 미만 : 낙제
 
 변수 : score


test = [91, 80, 72, 64, 59]

score = 91
if score >= 90:
    print('아주 잘했어요')
elif score >= 80:
    print('잘했어요')
elif score >= 70:
    print('노력하세요')
elif score >= 60:
    print('공부하세요')
else:
    print('낙제')

#while문 ~하는 동안에

treehit = 0
while True:
    treehit = treehit +1
    print("나무를 %d번 찍었습니다" % treehit)
    if treehit == 10:
        print("나무 넘어갑니다")
     break:

print('끝')



a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)


    if a % 2 == 1:
        print(a)


 #for문
test = [91, 80, 72, 64, 59]

for score in [91, 80, 72, 64, 59]:
    print(score)

#range : 범위를 나타내는 함수
#range(시작지점, 끝나는 지점(+1), 얼만큼 커지는지)

for i in range(1, 6, 1):
    if i % 2 == 0:
     print(i)

for i in range(2, 6, 2):
    print(i)



temp = [1,2,3,4,(5,6)]

print(type(()))
for x in temp:
    print(x)

temp = [(1,2), (3,4), (5,6)]

for a,b in temp:
    print(a)
    print(b)
    print(a+b)
#튜플의 패키징을 푸는 것, 언팩킹이라고 한다, 파이썬에는 이런 문법도 지원함

#test : 변수
#for문과 if문을 조합

test = [91, 82, 73, 61, 59]

for score in test:
 if score >= 90:
    print('아주 잘했어요')
 elif score >= 80:
    print('잘했어요')
 elif score >= 70:
    print('노력하세요')
 elif score >= 60:
    print('공부하세요')
 else:
    print('낙제')


test = [91, 82, 73, 61, 59]
print(list(enumerate(test)))
for i, score in enumerate(test):
    if score >= 90:
        print('%d번째 학생은 참 잘했어요' % i)
    elif score >= 80:
        print('%d번째 학생은 잘했어요' % i)
    elif score >= 70:
        print('%d번째 학생은 노력해요' % i)
    elif score >= 60:
        print('%d번째 학생은 공부하세요' % i)
    else:
        print('낙제')

#enumerate 는 인덱스를 뽑아낼 때 쉽다

list = [1]
for i in range(2, 11, 1):
    list.append(i)
    print('i=', i, 'list = ', list)

print(list)

list = [1]
print(list + list(range(2, 11, 1)))
print(list)
#for i in range(2, 11, 1):

# if(만약에), elif(만약이 아니면), else(아니면) 외우기, in, and, or, not
# 비교연산자, while(참일때만 작동 false는 바로 다음걸로 넘어감)
# if 조건문 brake, continue, for문

'''