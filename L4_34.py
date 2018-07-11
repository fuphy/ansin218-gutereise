# 4.3 Bubble search
list2=[6,5,3,1,8,7,2,4,10,9,11]
#listTest= [1,3,5,8,7]
end = len (list2)-1
#print (end)

def SortOrNo (listInput):
    if all(listInput[i] <= listInput[i+1] for i in range(len(listInput)-1)):
        return True
    else: 
        return False
#print (SortOrNo(list2))

#while SortOrNo(list2) is False:
#    for i in range (len(list2)-2):
#        i=0
#        while i<end-1:
#            if list2[i]>list2[i+1]:
#                list2[i], list2[i+1] = list2[i+1],list2[i]
#            i=i+1
#        end=end-1
#    print (list2)


# for i in range (len(list2)-2):
#     while SortOrNo(list2) is False:
#         i=0
#         while i<end:
#             if list2[i]>list2[i+1]:
#                 list2[i], list2[i+1] = list2[i+1],list2[i]
#             i=i+1
#         end=end-1
#         print (list2)
#print (list2)


# insertion sort


for i in range (len(list2)-2):
    while SortOrNo(list2) is False:
        i=0
        j=end
        x=list2[j]
        while i< j-1:
            if x < list2[i]:
                list2.insert(x,i)
                i+=1
        j=j-1
    print(list2)

