/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParityII = function(nums) {
    let oddptr = 1
    let evenptr = 0
    
    while(oddptr < nums.length && evenptr < nums.length){
        if(nums[oddptr] % 2 != 0){
            oddptr += 2
        } else if (nums[evenptr] % 2 == 0){
            evenptr += 2
        } else if (nums[oddptr] % 2 == 0 && nums[evenptr] % 2 != 0){
            let temp = nums[oddptr]
            nums[oddptr] = nums[evenptr]
            nums[evenptr] = temp
        }
    }
    return nums
};