"""
Title : Course Schedule
Link : https://leetcode.com/problems/course-schedule/
"""

from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_before = [0] * numCourses
        course = {x: [] for x in range(numCourses)}
        for a, b in prerequisites:
            course_before[b] += 1
            course[a].append(b)
        queue = deque()
        for i, c in enumerate(course_before):
            if not c:
                queue.append(i)
        check = [False] * numCourses
        while queue:
            x = queue.popleft()
            check[x] = True
            for y in course[x]:
                course_before[y] -= 1
                if not course_before[y]:
                    queue.append(y)
        if all(check):
            return True
        return False


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0]]

    solution = Solution()
    print(solution.canFinish(numCourses, prerequisites))
