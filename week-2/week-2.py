# Question.1

def calculate(min, max):
	sum = 0
	for i in range (min, max + 1):
		sum += i
		i += 1
	print(sum)

calculate(1,3)
calculate(4,8)

# ==========================================

# Question.2

def avg(data):
	count = data["count"]
	sum = 0
	for e in data["employees"]:
		sum += e["salary"]

	avg_salary = sum / count
	print(avg_salary)


avg(
	{
		"count":3,
		"employees":[
			{
				"name": "John",
				"salary": 30000
			},
			{
				"name": "Bob",
				"salary": 60000
			},
			{
				"name": "Jenny",
				"salary": 50000
			}
		]
	})

# ==========================================

# Question.3

def maxProduct(nums):
	prod_list = []
	for i in range(0, len(nums)):	
		for j in range(i + 1, len(nums)):
			prod_list.append(nums[i] * nums[j])
	print(max(prod_list))
				
maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([-1, 2])
maxProduct([-1, 0, 2])
maxProduct([-1, -2, 0])

# ==========================================

# Question.4

def twoSum(nums, target):
	for i in range(0, len(nums)):
		for j in range(i + 1, len(nums)):
			if nums[i] + nums[j] == target:
				return([i, j])

result = twoSum([2, 11, 7, 15], 9)
print(result)

# ==========================================

# Question.5

def maxZeros(nums):
	count = 0
	count_list = []
	for i in nums:
		if i == 1:
			count = 0
		else:
			count += 1
			count_list.append(count)

	if len(count_list) != 0:
		print(max(count_list))
	else:
		print(0)

maxZeros([0, 1, 0, 0])
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])
maxZeros([1, 1, 1, 1, 1])
maxZeros([0, 0, 0, 1, 1])
