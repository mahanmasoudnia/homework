input=input("Enter 5 number, just write number and seperate with space: \n")
array=[]
for item in input.split():
    array.append(item)
def MergeSort(arr):
    if len(arr)<=1:
      return arr

    mid=len(arr)//2
    left=MergeSort( arr[:mid])
    right=MergeSort( arr[mid:]) 
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
          result.append(right[j])
          j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

sorted_arr=MergeSort(array)
print(sorted_arr)