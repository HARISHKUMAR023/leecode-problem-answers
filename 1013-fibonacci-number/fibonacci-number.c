

int fib(int n){
if (n <= 1){
            return n;
        }
            
        int last=fib(n-1);
        int f=fib(n-2);
        return last+f;
}