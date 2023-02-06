'''letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력'''

letters = 'python'
print(letters[0], letters[2]) # 결과 : p t

'''int형 숫자여도 인덱싱이 될까?''' 
# letters2 = int(123)
# print(letters2[0], letters2[2])

'''    print(letters2[0], letters2[2])
          ~~~~~~~~^^^
TypeError: 'int' object is not subscriptable''' # 결과 : 오류 발생
# 정수형(int)에서 '인덱싱' 및 '슬라이싱'을 시도할 때 발생하는 오류
# 자료형 관련 에러다

'''음수 매개변수를 입력하면 어떻게 될까?''' # 결과 : n o
print(letters[-1], letters[-2]) 
# 뒤에서부터 정상적으로 인덱싱이 이루어진다.
# 파이썬 문자열에서 한 글자를 가져오는 것을 인덱싱이라고 부른다.

'''자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.[문자열 슬라이싱]'''
license_plate = "24가 2210"
print(license_plate[4:8]) # [4:8]은 [4부터 : 8미만까지]라고 생각하면 편하다. # 결과 : 2210
print(license_plate[-4:]) # [-4:]는 [뒤에서 4번째 부터 끝까지] 라는 의미다. [시작 : 끝(미만)] # 결과 : 2210
# 반대의 경우 시작을 생략하면 0으로 간주한다.

'''문자열을 거꾸로 뒤집어 출력하세요.[문자열 슬라이싱]'''
string = "PYTHON"
print(string[::-1]) # 결과 : NOHTYP
# [시작 : 끝 : 증가폭]
# 증가폭을 음수로 입력하면 뒤에서부터 가져온다.

'''아래의 전화번호에서 하이푼 ('-')을 제거하고 출력 [문자열 치환]'''
phone_number = "010-1111-2222" 
# phone_number2 = phone_number['-',' ']

# TypeError: string indices must be integers, not 'tuple' [에러발생]
# phone_number2 = phone_number("-"," ")
# 'str' object is not callable [에러발생]

phone_number2 = phone_number.replace("-"," ")
print(phone_number2) # 결과 : 010 1111 2222
# replace 함수를 사용하자.

'''url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요. 실행 예: kr [문자열 다루기]'''
url = "http://sharebook.kr"
# url_split = url.split(".") 
# print(url_split)                # 결과 : 'http://sharebook', 'kr'
# split함수는 정상적으로 작동하였지만 예시를 만족하지 못했다.

url_split = url.split(".")
print(url_split[-1]) # 결과 : kr
# 문자열.split(sep, maxsplit) 함수는 문자열을 maxsplit 횟수만큼 sep의 구분자를 기준으로 문자열을 구분하여 잘라서 리스트로 만든다.
# 리스트로 변경되었기에 print함수로 리스트로 변경된 url_split에서 'kr'만 출력하기 위해 -1을 입력해서 뒤에서부터 출력한다.
# 문자열.split() 처럼 공백으로 두면 띄어쓰기를 기준으로 한다.

'''아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요. [Replace 메서드]'''

string = 'abcdfe2a354a32a'
# print(string.replace(a,A))
print(string.replace('a','A')) # 결과 : Abcdfe2A354A32A
# 변경하려는 것이 a가 아닌 문자열 'a' 와 'A'라는 것을 기억하자. replace('대상문자', '바뀔문자')
# string의 값 자체는 변하지 않는다.

'''그렇다면 한 replace메서드에서 한번에 여러 문자열을 바꾸는 것도 가능한가?'''
# print(string.replace('a','A','b','B'))
# TypeError: replace expected at most 3 arguments, got 4 [에러발생]

'''아래 코드의 실행 결과는?'''

a = "3"
b = "4"
print(a + b)    # 결과 : 34
# 무의식적으로 7으로 예상했다. '"'를 사용했기 때문에 숫자이지만 문자열인것을 확인하자.

'''변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력.'''

name1 = "박동수" 
age1 = 10
name2 = "김현광"
age2 = 13
#이름: 박동수 나이: 10
#이름: 김현광 나이: 13

#print("이름 :" , name1, " 나이:", age1)
# 위 방식도 예시되로 출력되지만 %formatting을 사용하지 못했다.

print("이름: %s 나이: %d" % (name1, age1)) # 결과 : '이름: 박동수 나이: 10'
print("이름: %s 나이: %d" % (name2, age2)) # 결과 : '이름: 김현광 나이: 13'
#print 포맷팅에서 `%s`는 문자열 데이터 타입의 값을 `%d`는 정수형 데이터 타입 값의 출력을 의미

'''문자열의 format( ) 메서드를 사용해서 위 문제를 다시 풀어보자'''
print("이름: {} 나이: {}".format(name1, age1)) # 결과 : '이름: 박동수 나이: 10'
print("이름: {} 나이: {}".format(name2, age2)) # 결과 : '이름: 김현광 나이: 13'

'''f-string을 사용해서 위 문제를 다시 풀어보자'''
print(f"이름: {name1} 나이: {age1}") # 결과 : '이름: 박동수 나이: 10'
print(f"이름: {name2} 나이: {age2}") # 결과 : '이름: 김현광 나이: 13'

# f-string은 문자열 앞에 f가 붙은 형태.
# f-string을 사용하면 `{변수}`와 같은 형태로 문자열 사이에 타입과 상관없이 값을 출력.

'''삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환.'''

상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(",", "")
타입변환 = int(컴마제거)
print(타입변환, type(타입변환)) # 결과 : 5969782550 <class 'int'>

'''다음과 같은 문자열에서 '2020/03'만 출력'''

분기 = "2020/03(E) (IFRS연결)"
print(분기[0:7]) # 결과 : 2020/03     # print(분기[:7])도 가능하다.

'''문자열의 좌우의 공백이 있을 때 이를 제거.'''
data = "   삼성전자    " 
print(data.strip()) # 결과 : 삼성전자

# 문자열에서 strip( ) 메서드를 사용하면 좌우의 공백을 제거할 수 있다.
# 이때 '원본 문자열(data)'은 그대로 유지되고 공백이 제거된 새로운 문자열이 반환.
# data = "   삼성전자    "
# data1 = data.strip()
# print(data1)

'''다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경. [upper 메서드]'''

ticker = "btc_krw"
print(ticker.upper()) # 결과 : BTC_KRW
# upper()메서드는 모든 알파벳을 대문자로 변경

'''다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경. [lower 메서드]'''

ticker1 = "BTC_KRW"
print(ticker.lower()) # 결과 : btc_krw
# lower()메서드는 모든 알파벳을 소문자로 변경

'''문자열 'hello'가 있을 때 이를 'Hello'로 변경 [Capitalize 메서드]'''
Q043 = "hello"
print(Q043.capitalize()) # 결과 : Hello
# capitalize() 메서드는 맨 앞 알파벳을 대문자로 바꾼다.

'''파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인 [endswith메서드]''' 
file_name = "보고서.xlsx"
print(file_name.endswith('xlsx')) # 결과 : True
# file_nameendswith(value, start, end)
# [endswith 메서드의 매개변수]
# -value -> 필수. 체크할 '끝나는 값' 지정. (ex: 문자열, 문자, 숫자 등...)
# -start -> 선택. 검색 시작 위치 나타내는 정수. (기본값: 0)
# -end -> 선택. 검색 종료 위치 나타내는 정수. (기본값: 문자열 끝) 포함 X

''' endswith()메서드로 2개 이상의 문자열도 확인할수 있을까?'''
print(file_name.endswith(('xlsx','abcd'))) # 결과 : True
print(file_name.endswith(('abcd','xlsx'))) # 결과 : True
# 2개 이상의 문자열을 확인할 때는 괄호를 2개 사용해야 한다.
# 여러가지 매개변수 중에서 하나라도 포함되어 있으면 True값을 반환한다.

''' endswith()메서드 매개변수 전부 사용해서 결과확인해보기'''
print(file_name.endswith('x', 0, 3)) #결과 : False
print(file_name.endswith('x', 0, 5)) #결과 : True

# 'x'문자열은 4번째부터 존재하므로 검색 종료 위치가 3에서 끝나면 False값이 출력된다.
# 'x'문자열이 5번째까지 검색하므로 4번째에서 확인이 되어 True값이 출력된다.

'''파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인[startswith 메서드]'''
file_name1 = "2020_보고서.xlsx"
print(file_name1.startswith('2020')) # 결과 : True

# endswith()메서드와 비슷한 개념이다.

'''다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나누기 [split 메서드].'''

q47 = "hello world"
print(q47.split(" ")) # 결과 : ['hello', 'world']
# .split()으로 완전 공백으로 해도 띄어쓰기를 기준으로 문자열이 나눠진다.
# 리스트형으로 만든다.


'''문자열의 오른쪽에 공백이 있을 때 이를 제거.[rstrip 메서드]'''

q50 = "039490     "
print(q50.rstrip()) # 결과 : ['039490']




