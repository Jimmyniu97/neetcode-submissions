from collections import deque
class Solution:
    def helper(self, num, digit, zeros):
        i, carry = len(num)-1, 0
        digit = int(digit)
        res = deque([])
        while i >= 0 or carry:
            n = int(num[i]) if i >= 0 else 0
            prod = n*digit+carry
            res.appendleft(str(prod%10))
            carry = prod // 10
            i -= 1
        return "".join(res) + "0"*zeros


    def concat(self, num1, num2):
        res = deque([])
        i, j = len(num1)-1, len(num2)-1
        carry = 0
        while i >= 0 or j >= 0 or carry:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            total = n1+n2+carry
            res.appendleft(str(total%10))
            carry = total // 10
            i -= 1
            j -= 1
        return "".join(res)

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        if len(num2) > len(num1):
            num1, num2 = num2, num1  
        res = ""
        for i in range(len(num2)-1, -1, -1):
            curr = self.helper(num1, num2[i], len(num2)-1-i)
            res = self.concat(res, curr)
        return res