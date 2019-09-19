class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # nums1[m:m+n] = nums2
        # nums1.sort()
        p = m + n -1
        m -= 1
        n -= 1
        while m>=0 and n>=0:
            if nums1[m] >nums2[n]:
                nums1[p] = nums1[m]
                m-=1
            else:
                nums1[p] = nums2[n]
                n-=1
            p-=1
        nums1[:n+1] = nums2[:n+1]
        return nums1