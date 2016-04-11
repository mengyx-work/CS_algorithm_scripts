class Solution:
	## function checks if the substring can be a valid section of IP ##
	def validSec(self, s):
		if 0<int(s)<=255 and s[0]!='0':
			return True
		elif int(s)==0 and len(s)==1:
			return True
		return False

	## to create a section of IP recursively ##
	def setIPSec(self, s, indx, secNum):
		#print 'indx: %i, secNum: %i' % (indx, secNum)
		tmpRes = []
		if secNum==3:
			if self.validSec(s[indx:]):
				return [s[indx:]]
			else:
				return tmpRes
		else:
			for i in range(1, 4):
				if indx+i<len(s) and self.validSec(s[indx:indx+i]):
					tmpList = self.setIPSec(s, indx+i, secNum+1)
					for tmp in tmpList:
						tmpRes.append(s[indx:indx+i]+'.'+tmp)
			return tmpRes
					
    # @param {string} s
    # @return {string[]}			
	def restoreIpAddresses(self, s):
		resList = self.setIPSec(s, 0, 0)
		return resList  

s ='25525511135'
#s='0000'
#s = '010010'
solut = Solution()
print solut.restoreIpAddresses(s)
