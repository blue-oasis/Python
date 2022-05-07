def solution(queue1, queue2):
    answer = -2
    q_answer = sum(queue1) + sum(queue2)
    q_answer /= 2
    q_answer = int(q_answer)
    print(q_answer)
    if q_answer % 2 == 1:
        answer = -1

    return answer


solution([1, 2], [7, 4])

a = [1, 2, 3]
print(a.pop())
print(a)
a.insert(len(a), 5)
print(a)