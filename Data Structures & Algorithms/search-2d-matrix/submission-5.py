class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def BS(ans):
            l,r = 0,len(ans)-1
            while l <= r:
                mid = l + (r-l)//2
                if ans[mid] == target:
                    return True
                elif ans[mid] > target:
                    r = mid - 1
                elif ans[mid] < target:
                    l = mid + 1
            return False
  
        ans=[]
        for i in matrix:
            if target > i[-1]:
                continue
            elif target < i[-1]:
                v=BS(i)
                print(f'v : {v}')
                if v == True:
                    return True
            elif target == i[-1]:
                return True

        return False

        