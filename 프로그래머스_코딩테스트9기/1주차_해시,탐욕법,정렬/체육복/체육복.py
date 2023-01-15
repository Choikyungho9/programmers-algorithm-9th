n = 5
lost = [2, 4]
reserve = [1, 3, 5]

def solution(n, lost, reserve):
    u = [1] * (n+2)
    for i in reserve:
        u[i] += 1


    for i in lost:
        u[i] -= 1



    for i in range(1, n+1):
        if u[i-1] == 0 and u[i] == 2:   # 앞사람이 0이고 내가 2개 들고 있으면,,

            u[i-1 : i+1] = [1, 1]       # i-1번 원소와 i번 원소를 1로 만든다. ~까지이므로 +1 해줘야함.


        elif u[i] == 2 and u[i + 1] == 0:   # 뒷사람을 체크해서
            print('ok')
            u[i : i+2] = [1, 1]             # 나와 뒷사람을 1, 1 로 만든다.

    return print(len([x for x in u[1:-1] if x > 0])) # 리스트 컨프리헨션으로 1번째 idx부터 끝에서 2번째까지 돌면서 len을 센다)

solution(n, lost, reserve)