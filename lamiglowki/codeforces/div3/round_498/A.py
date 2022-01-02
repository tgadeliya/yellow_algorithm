num = int(input())
l = list(map(int, input().split()))
res = [str(n-1 if n % 2 == 0 else n) for n in l] 
print(" ".join(res))