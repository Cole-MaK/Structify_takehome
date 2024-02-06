from structify_takehome import *
import numpy as np
assert calculate_intersections([(0.78,1.47,1.77,3.92),('s_1','s_2','e_1','e_2')]) == 1
assert calculate_intersections([(0.9,1.3,1.7,2.92),('s1','e1','s2','e2')]) == 0
assert calculate_intersections([(0.9,1.3,1.7,2.92),('s1','s2','a1','e2')]) == 'invalid tuples containing identifiers'
assert calculate_intersections([(0.1,0.2,0.3,2,2.1,2.2),('s_1','s2','s_3','e_1','e2','e3')]) == 3



# list of start and endpoints, considering case where all starts come first then end points
# since this results in the most computations.
heheheha = [] 
max = 16 # can set amount of chords where chord_count = max / 2

for i in range(max):
    if i < int(max/2):
        heheheha.append(f"s_{i}")
    else:
        heheheha.append(f"e_{i - int(max/2)}")


# create corresponding radian list and does not matter value since the algorithm only considers
# id tuple.
test_tuple = []
for i in range(max):
    test_tuple.append(i)

assert calculate_intersections([range(8),heheheha]) == 28

