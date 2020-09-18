# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3463/
# On an infinite plane, a robot initially stands at(0, 0) and faces north.  
# The robot can receive one of three instructions:
#
# "G": go straight 1 unit
# "L": turn 90 degrees to the left
# "R": turn 90 degress to the right.
# The robot performs the instructions given in order, and repeats them forever.
#
# Return true if and only if there exists a circle in the plane such that the 
# robot never leaves the circle.
#
# Example 1:
# Input: "GGLLGG"
# Output: true
# Explanation:
# The robot moves from (0, 0) to(0, 2), turns 180 degrees, and then returns to(0, 0).
# When repeating these instructions, the robot remains in the circle of radius 2 
# centered at the origin.
#
# Example 2:
# Input: "GG"
# Output: false
# Explanation:
# The robot moves north indefinitely.
#
# Example 3:
# Input: "GL"
# Output: true
# Explanation:
# The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
#
# Note:
# 1 <= instructions.length <= 100
# instructions[i] is in {'G', 'L', 'R'}
class Solution:
    def isRobotBounded(self, instructions: str, debug: bool) -> bool:
        robotBound = False
        firstLocation = True
        originFound = 0
        location = [0, 0]
        direction = ['north', 'east', 'south', 'west']
        facing = 0
        iteration = 0
        iterations = 7

        while robotBound == False and iteration < iterations:
            for i in range(len(instructions)):
                if firstLocation:
                    not firstLocation
                if instructions[i] == 'G':
                    if direction[facing] == 'north':
                        location[1] += 1
                    elif direction[facing] == 'south':
                        location[1] -= 1
                    elif direction[facing] == 'east':
                        location[0] += 1
                    elif direction[facing] == 'west':
                        location[0] -= 1
                    else:
                        print("%s is not a valid direction" % direction[facing])
                elif instructions[i] == 'L':
                    facing -= 1
                    if facing == -1:
                        facing = 3
                elif instructions[i] == 'R':
                    facing += 1
                    if facing == 4:
                        facing = 0
                else:
                    print("%s is not a valid instruction" % instructions[i])
                
                if debug: 
                    print('locaton = [%s, %s]' % (location[0], location[1]))

                if not firstLocation and location[0] == 0 and location[1] == 0:
                    originFound += 1
                    if originFound > 1 and iterations > 1:
                        robotBound = True
                        break
            if debug: print('end locaton = [%s, %s]' % (location[0], location[1]))
            if location[0] == 0 and location[1] == 0:
                robotBound = True
                break
            iteration += 1
        
        return robotBound

s = Solution()
input = "GGLLGG"
solution = True
output = s.isRobotBounded(input, False)
print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

input = "GG"
solution = False
output = s.isRobotBounded(input, False)
print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

input = "GL"
solution = True
output = s.isRobotBounded(input, False)
print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

input = "LRRRRLLLRL"
solution = True
output = s.isRobotBounded(input, False)
print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

input = "GLGLGGLGL"
solution = False
output = s.isRobotBounded(input, False)
print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

input = "RRGRRGLLLRLGGLGLLGRLRLGLRLRRGLGGLLRRRLRLRLLGRGLGRRRGRLG"
solution = False
output = s.isRobotBounded(input, False)
print("%s | %s" % ('PASS' if (output == solution) else 'FAIL', output))

