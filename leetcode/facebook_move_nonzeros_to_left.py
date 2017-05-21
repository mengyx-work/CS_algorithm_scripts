def move_nonzeros_to_left(nums):
    if len(nums) == 0:
        return 
    start, end = 0, len(nums) - 1
    while(start <= end):
        while(start < end and nums[start] == 0):
            start += 1
        while(start < end and nums[end] != 0):
            end -= 1
        if start == (len(nums) - 1) and nums[start]==0:
            return -1
        #print 'start, end: ', start, end
        #print nums[start], nums[end]
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    return start


nums =  [ 1, 0, 2, 0, 0, 3, 4 ]
assert move_nonzeros_to_left(nums) == 3

assert nums == [0, 0, 0, 2, 1, 3, 4]
nums = [0] * 5
assert move_nonzeros_to_left(nums) == -1
nums = [0] * 5 + [2]
print move_nonzeros_to_left(nums)
print nums


