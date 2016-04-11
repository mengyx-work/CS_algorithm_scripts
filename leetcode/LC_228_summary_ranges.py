class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        results = []
        if len(nums)==0:
            return results
        if len(nums)==1:
            result = "%i" %(nums[0])
            results.append(result)
            return results
            
        start = nums[0]
        end = nums[0]

        for i in xrange(1, len(nums)):

            if nums[i]<=(end+1):
                end = nums[i]
            else:
                if start==end:
                    result = "%i" %(start)
                    results.append(result)
                else:
                    result = "%i->%i" % (start, end)
                    results.append(result)
                    
                if i==(len(nums)-1):
                    result = "%i" %(nums[-1])
                    results.append(result)
                    return results
                else:    
                    start = nums[i]
                    end = nums[i]
                
            if i==(len(nums)-1):
                result = "%i->%i" % (start, end)
                results.append(result)
                return results

solut = Solution()
data = [0, 5, 9]
print solut.summaryRanges(data)
