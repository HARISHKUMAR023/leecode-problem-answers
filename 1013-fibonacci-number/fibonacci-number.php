class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function fib($n) {
        if ($n <= 1){
            return $n;
        }
            
      
        $last = $this->fib($n - 1);
        $f = $this->fib($n - 2);
        return $last+ $f;
    }
}