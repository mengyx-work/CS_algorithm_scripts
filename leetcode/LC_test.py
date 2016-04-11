import collections
class Solution:

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 1 or t < 0:
            return False
        dic = collections.OrderedDict()
        for n in nums:
            print 'dic: ', dic
            print 't: ', t, 'n//t: ', (n//t)
            key = n if not t else n // t
            print 'key: ', key
            #for m in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
            for m in (dic.get(key - 1), dic.get(key + 1)):
                if m is not None and abs(n - m) <= t:
                    return True
            if len(dic) == k:
                dic.popitem(False)
            dic[key] = n
        return False



solut = Solution()
data = [3, 6, 11, 8, 10, 30, 12, 3]
data = [3, 10, 20, 43, 30, 43]
print solut.containsNearbyAlmostDuplicate(data, 3, 2)
