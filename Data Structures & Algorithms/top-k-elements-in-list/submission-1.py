class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_a = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for num in nums:
            dict_a[num] = 1 + dict_a.get(num, 0)
        
        for key, value in dict_a.items():
            frequency[value].append(key)
        
        res = []
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                res.append(num)
                if len(res) == k:
                    return res

        print(dict_a)
