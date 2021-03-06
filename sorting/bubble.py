"""
    http://bigocheatsheet.com/

    best case performance: O(n)
    worst case performance: O(n^2)
    average case performance: O(n^2)

    Case 1)
        O(n) (Best case): This time complexity can occur if the array is
        already sorted, and that means that no swap occurred and
        only 1 iteration of n elements

    Case 2)
        O(n^2) (Worst case): The worst case is if the array is already sorted
        but in descending order. This means that in the first iteration it
        would have to look at n elements, then after that it would
        look n - 1 elements (since the biggest integer is at the end) and so on
        and so forth till 1 comparison occurs.
        Big Oh = n + n - 1 + n - 2 ... + 1 = (n*(n + 1))/2 = O(n^2)

    Space Complexity: O(1) Auxiliary
        Stable: Yes

    Psuedo code: http://en.wikipedia.org/wiki/Bubble_sort

    1. Each two adjacent elements are compared
    2. Swap with  lighter elements
    3. Move forward and swap with each lighter item
    4. If there is a heavier element, then this item begins to bubble to the
    surface
    5. Finally the Heaviest Element is on its place
"""

elements = raw_input("enter comma separated elements : ")
elements = elements.split(',')
elements = map(int, elements)
length = len(elements)

for i in xrange(length - 1):
    print "-" * 30
    print "outer pass : ", i
    for j in xrange(length - i - 1):
        print "inner pass : ", j
        if elements[j] > elements[j + 1]:
            elements[j + 1], elements[j] = elements[j], elements[j + 1]
        print "elements : ", elements
print "sorted elements : ", elements
