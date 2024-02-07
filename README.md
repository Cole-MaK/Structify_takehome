# Structify_takehome

-------------------
Runtime: O(nlog(n))
-------------------

--------
Process:
--------

Initially looking at the problem it seemed like a fairly easy question. However, my initial solution required a time complexity of O(n^2) and I knew this could not be the best solution.

Looking at this problem more, I realized that the radians list would not even be useful so I create another algorithm that utilized a list that kept track of --
'active chords' in order to count the number of starting points in between (for example) the first chord's start and end. However this did not account for the index of the endpoint.

After multiple different O(n^2) time complexity solutions I had the idea to think about this problem from a math approach thinking about what properties make a chord intersect. These --
properties included that the sum of the chord's radians had to be greater than the chord we are checking intersection for but also less than double the sum. After this I could sort the --
sums and use binary search but I could not completely figure out the solution.

I finally realized that this is a sorting algorithm to find an endpoints corresponding startpoint once the algorithm realizes we have found an endpoint resulting in a nlon(n) solution.

After testing with over 50000 chords the new nlog(n) method reduced computational time from 18s to 1.3s. At smaller chord amounts computation was similar.

------
Design
------

The input states that the radians will always have to be in ascending order and that the s_x < e_x so all starts will occur first in the identifier list. Using the ordered nature --
we know that when we see our first endpoint all starting points inbetween will count for an intersection. This is because for a chord to intersect only one end of the chord can be --
inbetween the radian values of another chord. 

Using this information we need to make a few functions:

    - PointID
        --- Time Complexity: (O(1))
        - we know we are going to identify the chord index many times so we make a function to find this value quickly.

    - calculate_intersections
        --- Time Complexity: (O(n))
        - we need to go through the list to find each endpoint in order which in the worst case will go through a list of length n.
        - runs binary search.
        - after binary search finds a corresponding startpoint, we can subtract the endpoint index from the startpoint index to --
            aquire the amount of intersections and add to a running count.
        - Lastly we need to remove the end and start point in this order, to not interupt index deletion and to not doulbe count --
            intersections.

    - binary_search
        --- Time Complexity: (O(log(n)))
        - after calculate_intersections finds an endpoint we need to binary search the list to find its corresponding startpoint.
