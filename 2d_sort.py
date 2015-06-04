import sys
from collections import namedtuple


####################################################################################################
##									Summary of the Algorithm
##	2D (x, y) data is given. 
##	A. the data is sorted by the metric (x^2 + y^2) so that for any A<B, A is always before B in the sorted list.
##
##	B. start from every large element as the start_index to search all the possible paths. A trick to exclude all
##	the element considered as a valid middle step in the found paths.
##	
##	C. In the paths search using 'get_full_pathList', function checks whether next/new step can be found using function
##	'get_updated_pathList' and upated paths along with new steps. Once no more paths is found. search is finished. 
##	
##	D. The possible next step is considered using function 'get_possible_next_step'. It starts the search with
##	the largest/adjacent element in the sorted list. If the step can be used as future step, discard it.
##
####################################################################################################


## create a global variable that's used by multiple functions
considered_index = set()

##########################################################################
## check if the possible step could be a future step, but not the adjacent step
def check_following_step(data, possible_next_step_list, possible_index):
	
	if (len(possible_next_step_list)==0):
		return True
	
	possible_x = data[possible_index][0]
	possible_y = data[possible_index][1]

	for index in possible_next_step_list:
		next_x = data[index][0]
		next_y = data[index][1]
	
		if((next_x>possible_x) and (next_y>possible_y)):
			return False

	return True

##########################################################################
## function 'get_possible_next_step' gives back all the possible steps 
## based on the current_position. The algorithm requires that the next
## possible step is 
## a. smaller than current_position in both x and y;
## b. but can't be a future steps

def get_possible_next_step(data, current_position):
	## current position is the index in data list
	## data is sorted by the disance to origin

	if(current_position==0):
		return []
	
	possible_next_step_list = []
	current_x = data[current_position][0]
	current_y = data[current_position][1]
	## loop through the possible candidates for the next step
	for i in range(current_position):
		possible_index = current_position - 1 - i
		possible_x = data[possible_index][0]
		possible_y = data[possible_index][1]
			
		if((possible_x<current_x) and (possible_y<current_y) and check_following_step(data, possible_next_step_list, possible_index)):
			possible_next_step_list.append(possible_index)
			print 'current_position, the step added: ', current_position, possible_index
	return possible_next_step_list

##########################################################################
## calcuate/estimate the result for a full path

def get_path_result(path):
	path_result_structure = namedtuple("path_result", "start_index end_index steps_num")
	path_result = path_result_structure(path[0], path[-1], len(path))
	
	#return path_result
	return path


##########################################################################
## this function 'get_updated_pathList' receives a list of paths as inputs.
## function forwards every single path in this list one step. If no possible 
## next step is found, analyzes and sends result into the results list; 
## otherwise put a new path into the 'new_pathList'

def get_updated_pathList(data, path_list, path_results):
	
	new_pathList = []

	for path in path_list:
		current_step = path[-1]
		next_step_list = get_possible_next_step(data, current_step)

		if(len(next_step_list)!=0):
			global considered_index

			for nex_step in next_step_list:
				considered_index.add(nex_step)
				new_path = list(path)
				new_path.append(nex_step)
				new_pathList.append(new_path)
		## no possible next step is found for single path
		else:
			result = get_path_result(path)
			path_results.append(result)

	return new_pathList



##########################################################################
## loop through all the possible path sharing the same 'start_index'.
## the function 'get_updated_pathList' constantly returns new/updated paths
## with one new step added, until there's no updated_path is found

def get_full_pathList(data, start_index, path_results):

	new_pathList = [[start_index],]

	while(len(new_pathList)>0):
		path_list = new_pathList
		new_pathList = get_updated_pathList(data, path_list, path_results)



##########################################################################

def search_2d(data):

	sorted_data = sorted(data, key=lambda elem: elem[0]*elem[0]+elem[1]*elem[1])
	print sorted_data
	path_results = []
	
	for start_element in reversed(sorted_data):
		startt_index = sorted_data.index(start_element)
		print 'check startt_index: ', startt_index
		if(startt_index not in considered_index):
			get_full_pathList(sorted_data, startt_index, path_results)

	print path_results

##########################################################################

def main(argv):
	'''
	if(len(argv) != 3):
		print "Not enough arguments"
		sys.exit(0)
	else:
		honeycomb, max_layer_num = read_input(argv[1])
		read_dict(argv[2], honeycomb, max_layer_num)
	'''
	
	#input = open('input_data.txt', 'r')
	#data = [1, 3, 4, 6, 2 ,2, 8, 4, 8, 10]
	data = [(1, 1), (1, 4), (2, 5), (6, 5),(5, 7), (6, 3), (9, 8), (10 ,10), (9, 7), (8, 10), (12, 11), (12, 13), (13, 11)]
	## assumed the data list is sorted ##
	search_2d(data)

if __name__ == "__main__":
    main(sys.argv)
