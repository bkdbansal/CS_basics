"""
LeetCode 826. Most Profit Assigning Work

We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is the profit of the ith job. 

Now we have some workers. worker[i] is the ability of the ith worker, which means that this worker can only complete a job with difficulty at most worker[i]. 

Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.

What is the most profit we can make?

Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100 
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.
Notes:

1 <= difficulty.length = profit.length <= 10000
1 <= worker.length <= 10000
difficulty[i], profit[i], worker[i]  are in range [1, 10^5]
"""

# V0

# V1 
# https://www.jiuzhang.com/solution/most-profit-assigning-work/#tag-highlight-lang-python
# IDEA : GREEDY 
class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted([a, b] for a, b in zip(difficulty, profit))
        res = i = maxp = 0
        for ability in sorted(worker):
            while i < len(jobs) and ability >= jobs[i][0]:
                maxp = max(jobs[i][1], maxp)
                i += 1
            res += maxp
        return res   

# V1'
# http://bookshadow.com/weblog/2018/04/29/leetcode-most-profit-assigning-work/
# IDEA : GREEDY
import collections
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        diffPro = collections.defaultdict(int)
        for diff, pro in zip(difficulty, profit):
            diffPro[diff] = max(diffPro[diff], pro)
        maxVal = 0
        for x in range(min(difficulty + worker), max(difficulty + worker) + 1):
            diffPro[x] = max(diffPro[x], maxVal)
            maxVal = max(diffPro[x], maxVal)
        return sum(diffPro[w] for w in worker)

# V2 
# Time:  O(mlogm + nlogn), m is the number of workers,
#                        , n is the number of jobs
# Space: O(n)
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = list(zip(difficulty, profit))
        jobs.sort()
        worker.sort()
        result, i, max_profit = 0, 0, 0
        for ability in worker:
            while i < len(jobs) and jobs[i][0] <= ability:
                max_profit = max(max_profit, jobs[i][1])
                i += 1
            result += max_profit
        return result
