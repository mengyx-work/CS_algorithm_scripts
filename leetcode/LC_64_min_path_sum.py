import time

def CountPaths(grid, single_path, tot_paths):
    hrzn_steps = len(grid[0])-1
    vrtl_steps = len(grid)-1
        
    if single_path['x']==hrzn_steps and single_path['y']==vrtl_steps:
        single_path['num'] += grid[vrtl_steps][hrzn_steps]
        tot_paths.append(single_path['num'])
        return
        
    if single_path['x']<hrzn_steps:
        altn_hrzn_path = single_path.copy()
        altn_hrzn_path['x'] += 1
        altn_hrzn_path['num'] += grid[altn_hrzn_path['y']][altn_hrzn_path['x']]
        CountPaths(grid, altn_hrzn_path, tot_paths)
         
    if single_path['y']<vrtl_steps:
        altn_vrtl_path = single_path.copy()     
        altn_vrtl_path['y'] += 1
        altn_vrtl_path['num'] += grid[altn_vrtl_path['y']][altn_vrtl_path['x']]
        CountPaths(grid, altn_vrtl_path, tot_paths)
    
    return

def minPathSum(grid):
    tot_paths = []
    single_path = {'x':0, 'y':0, 'num':grid[0][0]}
    CountPaths(grid, single_path, tot_paths)
        
    min = tot_paths[0]
    for i in range(1, len(tot_paths)):
        if(tot_paths[i]<min):
            min = tot_paths[i]
                
    return min


data = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]

start_time = time.time()

result = minPathSum(data)

print("--- %s seconds ---" % (time.time() - start_time))

print result
