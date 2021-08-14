def solution(name_list):

    name_dict = {}
    answer = []

    for name in name_list:
        name_dict[name] = name_dict.get(name, 0) + 1

        answer.append(name + chr(name_dict[name] + ord('A') - 1))

    return answer

print(solution(["김비바", "김비바", "이비바", "김토스", "이비바", "김비바"]))