class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        q, r = 1, 0
        for i in range(len(digits)-1, -1, -1):
            q, r = divmod(digits[i]+q, 10)
            digits[i] = r
            if q == 0:
                break
        if q != 0:
            digits.insert(0, 1)
        return digits