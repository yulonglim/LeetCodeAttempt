# https://leetcode.com/problems/different-ways-to-add-parentheses/
class Solution:
    def diffWaysToCompute(self, expression: str):
        solutions = []
        if expression[0] == '-':
            expression = '0' + expression
        for i in range(len(expression)):
            if expression[i] in ['+', '-', '*']:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if expression[i] == '+':
                            solutions.append(l + r)
                        elif expression[i] == '-':
                            solutions.append(l - r)
                        elif expression[i] == '*':
                            solutions.append(l * r)
        if not solutions:
            solutions.append(int(expression))

        return list(solutions)

if __name__ == "__main__":
    Solution = Solution()
    print(Solution.diffWaysToCompute("2*3-4*5"))