# 이름이 주어지면 몇 번이나 됬는지 기록해야한다.
# 배열 인덱스 / 문자열로 찾아가는 것 -> 해시 (Hash)
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

def solution(participant, completion):
    d = {}  # 빈 딕셔너리 사전
    for x in participant:
        d[x] = d.get(x, 0) + 1  # 딕셔너리에 x가 존재하면 그 값을 / 아니면 0을 반환
                                # 처음 등장하면 1, 처음 등장하지 않으면 원래 개수 + 1을 더한다.
        print(d)

    for x in completion:
        d[x] -= 1               # 이름이 3명 있었으면, completion에 등장하면 1씩 빠진다.

    # did not finish 배열
    dnf = [k for k, v in d.items() if v > 0 ]   # 이해했다. d
    print(dnf)

    answer = dnf[0] # 한명이 완주하지 못했으므로 1번째 배열에는 1명만 남는다.


    return print(answer)

solution(participant, completion)