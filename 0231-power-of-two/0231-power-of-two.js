/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    
    num = Math.log2(n);
    if (Number.isInteger(num)) {
        return true
    } else {
        return false
    }
    
};