class Solution(object):
    def numWays(self, n):
        if n in (0,1):
            return 1
        if n==2:
            return 2
        step_n_1=1
        step_n_2=2
        for i in range(n-2):
            step=step_n_2+step_n_1
            step_n_1=step_n_2
            step_n_2=step
        return step


if __name__=="__main__":
    print(Solution().numWays(7))