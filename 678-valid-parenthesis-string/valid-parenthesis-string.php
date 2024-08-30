class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function checkValidString($s) {
        $min = 0;
        $max = 0;
        $length = strlen($s); // Get the length of the string

        for ($i = 0; $i < $length; $i++) {
            if ($s[$i] == '(') {
                $min += 1;
                $max += 1;
            } else if ($s[$i] == ')') {
                $min -= 1;
                $max -= 1;
            } else { // $s[$i] == '*'
                $min -= 1;
                $max += 1;
            }

            if ($min < 0) {
                $min = 0;
            }

            if ($max < 0) {
                return false;
            }
        }

        return $min == 0;
    }
}
