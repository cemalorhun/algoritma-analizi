#include<stdio.h>
#include<time.h>
int Fibonacci(int);
 
main()
{
   clock_t start, end;

   start=clock();
   
   int n, i = 0, c;
   
   printf("Fibonacci series=> ");
   scanf("%d",&n);
 
   for ( c = 1 ; c <= n ; c++ )
   {
      printf("%d\n", Fibonacci(i));
      i++; 
   }
   
   end = clock();

   printf("Gecen Sure: %f",(double)(end-start)/CLOCKS_PER_SEC);
 
   return 0;
}
 
int Fibonacci(int n)
{
   if ( n == 0 )
      return 0;
   else if ( n == 1 )
      return 1;
   else
      return ( Fibonacci(n-1) + Fibonacci(n-2) );
}
 
