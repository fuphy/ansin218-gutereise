list1 = [3,5,7,8,6,1,2,4,10,9]
#print (list1)
key=int(input("please input the search key:"))

### 4.1 Linear search
def linearSearch (Skey):
    if Skey not in list1:
        print ("not found")
    else:
        i=0
        while list1[i]!=Skey and i<len(list1):
            i+=1
        print ("index",i)
    return
linearSearch(key)

### 4.2 binary search
listS=sorted(list1)
#print (listS)


#key=-1
def binarySearch (Skey):
    start=0
    end=len(listS)
    while start < end and end-start >1:
        mid=int(round((start+end)/2))
        if Skey == listS[mid]:
            return mid
        elif Skey > listS[mid]:
            start = mid
        else:
            end = mid
    return -1
if binarySearch(key) is -1:
    print ("not found")
else:
    print ("found")

