# 1D1P Day312 Programmers 해쉬 1번 완주하지 못한 선수 문제 - 2021.09.12

def solution(participant, completion):
    players = dict()
    for part in participant:
        players[part] = players.get(part, 0) + 1
    
    for part in completion:
        players[part] -= 1
    
    answer = []
    for player in players:
        if players[player]:
            answer.append(player)
    
    return answer


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], 	["stanko", "ana", "mislav"]))