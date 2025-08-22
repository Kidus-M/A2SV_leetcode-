class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic={}
        ans=[]
        for i in nums:
            if i not in dic:
                dic[i]=0
            dic[i] += 1
        for i in dic.keys():
            if dic[i] == 1:
                ans.append(i)

        return ans