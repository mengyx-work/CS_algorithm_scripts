## Challenge:
## how to find the element in the sequence 
## that is more than half (or not exit at all)
## requires linear time O(n) and O(1) space. 
## How to use O(1) space to find the element from the array

## excellent solution here https://leetcode.com/discuss/76264/java-easy-version-to-understand
## similar approach, but requires a second round to prove the results

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums

        if len(nums) == 2:
            if nums[0] == nums[1]:
                return [nums[0]]
            else:
                return nums

        tmpA = nums[0]
        cntA = 1

        for num in nums[1:]:
            if num != tmpA:
                tmpB = num
                cntB = 1
                break
            else:
                cntA += 1

        if cntA == len(nums) or cntA + 1 == len(nums):
            return [tmpA]

        
        start_point = cntA + 1
        full_len = len(nums)
        for num in nums[start_point:]:
            ## completely new start
            if cntA == 0 and cntB == 0:
                tmpA = num
                cntA = 1
                continue

            if cntA != 0 and cntB == 0:
                if num == tmpA:
                    cntA += 1
                    continue
                else:
                    tmpB = num
                    cntB = 1
                    continue

            if cntB != 0 and cntA == 0:
                if num == tmpB:
                    cntB += 1
                    continue
                else:
                    tmpA = num
                    cntA = 1
                    continue
             
            if num != tmpA and num != tmpB:
                cntA -= 1
                cntB -= 1
                full_len -= 3
            if num == tmpA:
                cntA += 1
            if num == tmpB:
                cntB += 1

        if full_len == 0:
            return []
        #'''
        print tmpA, cntA
        print tmpB, cntB
        print full_len
        #'''

        final_res = []
        cntA,cntB = 0, 0
        for num in nums:
            if num == tmpA:
                cntA += 1
        if 3*cntA > len(nums):
            final_res.append(tmpA)
        
        if tmpB != tmpA:
            for num in nums:
                if num == tmpB:
                    cntB += 1
            if 3*cntB > len(nums):
                final_res.append(tmpB)

        return final_res

solut = Solution()
tests = [ [3,2,2], [2,2], [1,2,2,4,2], [1,2,2], [1,1,1], [1,2,1,4,2,1,1,2] ]
test_a = [1,2,3,2]

print 'special case:', solut.majorityElement(test_a)
#'''
for test in tests:
    print solut.majorityElement(test)
#'''

          

    
