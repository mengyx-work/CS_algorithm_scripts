class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_value = None
        max_value = None
        length = 0
        value_sum = 0
        

        for num in nums:
            if num >=1:
                length += 1
                value_sum  = value_sum + num

                if min_value is None:
                    min_value = num
                elif  min_value > num:
                    min_value = num

                if max_value is None:
                    max_value = num
                elif max_value < num:
                    max_value = num

        if min_value is None:
            return 1
    
        if min_value == max_value:
            if min_value <= 1:
                return min_value + 1
            else:
                return min_value - 1
            
        if min_value == 1: ## for the case 0 exists
            expec_sum = length * (length + 1) / 2
            #print length, min_value, max_value, value_sum, expec_sum

            if value_sum == expec_sum:
                return length + 1
            else:
                return max_value - value_sum + expec_sum

        expec_sum = length * (2 * min_value + length - 1) / 2
        #print length, min_value, max_value, value_sum, expec_sum
        if expec_sum == value_sum:
            return min_value - 1
        else:
            return max_value - value_sum + expec_sum

solut = Solution()
test_a = [3,4,-1,1]
test_b = [3, 4, 2, 1]
test_c = [3, 0, 2, 1]

test_1 = [2]  ## expect 1
test_2 = [1]  ## expect 2
test_3 = [2, 2] ## expect 1
test_4 = [1, 1]  ## expect 2
test_5 = [0, 0]  ## expect 1
test_6 = [100, -1]
print solut.firstMissingPositive(test_6) 
