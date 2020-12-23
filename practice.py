
print("Hello World - Coding")
print(5) #숫자
print(100000)
print(5*3+(2-2)/4)
print("장하다.") #문자
print('잘하고있다')
print("넌 할수있다"*3)

# 한줄 주석사용하기
'''여러줄 주석처리하기
방법'''

# 들여쓰기
print('a"')
print('b')
print('c')

# 조건 참/거짓
print(5>10)
print(5<10)
print(True)
print(False)

# 줄바꿈 ( \n ) 같음 ( == )

# 변수, 이름규칙(영문자( 대,소문자구분). - (언더스코어), 숫자(1)만사용 단 숫자는-첫글짜불가
a = 10
b = 5
print(a)
print(b)
print(a*b)
b = 7
print(a*b)
var = 7
print(type(var))
var = '문자열'
print(type(var))


#함수-이름(인자값,인자값,인자갑, ...) ---> 리턴 값
# 자료형함수 / type()

# perfix '0b'는 2진수,'0o'는 8진수,'0x'는 16진수 입니다.
print(0b10)
# 숫자형 (정수형-int, 실수형-float, 복수형-complex)
# 산술연산자 ( +, -, *, /, //(몫), %(나머지))

a=10
b=5
c=2.0
d=0.5
print(a+b)
print(a//b) # 몫
print(a%c)  # 나머지
print(a**d) # 제곱

# 논리연산자 ( or, and, not )
print((100 > 10) or (30 <= 3)) # True or False -> True
print((10 == 10) and (3 != 3)) # True and False -> False
print(not (3 <= 3))            # not True -> False

# boolean type : bool ( True( 1, 비어있지않음), False( 0, 비어있음) )

# 비교연산자 ( < , <=, >, >=, ==(같음), !=(같지않음) )

a = 100
b = 50
print(a>=b)
print(a<=b)
print(a>=b)
print(a==b)

# 문자열형 ( str ~, ' ', " ", '''''', """ """, / 문자+문지, 문자*정수)
py = "파이썬으로 코딩을 배우자"
print(py[3])
print(py[1])
print(py[-1])
print(len(py))
# 문자열 slicing (자르기) / [ ? : ? ]
print(py[3])
print(py[4:9])
print(py[:4])
print(py[4:])
# count(), find(), index()
py = "python programming"
print(py.count('p'))
print(py.find('o'))
print(py.index('o'))
print(py.find('w'))
# 대소문자전환 ( upper(), iower() )
print(py.upper())
print(py.lower())
# 문자열 변경하기 ( replace() )
py = "파이썬 공부는 너무 재밌어요!"
print(py.replace("파이썬","HTML"))
print(py)
# 문자열 나누기 ( spiit() 띄어쓰기, 공백기준 )
print(py.split(' '))
print(py.split())
print(py)

# 조건문
# if ~ else
con = "sweet"

if con == "sweet":
   print("삼키다")
    
else:
    print("뱉는다")
season = "summer"  
if season == "spring":
    print("봄이 왔네요!")
else:
    if season == "summer":
        print("여름에는 더워요~")
    else:
        if season == "fall":
            print("가을은 독서의 계절!")
        else:
            if season == "winter":
                print("겨울에는 눈이 와요~")   
# if ~ elif
season = 'winter'
if season == 'spring':
    print ("봄")
elif season == "summer":
    print (여름)
elif season == 'fall':
    print ('가을')
elif season == 'winter':
    print ('겨울')
# if pass - 아무일 하지않기

temp = 30
if temp < 26:
    pass
else:
    print ('에어컨을 켠다.')

num = int (input('숫자 하나 입력 : '))
if num > 0 :
    print('{} 은 양수입니다')

# if ~ elif ~ else


# iteration statement - 반복문

# while 조건: - 실행코em / 조건이 참일때 실행반복
i = 1

while i < 11: # 조건식

    print("파이썬 " + str(i))

    i = i + 1 # 탈출 조건

# 무한루프
a = int ( input('a'))
while a<=2 :
    print('실행')

# for문- n번, ~까지 반복하기 / for 변수 in (문자열,tuple,list) 명령문
str = "파이썬 프로그래밍"  
for ch in str:
    print(ch)
# range(마지막정수)/(시작정수,마지막정수)
for col in range(2,3):
    for row in range(1,5):
        print (col,'x',row, '=',col*row)
# break와 continue
for col in range(2,10):
        if col > 3:
           break
for row in range (1,10):
        print (col,'x',row,'=',col*row) 

for n in range(1,11):
    if n % 2 == 0:
        continue
    print(n, '은 홀수입니다')

# 데이터 구조 ( )
# 군집자료형 ( list, tuple, set, dictionary)
# list type ( 대괄호[] ,쉼표','로구분 )
primes = [2,3,5,7]
for p in primes:
    print(p)
print(len(primes))

print(primes[0])
print(primes[-1])
print(primes[1]+primes[3])
# 문자열 slicing ( 콜론 - : , )
print(primes[3])
print(primes[1:3])
print(primes[:3])
print(primes[2:])
print(primes)
# 리스트 복사하기01-주소만 넘겨줌
copy = primes
copy.append(10)
print(copy)
print(primes)
# 리스트 복사하기01-제대로복사/슬라이싱사용
copy = primes[:]
copy.append(11)
print(copy)
print(primes)
#리스트끼리연산
list1 = [1,2,3]
list2 = [4,5,6]
print(list1*3)
print(list1 + list2)
list1.extend(list2) # 원본리스트 변경함
# 리스트 요소추가,제거(요소가 두개이상시 인덱스가 낮은요소제거)
print(list1)
list1 = [1,2,3,4,5]
list1.append(10)
print(list1)
list1.remove(4)
list1.remove(3)
print(list1)
# 리스트에 요소삽입(insert(인수,요소))이나 꺼내기(pop(인수))
list1 = [1,2,3,4,5]
list1.insert(3,9)
print(list1)

list1.pop(4)
print(list1)
# 리스트 뒤집거나(rever()) 정렬하기(sort())
list1 = [1,2,3,4,5]
list2 = [5,2,4,1,3]
list1.reverse()
print(list1)
list1.sort() # 원본변경
print(list1)
print(sorted(list2)) # 원본변경없음
print(list2)
# 중첩 리스트
matrix = [[1,2,3],['하나','둘','셋']]
print(matrix[0])
print(matrix[1])
print(matrix[0][0])
print(matrix[1][2])
# tuple ( 쉼표(,)로구분, 소괄호()로 감싸거나 아예 감싸지 않는다.)
# 튜플명 = (요소,1요소2,요소3)/요소1,요소2,요소3...
tuple1 = (1,2,3)
tuple2 = 1,2,3,
tuple3 = 1,
tuple4 = 1
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
tuple1 = (1, 2, 3)
tuple2 = tuple(["원", "투", "쓰리"])
 # 튜플 요소 선택하기
print(tuple1[0])
print(tuple2[-1])  
# 튜플 자르기
print(tuple1[1:])
print(tuple2[:2])  
# 튜플끼리의 연산
print(tuple1 + tuple2)
print(tuple1 * 2)
# 패킹-packing
tuple = 10,"열",True
# unpacking
a,b,c = tuple
print(a),print(b),print(c)
# 특정요소의포함여부 - in, not in 참-true/ 거짓-false
print(10 in tuple)
print("일곱" in tuple)
print("일곱" not in tuple)

# set tyoe ( 세트선언 중괄호{}/ 요소구분 쉼표(,)/중복제거,순서무시)
# 세트명 = (요소1, 요소2, 요소3, ...)
set1 = {1,2,3}
set2 = set("python")
set3 = set("hello")
print(set1)
print(set2)
print(set3)

set1 = {}
set2 = set()
print(type(set1))
print(type(set2)) # empty set

set1 = {1,2,3}
set1.add(4) # set 요소추가
print(set1)
set1.update((5,6)) # set 여러요소추가
print(set1)
set1.remove(2) # set 요소제거
print(set1)
# 집합연산
set1 = {1,2,3,4,5}
set2 = {1,3,5,7,9}
print(set1 | set2) # 합집합
print(set1 & set2) # 교집함
print(set1 - set2) # 차집합
print(set1 ^ set2) # 여집합 = 합집합 - 교집합

# dictionary ( 선언-중괄호/구분-쉼표(,)/key와 value연결-콜론(:))
dict1 = {'하나':1,'둘':'two','파이':3.14}
dict2 = dict({'하나':1,'둘':'two','파이':3.14})
dict3 = dict([('하나',1),('둘','two'),('파이',3.14)])
dict4 = dict(하나=1,둘='teo',파이=3.14)
print(dict1)
print(dict2)
print(dict3)
print(dict4)

dict1 = {'하나':1, 2:'two', 3.14:'pi'}
dict2 = {('ten',10):['열',10.0]}
print(dict1)
print(dict2)

#  대괄호([])안에 key를 가지고 value를 알수있다. / get()함수 사용
dict1 = {'하나':1, 2:'two', 3.14:'pi'}
dict2 = {('ten',10):['열',10.0]}
print(dict1['하나'])
print(dict1.get('two'))
print(dict1.get(2))
# 요소삽입 - 대괄호([])안에 key를 넣고 대입연산자(=)를 사용하여 value를 저장
dict1 = {'하나':1, 2:'two', 3.14:'pi'}
dict1 ['파이썬'] = 100
print(dict1)
del dict1[2]  # del = key 워드 / clear()
print(dict1)
dict1['하나'] = 1000
print(dict1)

# keys()-key값들 / values()-value값들 / items()-key,value값들
print(dict1.keys())
print(dict1.values)
print(dict1.items())
# 찾기- in  = key 워드
print('하나'in dict1)
print('HTML'in dict1)
dict1.clear()
print(dict1)
## 함수 function - 하나의 특정작업을 수행하기위한 프로그램코드집합
## def 함수명 (매개변수-parameter1,...) / 
# 실행할 코드1,
# 실행할 코드2
# return 결과값
def hello():
    print("hello")  
    print("-함수시작-")
    print("안녕")
hello() # 함수호출
hello() # 함수호출

# 인수 arguments - 함수호출시 내부에서 사용할 데이터 전달 역할.
# 소괄호()안에 쉼표로(,)로 구분
def sum(a,b):
    print(a + b)
sum(1,2)
sum(3,4)
# 값을 반환(return)하는 함수
def sum (a, b):
    print('함수시작')
    print('함수끝')
    return a+b
c = sum (1, 2)
print(c)
print(sum(3,4))

def sum (a, b):  
    print('함수시작')
    return a+b
    print('함수끝') 
c = sum (1, 2)
print(c)
print(sum(3,4))
# 인수 전달시 매개변수 지정
def sub(a,b):
     print(a-b)
sub(1,2)
sub(a=1,b=2)
sub(b=1,a=2)
# parameters의 기본값 설정
def total(a,b=5,c=10):
    print(a+b+c)
total(1)       
total(1,2)
total(1,2,3)
# variable parameters 가변매개변수
# 매개변수명 앞에 별(*)기호를 추가선언
def  add(*paras):
    print(paras)
    total = 0
    for para in paras:
        total += para
    return total

print(add(10))
print(add(10,100))
print(add(10,100,1000))
        
 # 매개변수로 딕서너리 시용시 명앞에 별(**)기호를 추가선언   
def print_map(**dicts):
    for item in dicts.items():
        print(item)
print_map(하나=1)
print_map(one=1,two=2)
print_map(하나=1,둘=2,셋=3)

# 여러개의 결과값 반환하기
def arith(a,b):
    add = a+b
    sub = a-b
    return add,sub

i,j = arith (10,1)
print(i)
print(j)

# lambda - 간단한 함수의 선언과 호출을 하나의 식으로
def add(a,b):
    return a+b

print(add(1,2))
print((lambda a,b:a+b)(1,2))

## variable scope 변수의 유효범위
# 지역변수 local variable
def func():
    local_var = "local variable"
    print(local_var)

func()
# print( locar_variable)
# 전역변수 global variable
def func():
    global global_var
    local_var = "local variable"
    print(local_var)
    print(global_var)
global_var = 'global variable'
func()
print(global_var)

def func():
    var = '지역변수'
    print(var)
var = '전역변수'
print(var)
func()
print(var)

# 자료형 변환

# 함수
def order():
    print('주문하실 음료를 알려주세요')
    drink = input()
    print(drink,'주문하셨습니다.')
order()
    
print("XX행 열차가 들어오고 있습니다.")
station = "광주행"
print(station + "열차가 들어오고 있습니다.")

#함수-이름(인자값,인자값,인자갑, ...) ---> 리턴 값

print('hi','hellow')
name = input ('이름을 입력하세요?')
print('안녕하세요?',name)
   
# class와 object / objec-oriented programming
# class member / attribute-속성(변수)와 method-메소드(함수)
class Dog:
    name = '삼식이'
    age = 3
    breed = '골든 리트리버'
    def bark(self):
        print(self.name +'가 멍멍하고 짖는다.')

# instance란 class를 기반으로한 object-객체
# 소괄호()로 생성, 닷(.)연산지를 사용하여 호출
my_dog = Dog()
print(my_dog.breed)
my_dog.bark()
# 초기화 메소드 (initialize method) / __init__
class Dog:
    def __init__(self,name):
        self.name = name
    def bark(self):
        print(self.name + "가 멍멍하고 짖는다.")   
# class variable - 모든 인스턴스가 값을 공유
# instance variable - __init__()내에 선언된 변수

class Dog:
    sound = '멍멍'
    def __init__(self,name):
        self.name = name
    def bark(self):
        print(self.name + "가 멍멍하고 짖는다.")

my_dog = Dog ("삼식이")
your_dog = Dog ("콩이")

print(my_dog.sound)
print(my_dog.name)

print(your_dog.sound)
print(your_dog.name)

# inheritance(상속) - parent(base) class / child(derived) crass
# 소괄호(())사용

class Bird:
    def __init__(self):
        self.flying = True
    def birdsong(self):
        print('새소리')
class Sparrow(Bird):
    def birdsonf(self):
        print('짹짹')

my_pet = Sparrow()
print(my_pet.flying)
my_pet.birdsong()

# method overriding
class Bird:
    def __init__(self):
        self.flying = True
    def birdsong(self):
        print('새소리')
class Sparrow(Bird):
    def birdsong(self):
        print('짹짹')
class Chicken(Bird):
    def __init__(self):
        self.flying = False
my_sparrow = Sparrow()
my_chicken = Chicken()

my_sparrow.birdsong()
my_chicken.birdsong()

# access control -접근제어
# public = (_)포함되지않음/ 
# private = (__)두개,접두사/ 
# protected = (_)한개,접두사

## 입출력및 예외처리
# module - 모듈 / import문 / 코드맨앞유리 / 닷(.)연산자
# import 모듈명/ from 모듈명 import * / from 모듈명 import 함수명또는 클래스명

import math
print(math.pi)
print(math.pow(2,2)) # pow함수 = 2^N

from math import *
print(pi)
print(pow(2,2))

e = '내가 정의한 변수e'
print(e)
from math import * # e - 오일러의 수
print(e)
print(pi)

e = '내가 정의한 변수e'
from math import pi
print(e)
print(pi)

# 파일 입출력-input(), print() / open(), close()

# r(read mode, 기본값)/w(write mode)/a(append mode)
# t(text mode,기본값)/b(binary mode)
# x(exclusive mode)/+(update mode)

# 파일내용 읽기 - 1.read()/readline()/readlines()
# 파일내용추가 - write()
# 자동으로 파일 닫기 - with문

# exception handling - 예외처리
# try문~finally절, excet문~else문
# 예외 발생시키기 - raise 키워드
class Bird:
      def birdsong(self):
        raise NotImplementedError    

class Chicken(Bird):
    def birdsong(self):
        print("짹짹")    
my_chicken = Chicken()
my_chicken.birdsong()
