'''
Created on 2012-8-20

@author: Administrator
'''
arr1 = [1, 2, 0, 4, 5]
arr2 = [2, 3, 4, 8, 1]
arr3 = [1, 1, 5, 3, 0]
list = []
k = 0
for x in range(1, len(arr1)):
    k = arr1[x - 1] + arr1[x] + arr2[x - 1] + arr2[x]
    list.append(k)
    k = arr2[x - 1] + arr2[x] + arr3[x - 1] + arr3[x]
    list.append(k)
list.sort()
for x in range(1, len(arr1)):
    if(list[len(list) - 1] == arr1[x - 1] + arr1[x] + arr2[x - 1] + arr2[x]):
        print `arr1[x - 1]` + ',' + `arr1[x]`
        print `arr2[x - 1]` + ',' + `arr2[x]`
    if(list[len(list) - 1] == arr2[x - 1] + arr2[x] + arr3[x - 1] + arr3[x]):
        print `arr2[x - 1]` + ',' + `arr2[x]`
        print `arr3[x - 1]` + ',' + `arr3[x]`
            
    
