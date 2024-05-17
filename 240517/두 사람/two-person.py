# 입력을 공백으로 구분하여 받기
first_person_input_list = input().split()
second_person_input_list = input().split()

# 나이와 성별 정보를 각각 변수에 저장
first_person_age = int(first_person_input_list[0])
first_person_sex = first_person_input_list[1]

second_person_age = int(second_person_input_list[0])
second_person_sex = second_person_input_list[1]

# 조건문을 통해 결과 출력
if ((first_person_age >=19 and first_person_sex == "M") or 
    (second_person_age >= 19 and first_person_sex == "M")):
    print(1)
else:
    print(0)