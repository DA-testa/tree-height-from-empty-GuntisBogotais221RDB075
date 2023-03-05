# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    root= -1
    for i in range(n):
        if parents[i]==-1:
            root= i
            break

    tree=[[] for i in range(n)]
    for i in range(n):
        if parents[i]!=-1:
            tree[parents[i]].append(i)
    # Your code here
    def max_height(node, depth):
        if not tree[node]:
            return depth
        max_depth = depth
        for child in tree[node]:
            max_depth=max(max_depth, max_height(child, depth+1))
        return max_depth
    return max_height(root, 1)

def main():
    # implement input form keyboard and from files
    check=input()
    if check=="F":
        filename = input()
        with open(filename, 'r') as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
    else:
        n = int(input())
        parents = list(map(int, input().split()))

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    print(compute_height(n, parents))
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))