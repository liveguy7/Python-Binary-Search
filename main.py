
def binary_search(n, low, high, target):
  mid = (low + high) // 2
  if(low <= high):
    if(n[mid] == target):
      print("The target is at index {0}".format(mid))
    elif(target < n[mid]):
      binary_search(n, low, mid-1, target)
    elif(n[mid] < target):
      binary_search(n, mid+1, high, target)
  if(low > high):
    print("The target is not in the list")


collection = [3,12,45,67,90,100,119,130,200]
n = len(collection)
low = 0
high = n-1
target = 90
binary_search(collection, low, high, target)
target = 91
binary_search(collection, low, high, target)







