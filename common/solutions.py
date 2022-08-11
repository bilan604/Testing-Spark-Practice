from __future__ import annotations


from math import factorial as f


class Solution:
    # https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
    @staticmethod
    def countOrders(n):
        if n == 1:
            return 1
        return (f(2*n) // (2**n)) % (10**9 + 7)