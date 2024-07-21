/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
var rotateString = function(s, goal) {
    if (s.length !== goal.length) {
            return false;
        }
        
        let my = s.split('');
        
        for (let i = 0; i < my.length; i++) {
            if (my.join('') === goal) {
                return true;
            }
            my.push(my.shift());
        }
        
        return false;
};