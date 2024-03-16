A_grade = input()
A_grade = list(map(int, A_grade.split()))
A_math_grade, A_eng_grade = A_grade[0], A_grade[1]

B_grade = input()
B_grade = list(map(int, B_grade.split()))
B_math_grade, B_eng_grade = B_grade[0], B_grade[1]

if A_math_grade > B_math_grade and A_eng_grade > B_eng_grade:
    print(1)