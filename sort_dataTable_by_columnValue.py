## the code to sort a table by values from a certain column

def get_index_order(data_table, K):
	## the only interested data is from certain column
	interested_attribute_list = [int(row[K]) for row in data_table]
	## sort the key parameter while return the sorted index
  sorted_index = sorted(range(len(interested_attribute_list)), key=lambda k: interested_attribute_list[k])
  return sorted_index

N, M = raw_input().split()
data_table = []
for i in range(int(N)):
	row = raw_input().split()
  ## the row itself is already a list ##
	data_table.append(row)
K = int(raw_input())
index_order = get_index_order(data_table, K)
for i in range(len(index_order)):
	print ' '.join(data_table[index_order[i]])
