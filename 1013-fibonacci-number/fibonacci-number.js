/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    if (n <= 1){
            return n;
        }
            
        let last=fib(n-1);
        let f=fib(n-2);
        return last+f;
};