class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ans=[]
        for i in matrix:
            ans.extend(i)
        print(ans)
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
        return BS(ans)

        