from os import *
from sys import *
from collections import *
from math import *

def merge(left,right):
	merged = []
	leftindex = rightindex = 0 
	count = 0
	while leftindex < len(left) and rightindex < len(right):
		if left[leftindex] <= right[rightindex]:
			merged.append(left[leftindex])
			leftindex += 1
		else:
			merged.append(right[rightindex])
			rightindex += 1
			count+=len(left) - leftindex
	merged.extend(left[leftindex:])
	merged.extend(right[rightindex:])
	return merged,count

def mergesort(arr):
	if len(arr) <= 1:
		return arr,0
	mid = len(arr)//2
	left,left_count = mergesort(arr[:mid])
	right, right_count = mergesort(arr[mid:])
	arr ,count = merge(left,right)
	total_count = left_count + right_count + count 
	return arr, total_count 

def getInversions(arr, n) :
	# Write your code here.
	arr, count = mergesort(arr)
	return count


# print(getInversions([52244275, 123047899, 493394237, 922363607 ,378906890 ,188674257 ,222477309 ,902683641 ,860884025 ,339100162],10))
print(getInversions([3,2,1,4],3))