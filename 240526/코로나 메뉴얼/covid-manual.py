person_a = input()
person_b = input()
person_c = input()

person_a_symptom, person_a_temperature = person_a.split()
person_b_symptom, person_b_temperature = person_b.split()
person_c_symptom, person_c_temperature = person_c.split()

def symptom_checker(symptom, temperature):
    assert int(temperature) >= 0 and int(temperature) <= 40, "정상적인 체온 input이 아닙니다."

    if symptom == 'Y':
        if int(temperature) >= 37:
            state = 'A'
            return state
        elif int(temperature) == 37:
            state = 'C'
            return state
    elif symptom == "N":
        if int(temperature) >= 37:
            state = 'B'
            return state
        elif int(temperature) == 37:
            state = 'D'
            return state


person_a_state = symptom_checker(person_a_symptom, person_a_temperature)
person_b_state = symptom_checker(person_b_symptom, person_b_temperature)
person_c_state = symptom_checker(person_c_symptom, person_c_temperature)

state_list = [person_a_state, person_b_state, person_c_state]

if state_list.count('A') >= 2:
    print("E")
else:
    print("N")