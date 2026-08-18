class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        half = (len(A)+len(B)+1)//2
        l, r = 0, len(A)
        while l <= r:
            pivotA = (l+r) // 2
            pivotB = half-pivotA
            leftA = A[pivotA-1] if pivotA > 0 else float("-inf")
            rightA = A[pivotA] if pivotA < len(A) else float("inf")
            leftB = B[pivotB-1] if pivotB > 0 else float("-inf")
            rightB = B[pivotB] if pivotB < len(B) else float("inf")

            if leftB>rightA:
                l = pivotA+1
            elif leftA>rightB:
                r = pivotA-1
            else:
                if (len(A)+len(B)) % 2 == 1:
                    return max(leftA, leftB)
                
                return (max(leftA, leftB)+min(rightA, rightB)) / 2
