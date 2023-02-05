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
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

