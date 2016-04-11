class Solution:
    '''
    def permute(self, nums):
        if len(nums)==1:
            return [[nums[0]]]
        stack = []
        res = []
        for num in nums:
            stack.append([num])
        while stack:
            v = stack.pop()
            if len(v)==len(nums): res.append(v)
            else:
                for num in nums:
                    if num not in v:
                        tmp = v[:]
                        tmp.append(num)
                        stack.append(tmp)
        return res

    ###########################
    def permute(self, nums):
        if len(nums)==1:
            return [[nums[0]]]
        stack = []
        res = []
        for num in nums:
            tmpNums = nums[:]
            tmpNums.remove(num)
            stack.append(([num], tmpNums))

        print stack
        while stack:
            v= stack.pop()
            print 'v: ', v
            if len(v[1])==1:
                v[0].append(v[1][0])
                res.append(v[0])
            else:
                for num in v[1]:
                    tmpNums = v[1][:]
                    tmpList = v[0][:]
                    tmpList.append(num)
                    tmpNums.remove(num)
                    stack.append((tmpList, tmpNums))

        return res
        '''
	def creatPermut(self, nums, curIndx, maxIndx, res):
		#print 'the first nums: ', nums, 'curIndx: ', curIndx
		if curIndx==maxIndx:
            res.append(tuple(nums))
            #res.append(nums)            
            #print 'the result: ', res
            return
       
        for i in range(curIndx, maxIndx):
			visited[nums[i]] = 1    
            tmp1 = nums[curIndx]
            nums[curIndx] = nums[i]
            nums[i] = tmp1
            #print 'nums: ', nums 
            self.creatPermut(nums, (curIndx+1), maxIndx, res)
            
            tmp1 = nums[curIndx]
            nums[curIndx] = nums[i]
            nums[i] = tmp1

    def permute(self, nums):
        resList = []
        self.creatPermut(nums, 0, len(nums), resList)
        #print 'the result to send: ', resList
        tmpRes = [list(elem) for elem in resList]
        return tmpRes

solut = Solution()
#nums = []
#nums = [1, 2]
#nums = [4,1,0, 3]
nums = [1, 2, 3]
#nums = [1, 1, 2, 2, 3]
print solut.permute(nums) 
