a = [67, 45, 2, 13, 1, 998]
b = [89, 23, 33, 45, 10, 12, 45, 45, 45]

def firstSort(a):
    swapped = True
    count = 0
    while count < len(a):
        while swapped:
            swapped = False
            for i in range(len(a) - 1):
                count += 1
                if a[i] > a[i+1]:
                    a[i], a[i+1] = a[i+1], a[i]
                    swapped = True                   
def secondSort(b):
    swapped = True
    count = 0
    while count < len(b):
        while swapped:
            swapped = False
            for i in range(len(b) - 1):
                count += 1
                if b[i] > b[i+1]:
                    b[i], b[i+1] = b[i+1], b[i]
                    swapped = True       
