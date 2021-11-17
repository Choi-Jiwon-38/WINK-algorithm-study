def solution(prices):
    answer = [0] * len(prices) # answer 요소들의 초기값을 0으로 설정
    for i in range(len(prices)): # i와
        for j in range(i + 1, len(prices)): # i보다 하나 뒤에 있는 인덱스 j와 비교
            if prices[i] <= prices[j]: # 가격이 안떨어지고 있는 경우에 answer에 +1``
                answer[i] += 1
            else: 
                answer[i] += 1 # 가격이 떨어진 경우 break를 통해 탈출
                break

    return answer