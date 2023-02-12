'''for문의 실행결과를 예측'''

과일 = ["사과", "귤", "수박"]
for variables in 과일:
    print(variables)

# 과일 리스트에 있는 데이터가 순서대로 출력


''' 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 for 문을 사용해서 화면에 출력. 단 부가세는 10원으로 가정.'''

q141 = [100, 200, 300]
for variables in q141:
    print(variables + 10)

# 결과 : 정상작동

''' for 문을 사용해서 리스트에 저장된 값을 출력'''

q142 = ["김밥", "라면", "튀김"]
for variables in q142:
    print(variables)

''' 리스트에 주식 종목이름이 저장돼 있다. 저장된 문자열의 길이를 출력.'''

q143 = ["SK하이닉스", "삼성전자", "LG전자"]
for stocks in q143:
    print(len(stocks))

# 결과 : 정상작동
# for문 끝에 ':' 반드시 붙여야함.

''' 리스트에는 동물이름이 문자열로 저장돼 있다. 동물 이름과 글자수를 출력.'''

q144 = ['dog', 'cat', 'parrot']
for animals in q144:
    print(animals, len(animals))

# 결과 : 정상작동

'''리스트에 동물 이름 저장돼 있다. for문을 사용해서 동물 이름의 첫 글자만 출력. '''

q145 = ['dog', 'cat', 'parrot']
for animals in q145:
    print(animals[0])

# 결과 : 정상작동

''' 리스트에는 세 개의 숫자가 바인딩. for문을 사용해서 다음과 같이 출력.'''
q146 = [1, 2, 3]

'''
3 x 1
3 x 2
3 x 3'''

for multiply in q146:
    print("3 x",multiply)

# 결과 : 정상작동

''' q146 리스트에서 for문을 사용해서 다음과 같이 출력.'''
'''
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9'''

for multiply in q146:
    print("3 x", multiply, "=", multiply * 3)

# q146은 위에 정의 되어있음.
# 결과 : 정상작동

''' 리스트에는 네 개의 문자열이 바인딩 되어있음. for문을 사용해서 다음과 같이 출력. '''
q148 = ["가", "나", "다", "라"]

'''
나
다
라'''
for hangle in q148[1:]:
    print(hangle)
# 결과 : 정상작동

''' q148 리스트를 활용하여 for문을 사용해 다음과 같이 출력. '''
'''
가
다'''
for hangle in q148[0::2]:
    print(hangle)
# 결과 : 정상작동

''' q148 리스트를 활용하여 for문을 사용해 다음과 같이 출력. '''

'''라
다
나
가'''
for hangle in q148[::-1]:
    print(hangle)
# 결과 : 정상작동

''' 리스트에는 네 개의 정수가 저장. for문을 사용해서 리스트의 음수를 출력. '''

q151 = [3, -20, -3, 44]
for minus in q151:
    if minus < 0:
        print(minus)
# 결과 : 정상작동
# 들여쓰기에 유의하자. for문에 들여쓰기 되어있는 if문을 반복한다. if문이 반복되어 변수(minus)를 출력.


''' for문을 사용해서 3의 배수만을 출력 '''

q152 = [3, 100, 23, 44]
for multiply3 in q152:
    if multiply3 % 3 == 0:
        print(multiply3)
# 결과 : 정상작동

''' 20 보다 작은 3의 배수를 출력 '''

q153 = [13, 21, 12, 14, 30, 18]
for lowermulti3 in q153:
    if lowermulti3 < 20 and lowermulti3 % 3 == 0:
        print(lowermulti3)
# 결과 : 정상작동
# 나머지가 0이어야 되니 % 사용.

''' 리스트 q154에서 세 글자 이상의 문자를 화면에 출력.'''

q154 = ["I", "study", "python", "language", "!"]
for more3str in q154:
    if len(more3str) >= 3:
        print(more3str)
# 결과 : 정상작동

''' q155에서 대문자만 화면에 출력. '''

q155 = ["A", "b", "c", "D"]
for onlyupper in q155:
    if onlyupper.isupper() == True:
        print(onlyupper)

# 결과 : 정상작동
# if문에서 ' == Ture' 값을 생략해도 상관이 없다.

''' q157리스트의 첫 글자를 대문자로 변경해서 출력. '''

q157 = ['dog', 'cat', 'parrot']
for animals in q157:
    print(animals.capitalize())

# 결과 : 정상작동 
# upper 메서드를 사용해서 바꾼다면?

for animals in q157:
    print(animals[0].upper() + animals[1:])

# 결과 : 정상작동
# 변수 'animals'의 첫번째 글자를 .upper메서드로 대문자로 바꾸고 'animals'의 나머지문자열을 [1]번부터 끝까지 출력하는 방식.

''' 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력. (힌트: split() 메서드) '''

q158 = ['hello.py', 'ex01.py', 'intro.hwp']
for filename in q158:
    print(filename.split("."))

# 여기까지만 하면 split되어서 "."을 기준으로 나눠진 파일명과 확장자가 전부 출력된다.

for filename in q158:
    print(filename.split(".")[0])

# 결과 : 정상작동

''' 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라 '''

q159 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for extension in q159:
    if extension.split(".")[1] == "h":
        print(extension.split(".")[0])

# 결과 : 정상작동
# 답안비교
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
  split = 변수.split(".")
  if split[1] == "h":
    print(변수)

# 내가 작성한 코드가 답안보다 간결한 것 같은데 정상작동 되는 경우가 처음이라서 답안을 비교함.
# 내가 작성한 코드에 맹점이 있는 가능성이 있을 수 있지만 아직은 모르겠음.

''' 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력. '''
q160 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for extension_2 in q160:
    if extension_2.split(".")[1] == "h" or "c":
        print(extension_2)

# 이렇게 작성하며 작동은 되지만 문제에 맞는 답이 출력되지 않고 전부 출력되어버린다.
# if extension_2.split(".")[1] == "h" or "c":   이 코드는 if True or extension.split(".")[1] == "h":  와 다를 바가 없다.
# 그래서 첫번째 코드는 언제나 실행되어서 모든 리스트 원소를 출력하는 결과가 나와버린 것이다.

q160 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for extension_2 in q160:
    if extension_2.split(".")[1] == "h" or extension_2.split(".")[1] == "c":
        print(extension_2)

# 결과 : 정상출력

''' for문과 range 구문을 사용해서 0~99까지 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성. '''
for numbers in range(0,100):
    print(numbers)

# 결과 : 정상출력

''' 월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력'''
for wolrdcup in range(2002,2051,4):
    print(worldcup)
# 결과 : 정상출력

''' 1부터 30까지의 숫자 중 3의 배수를 출력 '''
for multi3 in range(3,31,3):
    print(multi3)
# 결과 : 정상출력

''' 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력'''
for reduce1 in range(100,0,-1):
    print(reduce1)
# 결과 : 정상출력
# 답안 : 
for i in range(100):
    print(99 - i)

''' 구구단 3단을 출력. 단 홀수 번째만 출력. '''
for gugudan in range(1,10,2):
    print("3 x" , gugudan, "=",3 * gugudan)

# 결과 : 정상작동

''' 1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성 '''
number = 0
for ds in range(1,11):
    number += ds
print(number)

# 결과 : 정상작동

''' 1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성 '''
number = 0
for holsu in range(1,11):
    if holsu % 2 != 0:
        number += holsu
print(number)

# 결과 : 정상작동
# 답안 :
hab = 0
for i in range(1, 11, 2):
    hab += i
print ("합 :", hab)

# 답안은 range 함수에서 증가폭을 2로 설정하여 1부터 2씩 더해나가서 홀수만 범위를 잡게 설정함.
# for문에 따라서 0으로 바인딩 된 hab에 홀수인 변수(i)가 10까지 합산을 반복한다.
 
''' 1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성 '''




    