class Solution:
  # @param {integer[]} gas
  # @param {integer[]} cost
  # @return {integer}
	def canCompleteCircuit(self, gas, cost):
		restStart, restEnd = 0, 0
		totRest = 0
		start, end = 0, 0
		leftGas = 0
		for i in range(len(gas)):
			leftGas += gas[i] - cost[i]
			if leftGas>=0:
				end += i+1
			else:
				while start<=i and leftGas<0:
					leftGas -= gas[start] - cost[start]
					totRest += gas[start] - cost[start]
					start += 1
					if end<start:
						end =start
			
			if i==len(gas)-1:
				if leftGas + totRest >=0:
					return start
				else:
					return -1


					
solut = Solution()
gas = [7, 2, 3 ,3, 5]
cost = [6, 4, 5, 1, 4]
gas = [2, 3, 3]
cost = [2, 3, 3]
print solut.canCompleteCircuit(gas, cost)	
