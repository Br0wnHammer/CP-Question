#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickestWayUp function below.
def quickestWayUp(le, sn):
    l={}
    s={}
    ss={}
    p={1:0}
    for i in range (len(le)):
        l[le[i][0]]=le[i][1]
    for i in range (len(sn)):
        s[sn[i][0]]=sn[i][1]
    i=2
    while(i<=100):
        n=[]
        for j in range (1,7):
            try:
                n.append(p[i-j]+1)
                
            except:
                break
        try:
            if(p[i]>min(n)):
                p[i]=min(n)
        except:
            p[i]=min(n)
        try:
            
            p[l[i]]=min(n)
            p[i]=100000
        except:
            altyu='jalaltu'
        try:
            if(p[i]<p[s[i]]):
                p[s[i]]=p[i]
                ss[i]=1
                i=s[i]
        except:
            altyu='jalaltu'





        i+=1
    if(p[100]>=100000):
        return(-1)
    else:
        return(p[100])

    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
