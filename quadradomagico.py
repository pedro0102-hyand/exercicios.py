def verify(quadrado):
    s_diagonal_principal=quadrado[0]+quadrado[4]+quadrado[8]
    s_diagonal_secundaria=quadrado[2]+quadrado[4]+quadrado[6]
    if s_diagonal_principal != s_diagonal_secundaria :
        return False
    for i in range(3):
        s_line=sum(quadrado[i*3:i*3+3])
        s_column=quadrado[i]+quadrado[i+3]+quadrado[i+6]
        if s_line != s_column or s_line != s_diagonal_principal :
            return False
        return True
    def magicos():
        num=[1,2,3,4,5,6,7,8,9]
        quadrados=[]
        for i in num:
            for j in num:
                if j !=i  :
                    for k in num :
                        if k != i and k !=j :
                            for l in num :
                                if l!=i and l!=j and l!=k:
                                    for m in num:
                                        if m !=i and m!=j and m!=k and m!=l:
                                            for n in num:
                                                if n!=i and n!=j and n!=k and n!=l and n!=m :
                                                    for o in num:
                                                        if o!=i and o!=j and o!=k and o!=l and o!=l and o!=m and o!=n:
                                                            for p in num:
                                                                if p!=i and p!=j and p!=k and p!=l and p!=l and p!=m and p!=n and p!=o :
                                                                    for q in num :
                                                                        if q!=i and q!=j and q!=k and q!=l and q!=m and q!=n and q!=o and q!=p :
                                                                            quadrado =[i,j,k,l,m,n,o,p,q]
                                                                            if verify(quadrado):
                                                                                quadrados.append(quadrado)
        return quadrados
    quadrados=magicos() 
    print(f"Existem {len(quadrados)}quadrados magicos de 3x3 co numeros de 1 a 9:")          
    for quadrado in quadrados:
        print(f"{quadrado[0]} {quadrado[1]} {quadrado[2]}") 
        print(f"{quadrado[3]} {quadrado[4]} {quadrado[5]}")
        print(f"{quadrado[6]} {quadrado[7]} {quadrado[8]}")
        print()

