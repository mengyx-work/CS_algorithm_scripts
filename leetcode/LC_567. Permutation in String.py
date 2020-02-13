from collections import defaultdict

class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        ref, cur = defaultdict(int), defaultdict(int)
        cnt, l, r = 0, 0, 0

        for char in s1:
            ref[char] += 1

        while r < len(s2):
            if s2[r] not in ref:
                cnt, cur = 0, defaultdict(int)
                l = r + 1
            else:
                cur[s2[r]] += 1
                cnt += 1
                if cur[s2[r]] == ref[s2[r]] and cnt == len(s1):
                        # print(l, r, cnt, cur)
                        return True
                else:
                    while cur[s2[r]] > ref[s2[r]]:
                        cur[s2[l]] -= 1
                        l += 1
                        cnt -= 1
            # print(l, r, cnt, cur)
            r += 1
            # print(r, cnt, cur)
        return False

sol = Solution()
s1 = "adc"
s2 = "dcda"
assert sol.checkInclusion(s1, s2) == True

s1 = "hello"
s2 = "ooolleoooleh"
assert sol.checkInclusion(s1, s2) == False

s1 = "ab"
s2 = "eidbaooo"
assert sol.checkInclusion(s1, s2) == True

s1= "ab"
s2 = "eidboaoo"
assert sol.checkInclusion(s1, s2) == False


