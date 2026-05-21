import statistics as st

age=[10,20,30,40,50,60,70,80,12,35,56,76,43,86,200,20]


print(st.variance(age))


## Through numpy

import numpy as nm

print(nm.var(age,axis=0))


## Population variance

def variance(age):
    n=len(age)
    # Step 1 - Mean
    mean=sum(age)/n
    # Step 2 - Differences
    difference=[]
    for value in age:
        difference.append(value-mean)
        print("Step 2 | Differences:", difference)
    # Step 3 - Square
    squared =[]
    for diff in difference:
        squared.append(diff**2)
        print("Step 3 | Squared:", squared)
    # Step 4 - Variance
    variance = sum(squared) / len(squared)
    print("Step 4 | Variance:", variance)

print(variance(age))

## sample variance

def variance(age):
    n=len(age)
    ##Mean of ages
    mean=sum(age)/n
    ##Variance
    deviation=[(x-mean)**2 for x in age]
    variance=sum(deviation)/(n-1)
    return variance

print(variance(age))


#Through Statics

import statistics as sts

sts.variance(age)