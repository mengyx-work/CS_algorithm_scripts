class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        version1 += '.0'
        version2 += '.0'

        ver1 = [int(x) for x in version1.split('.')]
        ver2 = [int(x) for x in version2.split('.')]

        #print ver1, ver2
        if len(ver1)>=len(ver2):
            length = len(ver2)
        else:
            length = len(ver1)
        
        for i in xrange(length):
            if ver1[i]>ver2[i]:
                return 1
            elif ver1[i]<ver2[i]:
                return -1
            else:
                continue
        return 0




solut = Solution()

#print solut.compareVersion("1.2.3", "1")
print solut.compareVersion("0", "1")
