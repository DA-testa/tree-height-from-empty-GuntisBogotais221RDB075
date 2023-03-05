# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    root= -1
    for i in range(n):
        if parents[i]==-1:
            root= i
            break

    tree=[[] for i in range(n)]
    for i in range(n):
        if parents[i]!=-1:
            tree[parents[i]].append(i)
    def get_height(node, depth):
        if not tree[node]:
            return depth
        max_depth = depth
        for child in tree[node]:
            max_depth=max(max_depth, get_height(child, depth+1))
        return max_depth
    return get_height(root, 1)

def main():
    input_method = input().strip()
    if input_method =="I":
        n = int(input())
        parents = list(map(int, input().split()))
    else:
        file = input().strip()
        path= file+"./test/"
        with open(path, 'r', encoding='utf-8') as file:
            n = int(file.readline())
            parents = list(map(int, file.readline().split()))
    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
