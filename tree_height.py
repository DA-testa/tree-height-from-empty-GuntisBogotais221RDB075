# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    high = numpy.zeros(int(n))
    max_height = 0
    for i in range(int(n)):
        if high[i] >0:
            height=0
            j=1
            while j !=-1:
                if high[j]:
                    height = height+height[j]
                    break
                else:
                    height=height+1
                    j = int(parents[j])
                high[i]=height
                if height > max_height:
                    max_height=height
    return max_height

def main():
    input_method = input().strip()
    if input_method =="I":
        n=input().strip()
        if n is not None:
            parents = input().strip().split()
            if parents:
                height = compute_height(n, parents)
                print(height)
    else:
        file_location = input().strip()
        try:
            with open(f"./test/{file_location}") as f:
                content = f.readlines()
        except FileNotFoundError:
            print("no file")
            return
        n=content[0].strip()
        if n is not None:
            parents = content[1].strip().split()
            if parents:
                height = compute_height(n, parents)
                print(height)


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
