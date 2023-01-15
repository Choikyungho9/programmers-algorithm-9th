number = "1924"; k = 2
number = "1231234"; k = 3
number = "4177252841"; k = 4


def solution(number, k):
    collected = []
    for i, num in enumerate(number):
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k-=1
        collected.append(num)

    collected = collected[:-k] if k>0 else collected
    answer = ''.join(collected)
    #print(answer)
    return answer

solution(number, k)