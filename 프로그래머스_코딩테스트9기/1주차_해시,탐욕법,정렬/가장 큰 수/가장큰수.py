numbers = [6,10,2]
#numbers = [3,30,34,5,9]

def solution(numbers):
    numbers = [str(x) for x in numbers]
    # x를 4번 반복하고 4까지 끊는다
    numbers.sort(key=lambda x: (x*4)[:4], reverse=True)
    if numbers[0]=='0':
        answer = '0'
    else:
        answer = ''.join(numbers)

    return answer


solution(numbers)