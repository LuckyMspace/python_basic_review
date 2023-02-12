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

