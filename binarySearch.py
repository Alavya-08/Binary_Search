# naive search  : scan the entire list and if its equal  to the target 
# if equal return index
# else return -1

def naive_search(l,target):
    # example = [1,2,3,,15,25]
    for i in range (len(l)):
        if l[i] == target:
            return (i)
    return (-1)

# Binary Search works on divide and conqure 
# assuming the fact that our list is sorted
def binary_search(l,target,low=None,high=None):
    # example = [1,2,3,,15,25]
    if (low is None):
        low = 0
    if (high is None):
        high = len(l) - 1
    if (high <low) :
        return (-1)
    mid = (low+high)//2 #dividing the list in half
    
    if (l[mid] == target):
        return mid
    elif (target < l[mid]):
        return binary_search (l,target,low,mid+1)
    else:
        # if target >l[mid]
        return binary_search(l,target,mid+1,high)
        
        
# practice code 
if __name__ == '__main__':
    l = [1,4,6,11,21]
    target = 11
    print(naive_search(l,target))
    print(binary_search(l,target))
    