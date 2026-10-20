class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur=0
        start=0
        if sum(gas)<sum(cost):
            return -1
        for i in range(len(gas)):
            cur+=gas[i]-cost[i]
            if cur<0:
                cur=0
                start=i+1
        return start
        