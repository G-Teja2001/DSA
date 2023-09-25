"""
Accessing Element 
    O(1) -> Contigous Memory Access 
    As we will have the first one element memory address
"""

"""
Insertion
    at end of array - O(1)
    at given index i - O(N-i) -> All elements starting from index i must be shifted to right by one position
    at beginning -> O(N) -> Shifting all elements to right by 1
"""

"""
Finding Element
    O(N) - UnSorted Array.
    O(logn) - Sorted Array.
"""

"""
Deleting Elements
    At End - O(1)
    At given index i -> O(N-i) -> All elements from i+1 index shd be shifted to left by one index.
    At beginning -> O(N) -> Shifting elements to left by one position
"""

"""
Sorting an Array
    O(nlogn)
"""