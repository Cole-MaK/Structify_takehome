import re

def pointID(point):
    '''
    Args:
        point(str): takes argument of the form s_i or e_i where i is an index
    Return:
        int: the index of the a point 
            if no match return -1

    uses regex to find index of starting or ending point  
    '''

    pattern = r'[es](_)?(\d+)'
    match = re.search(pattern, point)
    if match:
        return int(match.group(2))
    return -1
    
def calculate_intersections(radian_identifier):
    '''
    Args:
        radian_identifier(tuple): takes argument with a tuple containing two list
            - radians
            - point identifiers (startpoint or endpoint)
    Return:
        int: number of intersections or error message stating invalid input

    Ignores radian list since the starting points in the identifier list are assumed to be in --
    acsending ordered.
    (Identifier list will be referred to as 'list').
    Iterate through list to find first endpoint.
    Once an endpoint is found length between end and start will indicate number of intersections.
    Adds number of intersections into intersection count variable.
    Removes start and endpoint in order once their intersections are accounted for.
    
    Reiterate through the new list with start and end point removed and ensuring index is correct --
    since removing a start point shifts index.
    Iterates until no more start and endpoints in list.
    '''

    identifiers = list(radian_identifier[1])
    intersection_count = 0 # initialize intersections
    i = 0 # initialize index
    
    while i < len(identifiers): # iterating through identifiers to looks for an endpoint
        label = identifiers[i]
        if label[0] == 'e': # endpoint found
            id = pointID(label) # get id number
            if id == -1: # not a valid id
                print('error not a valid label')
                break 
            else: # valid id and run binary search
                x = binary_search(identifiers[:i],id)
                intersection_count += (i - x - 1) # calculate intersection and add to count
                identifiers.pop(i) # pop endpoint first to not interupt startpoint
                identifiers.pop(x) # remove start point
                i -= 1
        elif label[0] == 's': # a startpoint
            i += 1
        else: # if neither a s or e
            return 'invalid tuples containing identifiers'
            
    return intersection_count 

def binary_search(sorted_sub_list, target):
    '''
    Args:
        sorted_sub_list(list): a sublist starting at a startpoint and its corresponding endpoint
        target(int): the index to find and endpoints corresponding start point
    Return:
        mid(int): index of startpoint corresponding to a given endpoint

    Utilize Binary Search to achieve O(log(n))
    '''
    start = 0 # initialize start point
    end = len(sorted_sub_list) # set end index to use binary search

    while start <= end:
        mid = (start + end)//2
        
        if pointID(sorted_sub_list[mid]) == target:
            return mid
        elif pointID(sorted_sub_list[mid]) < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

