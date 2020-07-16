class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringLength = len(s)
        maxSubStringLen = 0

        if (stringLength == 0):
            return maxSubStringLen
        
        # for a in s:
        for a in range(stringLength):
            # print(s[a], end = '')
            # print(s[a])
            subStringLen = 1
            for b in range(a + 1, stringLength):
                # print(f"sub: {s[b]}")
                # if (s[a] != s[b]):
                if (s[b] not in s[a:b]):
                    # print(f"looking for {s[b]} in {s[:b]}")
                    subStringLen += 1
                else:
                    break
            if (subStringLen > maxSubStringLen):
                maxSubStringLen = subStringLen 
        print('')

        return maxSubStringLen

s = Solution()
returnValue = s.lengthOfLongestSubstring("blah")
print("Your number is: " + str(returnValue))
returnValue = s.lengthOfLongestSubstring("abcabcbb")
print("Your number is: " + str(returnValue))
returnValue = s.lengthOfLongestSubstring("bbbbb")
print("Your number is: " + str(returnValue))
returnValue = s.lengthOfLongestSubstring("pwwkew")
print("Your number is: " + str(returnValue))
returnValue = s.lengthOfLongestSubstring("dvdf")
print("Your number is: " + str(returnValue))
