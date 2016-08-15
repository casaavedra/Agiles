def recur_fibo(n):
   """Recursive function to
   print Fibonacci sequence"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("Hasta que numero desea la serie? "))

if nterms <= 0:
   print("El numero ingresado debe ser positivo y mayor a cero.")
else:
   print("Serie de Fibonacci:")
   for i in range(nterms):
       if recur_fibo(i) <= nterms:
           print(recur_fibo(i))
       else:
           break