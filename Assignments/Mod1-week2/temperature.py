# print('Today it 90 F in California')

# s = set('rat')
# t = set('car')

# print(s,t)

# if s == t:
#     print('true')
# else:
#     print('false')   

from collections import defaultdict    

def groupAnagrams(strs):
    from collections import defaultdict
    result = defaultdict(list)

    for word in strs:
        result[tuple(sorted(word))].append(word)
    print(result)
    return result.values() 

strs = ["eat","tea","tan","ate","nat","bat"]
#print(groupAnagrams(strs))

def isHappy(n) :

        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen :
            seen.add(n)
            n = get_next(n)

        return n == 1

#print(isHappy(7))

def containsNearbyDuplicate(nums, k) :
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:
                if abs(i - seen[nums[i]]) <= k:
                    return True
                else:
                    return False
            else:
                seen[nums[i]] = i

#print(containsNearbyDuplicate())   
# 
def threeSum(nums):
        res  = set()
        seen = {}
        #iterate though the array
        for i, val1 in enumerate(nums):
            # iterate i+1 next elements
            for j , val2 in enumerate(nums[i+1:]):
                complement = -val1 - val2
                if complement in seen and seen[complement] == i:
                    res.add(tuple(sorted((val1, val2, complement))))
                seen[val2] = i    
        return res   

nums = [-1,0,1,2,-1,-4]
#print(threeSum(nums))  
# 
def intToRoman(num):
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]

        roman_digit = []

        for value , symbol in digits:

            if num == 0 : break

            count , num = divmod(num, value)
            roman_digit.append(symbol * count)
        return "".join(roman_digit)    

num = 3
#print(intToRoman(num))    

def trap( height):
        left = 0
        right = len(height) - 1
        left_max , right_max = 0, 0
        ans = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]

                else:
                    ans += left_max - height[left]
                left += 1        

            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1 

        return ans
height =[0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))