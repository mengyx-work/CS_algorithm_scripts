class Solution(object):
    def licenseKeyFormatting(self, S, K):
        block, counter = "", 0
        content = []
        for i in xrange(len(S)-1, -1, -1):
            elem = S[i]
            if elem != '-':
                if counter == K:
                    content.append(block[::-1])
                    counter = 0
                    block = ""
                block += elem.upper()
                counter += 1
        if len(block) > 0:
            content.append(block[::-1])
        return '-'.join(content[::-1])

sol = Solution()
S = "2-4A0r7-4k"
assert sol.licenseKeyFormatting(S, 4) == "24A0-R74K"
S = "2-4A0r7-4k"
assert sol.licenseKeyFormatting(S, 3) == "24-A0R-74K"


