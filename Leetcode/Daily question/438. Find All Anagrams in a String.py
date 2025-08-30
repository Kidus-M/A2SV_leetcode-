class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dictionary = {}
        for i in p:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        start = 0
        end = 0
        result = []

        # print(dictionary)
        while end < len(s):
            if s[end] in dictionary and dictionary[s[end]] > 0:
                dictionary[s[end]] -= 1
                end += 1
                if end - start == len(p):
                    result.append(start)
            elif start == end:
                start += 1
                end += 1
            else:
                dictionary[s[start]] += 1
                start += 1
        return result