n = int(input("tedad e donbale fibo : "))

fibonacci = [1,2]

for i in range(2,n):

    formul = fibonacci[i-1]+fibonacci[i-2]

    fibonacci.append(formul)

print(fibonacci)