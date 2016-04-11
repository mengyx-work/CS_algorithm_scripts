import sys

## recursively process the list of all possible paths until it reaches the end.
def ProcessPath(paths):
	further_step = False
	new_paths = []
	for path in paths:
		if path>0:
			further_step = True
		if(path==0):
			new_paths.append(path)			
		if(path>=1):
			new_paths.append(path-1)
		if(path>=2):
			new_paths.append(path-2)
	#print 'paths after extending: ', new_paths
	#print 'further_step:', further_step
	if(further_step==False):
		length = len(new_paths)
		return length
	else:
		return ProcessPath(new_paths)


def diff_step(n):

	## only one option 
	if(n==1):
		return 1
 	if(n>=2):
		paths = [n-1, n-2]
		result = ProcessPath(paths)
		print result
		return result 

def main(argv):

	result = diff_step(2)

	print result

if __name__ == "__main__":
    main(sys.argv)
