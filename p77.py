
'''

def prod(options):
    p = 1
    for option in options:
        p *= option
    return p

def solve( options, m):
    #print(options, m)

    if m > 722 and m < 1444:
        f = prod(options)
        if (m + f) == 1444:
            return m, f, options
        else:
            
            return False

    if m > 1444:
        return False

    if not options:
        return False



    for index in range(len(options)):
        new_options = options[0:index] + options[index+1:]

        new_m = m * options[index]

        trial = solve(new_options, new_m)

        if trial:
            return trial 

    return False



print(solve([9,8,7,6,5,4,3,2,1], 1))
'''


grid = [  

[9, 0, 0, 0, 0], 
[9, 0, 0, 0, 0],
[9, 0, 1, 0, 0],
[9, 0, 0, 0, 0],
[9, 0, 0, 0, 0],

]

def get_next_hops(current):

    next_hops = []

    # up 
    if current[0] > 0:
        if grid[current[0]-1][current[1]] != 1: 
            next_hops.append( (current[0]-1, current[1]) )

    # down
    if current[0] < 4:
        if grid[current[0]+1][current[1]] != 1: 
            next_hops.append( (current[0]+1, current[1]) )

    # left 
    if current[1] > 0:
        if grid[current[0]][current[1] - 1] != 1: 
            next_hops.append( (current[0], current[1]-1) )

    # right 
    if current[1] < 4:
        if grid[current[0]][current[1] + 1] != 1: 
            next_hops.append( (current[0], current[1]+1) )

    return next_hops

vertices = 9
start = (4,0)
end = (0, 4)

paths = []
def solve(travel_so_far):

    # print(travel_so_far)

    if travel_so_far[-1] == end:
        if len(travel_so_far) == vertices :
            if travel_so_far not in paths:
                paths.append(list(travel_so_far))
        elif len(travel_so_far) < 8:
            print ("SSSSSS", travel_so_far)
            return

    elif len(travel_so_far) > 8:
        return 

    else:
        current = travel_so_far[-1]
        possible_paths = get_next_hops(current)

        for possible in possible_paths:
            travel_so_far.append(possible)
            solve(travel_so_far)
            travel_so_far.pop(-1)


solve([start])
for p in paths:
    print(p)

print(len(paths))

