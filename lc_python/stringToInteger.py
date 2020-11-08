# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2962/

# Implement atoi which converts a string to an integer.

# The function first discards as many whitespace characters as necessary until 
# the first non-whitespace character is found. Then, starting from this character 
# takes an optional initial plus or minus sign followed by as many numerical 
# digits as possible, and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral 
# number, which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral 
# number, or if no such sequence exists because either str is empty or it contains 
# only whitespace characters, no conversion is performed.

# If no valid conversion could be performed, a zero value is returned.

# Note:
# Only the space character ' ' is considered a whitespace character.
# Assume we are dealing with an environment that could only store integers within 
# the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out 
# of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

# Example 1:
#     Input: str = "42"
#     Output: 42
# Example 2:
#     Input: str = "   -42"
#     Output: -42
#     Explanation: The first non-whitespace character is '-', which is the minus sign. 
#         Then take as many numerical digits as possible, which gets 42.
# Example 3:
#     Input: str = "4193 with words"
#     Output: 4193
#     Explanation: Conversion stops at digit '3' as the next character is not a numerical 
#         digit.
# Example 4:
#     Input: str = "words and 987"
#     Output: 0
#     Explanation: The first non-whitespace character is 'w', which is not a numerical 
#         digit or a +/- sign. Therefore no valid conversion could be performed.
# Example 5:
#     Input: str = "-91283472332"
#     Output: -2147483648
#     Explanation: The number "-91283472332" is out of the range of a 32-bit signed 
#         integer. Thefore INT_MIN (−2^31) is returned.
# Constraints:
#     0 <= s.length <= 200
#     s consists of English letters (lower-case and upper-case), digits, ' ', '+', '-' and '.'.
#
from typing import List
class Solution:
    def myAtoi(self, s: str) -> int:
        debug = False
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if debug: print(INT_MIN)
        if debug: print(INT_MAX)
        sNum = ''
        num = 0
        negNum = False
        digits = ['0','1','2','3','4','5','6','7','8','9']
        
        words = s.replace(' ', ',').split(',')
        if debug: print('words =',words)
        for w in words:
            if debug: print(w)
            if debug: print(w[0])
            if w == '':
                continue
            elif len(w) >=1 and w[0] in digits:
                if debug: print(w)
                sNum = w
                break
            elif len(w) >= 2 and w[0] == '-' and w[1] in digits:
                negNum = True
                sNum = w[1:]
                break
            elif len(w) >= 2 and w[0] == '+' and w[1] in digits:
                sNum = w[1:]
                break
            else:
                break
        if debug: print(sNum)
        if sNum != '':
            if debug: print('no blank value')
            decIndex = sNum.find(".")
            if decIndex != -1:
                sNum = sNum[:decIndex]
                
            pos = 0
            if debug: print(sNum)
            for i in range(len(sNum)-1,-1,-1):
                if debug: print('sNum[i]=',sNum[i])
                if debug: print('index=',digits.index(sNum[i]))
                if debug: print (10**pos)
                val = ((10**pos) * digits.index(sNum[i]))
                num += val
                if debug: print('pos*10=',(10**pos))
                if debug: print('val=',val)
                if debug: print('num=',num)
                pos += 1
            if negNum:
                num *= -1
            if debug: print(num)
            if num < INT_MIN:
                num = INT_MIN
            elif num > INT_MAX:
                num = INT_MAX
        else:
            num = 0
        
        return num

s = Solution()
# string = "42"
# solution = 42
# output = s.myAtoi(string)
# print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

# string = "   -42"
# solution = -42
# output = s.myAtoi(string)
# print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

# string = "4193 with words"
# solution = 4193
# output = s.myAtoi(string)
# print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

# string = "words and 987"
# solution = 0
# output = s.myAtoi(string)
# print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

# string = "-91283472332"
# solution = (-2**31)
# output = s.myAtoi(string)
# print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

# string = "3.14159"
# solution = 3
# output = s.myAtoi(string)
# print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

string = "1"
solution = 1
output = s.myAtoi(string)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))

string = "+1"
solution = 1
output = s.myAtoi(string)
print("%s | %s" % ("PASS" if output == solution else "FAIL", output))