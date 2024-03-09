import random as rand
import matplotlib.pyplot as plt

def plot(arr,n,s,red,blue):
    plt.cla()
    x_values = range(len(arr))
    plt.bar(x_values, arr, color=['red' if i == red else 'blue' if i == blue else 'black' for i in range(n)])

    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.title(s)

    plt.pause(0.5)

def checkSort(arr,n):
    for i in range(n-1):
        if(arr[i]>arr[i+1]):
            return 0
    return 1

def generate(arr,n):
    for i in range(n):
        arr.append(rand.random()%750)

def selectionSort(arr,n,begin,end):
    min_index = 0
    for i in range(n):
        for j in range(i+1,n):
            if(arr[j]<arr[min_index]):
                min_index = j
            plot(arr,n,"selectionSort",min_index,j)
        if(i!=min_index):
            arr[i],arr[min_index] = arr[min_index],arr[i]
            plot(arr,n,"selectionSort",min_index,i)
        min_index = i+1

def bubbleSort(arr,n,begin,end):
    swapped = False
    for i in range(n):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
            plot(arr,n,"bubbleSort",j,j+1)
        if(swapped == False):
            break

def insertionSort(arr,n,begin,end):
    k = 0
    index = 0
    for i in range(n):
        index = i+1
        k = i
        for j in range(index-2,-1,-1):
            if(arr[j]>arr[k]):
                arr[j],arr[k] = arr[k],arr[j]
                plot(arr,n,"insertionSort",k,j)
                k = j
            else:
                break

def quickSort(arr,n,begin,end):
    if(begin>=end):
        return
    pivot = arr[end]
    k = begin-1
    for i in range(begin,end+1):
        if(arr[i]<pivot):
            k = k+1
            arr[k],arr[i] = arr[i],arr[k]
            plot(arr,n,"quickSort",end,i)
    arr[k+1],arr[end] = arr[end],arr[k+1]
    plot(arr,n,"quickSort",end,k+1)
    quickSort(arr,n,begin,k)
    quickSort(arr,n,k+2,end)

fig, ax = plt.subplots()
n = int(input("Enter the size of the array: "))
SortArray = [selectionSort,bubbleSort,insertionSort,quickSort]
for i in range(len(SortArray)):
    arr = []
    generate(arr,n)
    SortArray[i](arr,n,0,n-1)
    plt.show()
    print(checkSort(arr,n))





