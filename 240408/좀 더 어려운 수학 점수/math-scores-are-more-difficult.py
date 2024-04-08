grade_input_A = input()
grade_input_B = input()

grade_A = [int(num) for num in grade_input_A.split()]
grade_B = [int(num) for num in grade_input_B.split()]

math_A, eng_A = grade_A[0:2]
math_B, eng_B= grade_B[0:2]

if math_A > math_B:
    print("A")
elif math_A < math_B:
    print("B")
elif math_A == math_B:
    if eng_A > eng_B:
        print("A")
    else:
        print("B")