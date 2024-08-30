class Solution {
public:
    bool checkValidString(string s) {
        int min = 0;
        int max =0;
        for (int i =0; i< s.size();i++){
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
    }
};