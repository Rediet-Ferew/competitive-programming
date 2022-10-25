/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParity = function(nums) {
    for(let i = 0; i < nums.length; i++) {
        if (nums[i] % 2 === 0) {
            let num = nums[i];
            nums.splice(i, 1)
            nums.unshift(num)
        }
    
}
    return nums
};