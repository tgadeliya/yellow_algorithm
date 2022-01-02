n,k = map(int,input().split())
l = list(enumerate(map(int, input().split())))
l = sorted(l, key=lambda x:x[1], reverse=True) 
slice = l[:k]

res = sorted([idx for idx, _ in slice]) + [n]

n_zad = [res[1]]
for i in range(2, len(res)):
    n_zad.append(res[i] - res[i-1])


print(sum([r for _,r in slice]))
print(" ".join([str(zad) for zad in n_zad]))