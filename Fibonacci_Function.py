def fib(n,a=0,b=1): #0,1: val. par defaut     
     '''n-th term of Fibonacci sequence...
     starting at a,b.'''#tutoriel de fib
     a, b = 0, 1
     for i in xrange(n):
         a,b=b,a+b
     return a