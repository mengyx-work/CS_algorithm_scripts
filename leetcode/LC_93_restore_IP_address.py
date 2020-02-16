class Solution(object):
	def restoreIpAddresses(self, s):
		res = []
		self.dsf(res, [], s, 0)
		return res

	def dsf(self, res, curRes, s, i):
		if len(curRes) > 4:
			return
		if i == len(s) and len(curRes) == 4:
			res.append('.'.join(curRes))
		else:
			tmpRes = curRes[:]
			for j in range(i, min(i+3, len(s))):
				sec = s[i:(j+1)]
				if (len(sec) > 1 and sec.startswith('0')) or int(sec) > 255:
					continue
				tmpRes.append(sec)
				self.dsf(res, tmpRes, s, j+1)
				tmpRes = tmpRes[:-1]



s ='25525511135'
solut = Solution()
assert solut.restoreIpAddresses(s) == ['255.255.11.135', '255.255.111.35']
s = '0000'
assert solut.restoreIpAddresses(s) == ['0.0.0.0']
s = '010010'
print(solut.restoreIpAddresses(s))

