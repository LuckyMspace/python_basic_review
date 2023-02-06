# 파이썬 리스트

'''영화 제목을 movie_rank 이름의 리스트에 저장''' 
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank) # 결과 : ['닥터 스트레인지', '스플릿', '럭키']

'''movie_rank 리스트에 "배트맨"을 추가 [list.append 메서드]'''
movie_rank.append("배트맨")
print(movie_rank) # 결과 : ['닥터 스트레인지', '스플릿', '럭키', '배트맨']

'''movie_rank 리스트에 "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가 [list.insert메서드]'''
movie_rank.insert(1, "슈퍼맨")
print(movie_rank) # 결과 : ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
#list.insert(integar, "arguments")   몇번 째 자리에 삽입할 것인지 integar값을 넣고, 추가할 매개변수를 넣는다.

'''movie_rank 리스트에서 '럭키'를 삭제 [del 함수]'''
del movie_rank[3]
print(movie_rank) # 결과 : ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# '럭키'가 3번째에 있으므로 integar값을 3으로 입력하여 리스트 'movie_rank'의 3번째 값을 삭제

'''movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제'''
# del movie_rank[4,5]
# print(movie_rank) # 결과 : 오류 발생
# del을 이용하여 리스트에서 원소를 삭제할 수 있다. 리스트에서 어떤 값을 삭제하면 남은 값들은 새로 인덱싱된다.
# 따라서 여러 값을 삭제할 때는 어떤 값이 먼저 삭제된 후 남은 원소들에 대해서 순서를 새로 고려한 후 삭제.

del movie_rank[2]
del movie_rank[2]
print(movie_rank) # 결과 : ['닥터 스트레인지', '슈퍼맨']

'''lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들기'''

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang1 + lang2
print(langs) # 결과 : ['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']

'''다음 리스트에서 최댓값과 최솟값을 출력. (힌트: min(), max() 함수 사용)'''

nums = [1, 2, 3, 4, 5, 6, 7]
'''실행 예:
max:  7
min:  1     '''

print("max: ", max(nums)) # 결과 : max: 7
print("min: ", min(nums)) # 결과 : min: 1

'''다음 리스트의 합을 출력'''

q58 = [1, 2, 3, 4, 5]
print(sum(q58)) # 결과 : 15

'''다음 리스트에 저장된 데이터의 개수 구하기'''

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]

print(len(cook)) # 결과 : 12

'''다음 리스트의 평균을 출력. '''

q60 = [1, 2, 3, 4, 5]
print(average(q60))
average = sum(q60) / len(q60)
print(average) # 결과 : 3.0

# 정수로 표현하고 싶을 때
print(int(average))