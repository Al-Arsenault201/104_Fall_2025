import random

def get_nums():
    scores = []
    for i in range(500):
        scores.append(random.randint(1,100))
    return scores
    # print (scores)

def calc_mean(nums):
    total = 0.
    for n in nums:
        total += n
    return total/len(nums)

def calc_std_dev(nums):
    v = 0
    xbar = calc_mean(nums)
    for n in nums:
        v = v + (n - xbar)**2
    sd = (v/ len(nums))**(1/2)
    return sd

def calc_median(nums):
    nums.sort()
    size = len(nums)
    midpos = size//2
    if size%2 == 0:
        median = (nums[midpos] + nums[midpos+1])/2
    else:
        median = nums[midpos]
    return median

if __name__ == "__main__":
    grades = get_nums()
    print ("the grades are: ", grades)
    mean = calc_mean(grades)
    print("the average grade is ", mean)
    sd = calc_std_dev(grades)
    print("the standard deviation of the grades is: ", sd)
    median = calc_median(grades)
    print("the median grade is: ", median)

