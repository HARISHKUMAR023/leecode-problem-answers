/**
 * @param {string} s
 * @return {boolean}
 */
var checkValidString = function(s) {
        let min = 0;
        let max =0;
        for (let i =0; i< s.length;i++){
            if(s[i] == '('){
                min+=1;
                max+=1;
            }else if (s[i]== ')'){
                min-=1;
                max-=1;
            }else{
                min-=1;
                max+=1;
            }
            if(min < 0){
                min = 0 ; 
            }
            if(max < 0 ){
                return false;
            }
        }
        return min == 0 ;
};