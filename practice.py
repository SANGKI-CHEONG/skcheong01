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

# set type




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
   

