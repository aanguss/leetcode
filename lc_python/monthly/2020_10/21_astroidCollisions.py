# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3502/
# https://leetcode.com/problems/asteroid-collision/
#
# We are given an array asteroids of integers representing asteroids in a row.
#
# For each asteroid, the absolute value represents its size, and the sign represents 
# its direction (positive meaning right, negative meaning left). Each asteroid moves 
# at the same speed.
#
# Find out the state of the asteroids after all collisions. If two asteroids meet, 
# the smaller one will explode. If both are the same size, both will explode. Two 
# asteroids moving in the same direction will never meet.
#
# Example 1:
#     Input: asteroids = [5,10,-5]
#     Output: [5,10]
#     Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
# Example 2:
#     Input: asteroids = [8,-8]
#     Output: []
#     Explanation: The 8 and -8 collide exploding each other.
# Example 3:
#     Input: asteroids = [10,2,-5]
#     Output: [10]
#     Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
# Example 4:
#     Input: asteroids = [-2,-1,1,2]
#     Output: [-2,-1,1,2]
#     Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right. 
#         Asteroids moving the same direction never meet, so no asteroids will meet each other.
# Constraints:
#     1 <= asteroids <= 104
#     -1000 <= asteroids[i] <= 1000
#     asteroids[i] != 0
from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        debug = True
        if asteroids is None or len(asteroids) == 0:
            return []
        extraStep = False
        for i in range(len(asteroids)-2, -1, -1):
            if debug: print(i)
            if debug: print(asteroids)
            if extraStep:
                if debug: print('found extra step')
                extraStep = False
            else:
                while i+1<len(asteroids) and asteroids[i] > 0 and asteroids [i+1] < 0:
                    if debug: print('found em')
                    if asteroids[i] > (-1 * asteroids[i+1]):
                        asteroids.pop(i+1)
                        if debug: print('popping i+1 =', i+1)
                        if debug: print(asteroids)
                    elif asteroids[i] < (-1 * asteroids[i+1]):
                        asteroids.pop(i)
                        if debug: print('popping i =', i)
                        if debug: print(asteroids)
                    else:
                        asteroids.pop(i+1)
                        asteroids.pop(i)
                        if debug: print('popping both i+1 and i = ', i)
                        if debug: print(asteroids)
                        # extraStep = True
        return asteroids


s = Solution()
# input_val = [5,10,-5]
# solution = [5,10]
# output = s.asteroidCollision(input_val)
# print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

# input_val = [8,-8]
# solution = []
# output = s.asteroidCollision(input_val)
# print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

# input_val = [10,2,-5]
# solution = [10]
# output = s.asteroidCollision(input_val)
# print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

# input_val = [-2,-1,1,2]
# solution = [-2,-1,1,2]
# output = s.asteroidCollision(input_val)
# print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

input_val = [-2,1,1,-1]
solution = [-2]
output = s.asteroidCollision(input_val)
print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

# input_val = [-2,2,-1,-2]
# solution = [-2]
# output = s.asteroidCollision(input_val)
# print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

# input_val = [1,1,-1,-2]
# solution = [-2]
# output = s.asteroidCollision(input_val)
# print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))
