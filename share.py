# You are given an array of prices where prices[i] is the price of a given stock on day 5.

# You want to maximize your profit by choosing one day to buy a stock and a different day in the future to sell that stock.

# Return the maximum profit you can make from this trade. If you can't make any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]

# Output: 5

# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

# Note that buying on day 2 and selling on day 1 are prohibited because you must buy before selling.
#________________________________________________________________________________________________________________________________
def share(arr):
    res = []                
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[i]:
                    # print("arr[i] and arr[j]: ", arr[j], arr[i])
                    # print(arr[j] - arr[i])
                    a = arr[j] - arr[i]
                    res.append(a)
    # print(res)
    if res == []:
        return 0
    return max(res)
list1 = [7, 1, 5, 3, 6, 7]
print(share(list1))