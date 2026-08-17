class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        answer = 0
        cur_sum = sum(arr[:k])
        looking_for_sum = threshold * k

        if cur_sum >= looking_for_sum:
            answer +=1
        for i in range(k,len(arr)):
            cur_sum += arr[i]
            cur_sum -= arr[i-k]
            if cur_sum >= looking_for_sum:
                answer +=1
       

        return answer
