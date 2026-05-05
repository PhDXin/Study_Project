def equation(r1,r2,density,k):
    potential = ((4/3)*(3.1415926)*density*k*((1/2*r2**2+(r1**3)/r2)-(1/2*r1+(r1**3)/r1)))
    return potential
print(equation(float(input("r1:")),float(input("r2:")),float(input("density:")),float(input("k:"))))
