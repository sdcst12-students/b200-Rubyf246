#!python3


def getIntegers(myList):
    # myList : expected list or tuple
    # iterate through myList and add all the integers to the new list
    integers = []
    for inpt in myList:
            
        if isinstance(inpt, int):
            integers.append(inpt)
            
        ##else:
            ##print("do not append")
    print(integers)    
    return integers

def getFactor(myList,number):
    # myList : expected list or tuple
    # number : integer
    # iterate through the list and add the number to the list if
    # it is a factor of the number
    factors = []
 
    for m in myList:
        if (m != 0) and (number % m == 0):
             ## member is a factor of number
              factors.append(m)        
    print(factors)      
    return factors

def getNegatives(myList):
    # myList : expected list or tuple
    # iterate through myList and add all the negative numbers to the new list
    negatives= []
    for inpt in myList:
        if (inpt < 0):
          negatives.append(inpt)        
    print(negatives)     
    return negatives

def getIntersection(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # return a sorted list of numbers that is in both lists
    # the intersection of the 2 number sets
    common = []
    for m1 in list1: #iterate list1
        if m1 in list2:
            common.append(m1)
            
    for m2 in list2: #iterate list2
        if (m2 in list1) and (m2 not in common): # do not add to common twice
            common.append(m2)
    print (common)
    return common

def getUnion(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # return a sorted list of numbers that is in either of the lists
    # duplicate values will be ignored
    union = []
    for m1 in list1:
        union.append(m1)
    for m2 in list2:
        if (m2 not in union):
            union.append(m2)
    union.sort()
    print(union)
    return union   

def getMerge(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # add the elements of list2 into list1
    # if the list2 element is in list1, add it at the position where it occurs in list1
    # if the list2 element is not in list1, add it to the end
    for m in list2:
        if m in list1:
            idx = list1.index(m)
            list1.insert(idx,m)
        else:
            list1.append(m)
    print (list1)            
    return list1


def main():
    easy1 = [5,10,15,2,4,6,8]
    easy2 = [-2,-4,-6,2,4,6,0.1]
    numbers1 = [3,5,8,12,11,19,10,7,2,15,25,34,16,32,50,60,100,-3,0.25]
    numbers2 = [3,7,11,15,19,23,27,31,35,39,44,50]
    try:
        assert getIntegers([3,4,1.2,1.3,5]) == [3,4,5]
        assert getFactor(range(10),12) == [1,2,3,4,6]
        assert getNegatives([-3,-1,0,1,4]) == [-3,-1]
        assert getUnion(easy1,easy2) == [-6, -4, -2, 0.1, 2, 4, 5, 6, 8, 10, 15]
        assert getIntersection(easy1,easy2) == [2,4,6]
        assert getMerge(easy1,easy2) == [5,10,15,2,2,4,4,6,6,8,-2,-4,-6,0.1]
        print("All assertions passed")
    except:
        print("At least 1 assertion failed")

if __name__ == "__main__":
    main()
