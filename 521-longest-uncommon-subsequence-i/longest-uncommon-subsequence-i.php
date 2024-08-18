class Solution {

    /**
     * @param String $a
     * @param String $b
     * @return Integer
     */
    function findLUSlength($a, $b) {
        if ($a == $b) {
            return -1; // Missing semicolon
        } else {
            return max(strlen($a), strlen($b)); // Missing semicolons and corrected variable names
        } 
    }
}
