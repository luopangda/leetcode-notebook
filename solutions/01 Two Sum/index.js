let twoSum = function(nums, target) {
    let tempArray = {};
    for (let i = 0; i<nums.length; i++){
        let diff = target - nums[i];
        if(tempArray[diff] !== undefined){
            return [ tempArray[diff], i];
        }else {
            tempArray[nums[i]] = i
        }
    }
};
let result = twoSum([2,7,11,15], 9);
console.log(result);
