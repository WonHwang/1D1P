# 1D1P Day372 BOJ 4732번 조옮김 문제 - 2021.11.11

pitch = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
samepitch = {
    'Ab': 'G#',
    'Bb': 'A#',
    'Db': 'C#',
    'Eb': 'D#',
    'Gb': 'F#',
    'E#': 'F',
    'B#': 'C'
}

while True:
    input_ = input()
    if input_ == '***':
        break
    target = list(input_.split())
    transpose = int(input())
    answer = []

    for note in target:
        if note in samepitch:
            note = samepitch[note]
        idx = pitch.index(note)
        answer.append(pitch[(idx+transpose) % 12])

    print(*answer)