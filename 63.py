q = int(input('Termos:'))
termos=[0,1,1]
for i in range(q):
    termos.append(sum(termos[-2::]))
print(str(termos[0:q])[1:-1])