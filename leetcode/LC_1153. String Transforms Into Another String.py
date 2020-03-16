class Solution(object):
    def canConvert(self, str1, str2):
        if str1 == str2:
            return True
        m = {}
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if str1[i] not in m:
                    m[str1[i]] = str2[i]
                elif m[str1[i]] != str2[i]:
                    return False
        return len(set(str2)) < 26
