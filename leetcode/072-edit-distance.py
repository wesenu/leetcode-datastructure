#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Feb-24-23 16:56
# @Author  : Kan HUANG (kan.huang@connect.ust.hk)
# @RefLink : https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Minimum distance by edit distance
        : param word1:
        : param word2:
        : return:
        """
        if len(word1) == 0:
            return len(word2)
        elif len(word2) == 0:
            return len(word1)
        else:
            if word1[0] == word2[0]:
                # ignore same chars
                return self.minDistance(word1[1:], word2[1:])
            else:
                return 1 + min(
                    self.minDistance(word1[1:], word2),
                    self.minDistance(word1, word2[1:]),
                    self.minDistance(word1[1:], word2[1:])
                )


def main():
    sol = Solution()
    word1 = "horse"
    word2 = "ros"
    assert sol.minDistance(word1, word2) == 3

    # Time Limit Exceeded
    word1 = "dinitrophenylhydrazine"
    word2 = "acetylphenylhydrazine"
    print(sol.minDistance(word1, word2))


if __name__ == "__main__":
    main()
