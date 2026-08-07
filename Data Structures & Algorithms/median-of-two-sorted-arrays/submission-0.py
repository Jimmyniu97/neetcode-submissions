class Solution:
    def getKth(self, a, m, b, n, k, a_start=0, b_start=0):
        if m > n:
            return self.getKth(b, n, a, m, k, b_start, a_start)
        if m == 0:
            return b[k-1]
        if k == 1:
            return min(a[a_start], b[b_start])
        
        i = min(m, k//2)
        j = min(n, k//2)

        if a[a_start+i-1] > b[b_start+j-1]:
            return self.getKth(a, m, b, n-j, k-j, a_start, b_start+j)
        else:
            return self.getKth(a, m-i, b, n, k-i, a_start+i, b_start)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = (len(nums1)+len(nums2)+1) // 2
        right = (len(nums1)+len(nums2)+2) // 2

        return (self.getKth(nums1, len(nums1), nums2, len(nums2), left) + self.getKth(nums1, len(nums1), nums2, len(nums2), right)) / 2.0
