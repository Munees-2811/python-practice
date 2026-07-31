from collections import Counter

class Solution(object):
    def minimumPushes(self, word):
        count = Counter(word)
        freq = sorted(count.values(), reverse=True)
        ans = 0
        for i in range(len(freq)):
            ans += freq[i] * (i // 8 + 1)
        return ans