a = list(map(int, input("Enter numbers: ").split()))

for i in range(len(a)):
    mini = i
    for j in range (i+1, len(a)):
        if a[j] < a[mini]:
            mini=j
    
    a[i], a[mini] = a[mini], a[i]
    
print("Sorted array: ", a)