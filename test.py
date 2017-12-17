import numpy as np
from sklearn.linear_model import LinearRegression

b = [10,  25,  17,  11,  13,  17,  20,  13,  9,   15]
# print(np.corrcoef(a,b)[0][1])


# x = [15,  12,  8,   8,   7,   7,   7,   6,   5,   3]
# y = [10,  25,  17,  11,  13,  17,  20,  13,  9,   15]
# n= len(x)
# b = ((n*(np.sum(np.multiply(x, y) , axis=0)) - (np.sum(x, axis=0)*np.sum(y, axis=0)))/(n*np.sum(np.power(x,2), axis=0) - (np.sum(x, axis=0)**2)))
# print(b)

# a = np.reshape(a, (-1, 1))
# b = np.reshape(b, (-1, 1))
# linreg = LinearRegression()
# linreg.fit(a, b)
# print(round(linreg.predict(10)[0][0], 1))

result = []
import math
# for i in a:
#     for j in a:
#         if(math.fabs(i - j) == 4):
#             result.add((i, j))

#a = set(a)
#
# for i in s:
#     if i+4 in s:
#         result.append([i, i+4])
#         result.append([i+4, i])
# #
# hash_map = []
# for i in range(len(a)+4):
#     hash_map.append(False)
#
# for ii in range(len(a)):
#     if ii in a:
#         hash_map[ii] = True
#
# for j in a:
#     if hash_map[j+4]:
#         result.append([j, j+4])
#         result.append([j+4, j])
#
# print(result)

#a = [15,  12,  8,   8,   7,   7,   7,   6,   5,   3]
#a = sorted(set(a))

# def bin_search(first, last, item):
#     if(last >= first):
#         middle = (first + last)//2
#         if(a[middle] == item):
#             return True
#         elif(a[middle] > item):
#             return bin_search(first, last -1, item)
#         elif (a[middle] < item):
#             return bin_search(first+1, list, item)
#     else:
#         return False
#
# print(bin_search(0, len(a)-1, 3))


# T = int(input())
#
# def isPresent(first, data, arr):
#     for i in range(first, len(arr)):
#         if arr[i] == data:
#             return True
#     return False
#
# while T:
#     N = int(input())
#     a = list(map(int, input().strip().split(' ')))
#     if len(a) != N:
#         break
#     a = set(a)
#
#     a = list(a)
#     result = []
#     for i in range(len(a)-1):
#         if isPresent(i, -a[i], a):
#             result.append(-a[i])
#             result.append(a[i])
#     for j in range(len(result)):
#         print(str(result[j]) + " ", end="")


a = [15,  12,  8,   8,   7,   7,   7,   6,   5,   3]
s = set(a)
print(s)
for i in s:
    if i+4 in s:
        result.extend(([i, i+4], [i+4, i]))
print(result)