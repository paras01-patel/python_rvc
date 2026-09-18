# Linear Search Algorithm

print("Enter a list:")
li = list(map(int, input().split()))
print("Enter a target:")
target = int(input())
res=-1
size = len(li)
for i in range(size):
    if li[i] == target:
        res=i
        break
print(res)