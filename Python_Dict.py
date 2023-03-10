
'''별 표현식
기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 한다
하지만 star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있다.
튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 나머지 데이터의 언패킹 코드를 작성할 필요가 없다.'''

# 설명 예시
a, b, *c = (0, 1, 2, 3, 4, 5)
>> a
>> 0
>> b
>> 1
>> c
[2, 3, 4, 5]

''' 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, star expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하기.'''

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

*valid_score, _, _= scores
print(valid_score)  # 결과 : [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5]
# '*'는 unpacking의 역할을 하며 리스트,튜플,string,딕셔너리 등 iterable 형태의 데이터 타입들은 다 가능.
# for 문을 돌렸을때 출력되는 형태는 전부 iterable 형태라고 보면 된다.
# '*'가 없는 변수가 값을 할당받은 후 할당받지 못한 나머지 값들을 모아서 리스트를 만든다.
# '*'는 한번밖에 사용하지 못한다.

''' temp 이름의 비어있는 딕셔너리를 만들기 '''
temp = { }

''' 아이스크림 딕셔너리 만들기 '''
ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
print(ice)  # 결과 : {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}

''' 아이스크림 가격정보를 추가 '''
ice["죠스바"] = 1200
ice["월드콘"] = 1500
print(ice) # 결과 : {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}

''' 메로나 가격을 출력 '''
ice["메로나"]  # 결과 : 1000

''' 메로나의 가격을 1300으로 수정 '''
ice["메로나"] = 1300 
print(ice) # 결과 : {'메로나': 1300, '폴라포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}

''' 메로나 삭제 '''
del ice["메로나"]
print(ice) # 결과 : {'폴라포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}

# 딕셔너리 삭제할 때 'del'함수를 쓴다.

''' 딕셔너리 예제 생성 '''
''' "아이스크림 : [가격, 재고]'''
inventory = {"메로나": [300, 20], 
             "비비빅": [400, 3], 
             "죠스바": [250, 100]}
print(inventory)

# 한 줄로 써도 상관없지만 보기 좋게 줄마다 작성해도 정상적으로 출력된다.

''' inventory 딕셔너리에서 메로나의 가격을 화면에 출력 '''
# 실행 예시: 300 원
print(inventory["메로나"][0], "원") # 결과 : 300 원

''' inventory 딕셔너리에서 메로나의 재고를 화면에 출력 '''
# 실행 예시: 20 개
print(inventory["메로나"][1], "개")  # 결과 : 20 개

''' inventory 딕셔너리에 데이터 추가 '''
inventory["월드콘"] = [500,7]
print(inventory)  # 결과 : {'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100], '월드콘': [500, 7]}

''' 다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성 [key()메서드] '''

icecream2 = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream2keys = list(icecream2.keys())
print(icecream2keys) # 결과 : ['탱크보이', '폴라포', '빵빠레', '월드콘', '메로나']

''' values 값으로만 구성된 리스트를 생성 [value()메서드]'''

icecream2value = list(icecream2.values())
# value메서드 쓸 때 'value'가 아닌 'values'라고 입력해야 되나보다.
print(icecream2value) # 결과 : [1200, 1200, 1800, 1500, 1000]

''' 아이스크림 판매 금액의 총합을 출력 '''
print(sum(icecream2.values()))  # 결과 : 6700

''' 아래의 new_product 딕셔너리를 위의 icecream2 딕셔너리에 추가 [update메서드]'''

new_product = {'팥빙수':2700, '아맛나':1000}
# 실행 예시:
# >> print(icecream)
# {'탱크보이': 1200,  '폴라포': 1200,  '빵빠레': 1800,  '월드콘': 1500,  '메로나': 1000,  '팥빙수':2700, '아맛나':1000}

icecream2.update(new_product)
print(icecream2) # 결과 : {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000, '팥빙수': 2700, '아맛나': 1000}

''' 아래 두 개의 튜플을 하나의 딕셔너리로 변환. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장 [zip,dict]'''

# 실행 예시:
# >> print(result)
# {'apple': 300, 'pear': 250, 'peach': 400}

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

result = zip(keys,vals)
print(result) # 결과 : {'apple': 300, 'pear': 250, 'peach': 400}

'''date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성'''
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date, close_price))
print(close_table)  # 결과 : {'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}

