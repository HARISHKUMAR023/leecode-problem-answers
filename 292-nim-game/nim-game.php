class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function canWinNim($n) {
          if($n%4 == 0){
            return false;
        }
        else{
            return true;
        }
    }
}