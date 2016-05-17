#class Sort () :
#	def __init__(self) :
#		print "This a sorting program"
def mergeSort(alist):
  #  print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

       # while i < len(lefthalf):
       #     alist[k]=lefthalf[i]
       #     i=i+1
       #     k=k+1

        #while j < len(righthalf):
        #    alist[k]=righthalf[j]
        #    j=j+1
        #    k=k+1
    #print("Merging ",alist) 
 
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp




def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark



alist = list(input("  enter a list  \n"))



print "1) Merge Sort"
print "2) Bubble Sort"
print "3) Quick Sort"

a = input("Enter your choice");

if (a==1) :
	mergeSort(alist)
	print(alist)


elif (a==2) :
	bubbleSort(alist)
	print(alist)


elif (a==3) :
	quickSort(alist)
	print(alist)








