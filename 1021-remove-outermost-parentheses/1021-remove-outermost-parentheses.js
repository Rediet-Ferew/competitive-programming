/**
 * @param {string} s
 * @return {string}
 */
var removeOuterParentheses = function(s) {
    let num = 0;
    let valid = '';
    for(let i = 0; i < s.length; i++){
        if (s[i] === '('){
            if (num > 0)
                valid += s[i]
            num += 1
        }else{
          if(num > 1)
              valid += s[i]
            num -= 1
        }
    }
    return valid
};