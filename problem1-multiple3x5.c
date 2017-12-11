#include <stdio.h>
// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

// Find the sum of all the multiples of 3 or 5 below 1000.

int main(void)
{
int sum_multiple(int n);
printf("%d",sum_multiple(1000));
}
int steps;
int sum;
int sum_multiple(int n){
for( n=n-1;n>2;n--)
{
if(n%5==0||n%3==0)
{

sum = sum +n;

}

}
return sum;
}