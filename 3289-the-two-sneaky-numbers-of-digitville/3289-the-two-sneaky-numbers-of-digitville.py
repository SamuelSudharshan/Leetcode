class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        '''return multimode(nums)'''
        map={}
        ls=[]
        for i in nums:
            map[i]=map.get(i,0)+1
            if map[i] == 2:
                ls.append(i)
        return ls
        