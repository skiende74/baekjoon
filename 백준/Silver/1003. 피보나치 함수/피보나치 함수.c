#include <stdio.h>

int main()
{
    int a[2][41];

for (int n=0;n<=40;n++)
{
    if (n==0)
    {
        a[0][n]=1;
        a[1][n]=0;
    }
    else if (n==1)
    {
        a[0][n]=0;
        a[1][n]=1;
    }
    else
    {
        a[0][n]=a[0][n-1]+a[0][n-2];
        a[1][n]=a[1][n-1]+a[1][n-2];
    }
}
int N;
scanf("%d",&N);
int input[N];
for (int k=0;k<N;k++)
{
    scanf("%d",&input[k]);
}
for (int k=0;k<N;k++)
{
    printf("%d %d\n",a[0][input[k]],a[1][input[k]]);
}
}