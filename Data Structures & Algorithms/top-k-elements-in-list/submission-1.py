class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        list1 = []
        for i in range(0,k):
            #list(hashmap.values())
            max_key = max(hashmap, key=hashmap.get)
            list1.append(max_key)
            hashmap[max_key] = 0
        return list1
            
            
            


        