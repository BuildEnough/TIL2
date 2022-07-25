# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for i in range(len(numbers)): 
    
        for j in range(i+1,len(numbers)): 
        
            if numbers[i] + numbers[j] not in answer:
            
                answer.append(numbers[i] + numbers[j])
            
                answer.sort()
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
