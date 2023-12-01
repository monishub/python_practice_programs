def sqrt(n):
    approx=0.5*n
    better=0.5*n(approx+n/approx)
    while better!=approx:
        approx=better
        better=0.5*n(approx+n/approx)
    return approx
a=int(input())
print("sqrt:",sqrt(a))
        
