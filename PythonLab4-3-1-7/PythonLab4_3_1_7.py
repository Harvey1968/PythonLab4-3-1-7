# 4.3.1.7 LAB: How many days: writing and using your own functions

# Defines the 'is_year_leap' function
def is_year_leap(year):
	# if the year number isn't divisible by four, it's a common year;
	if year % 4:
		return False
	# if the year number isn't divisible by 100, it's a leap year;
	elif year % 100:
		return True
	# if the year number isn't divisible by 400, it's a common year;
	elif year % 400:
		return False
	# Otherwise, it's a leap year.
	else:
		return True

def days_in_month(year, month):
	# if the year or month is out of scope return None.
	if (year < 1582) or (month < 1) or (month > 12):
		return None
	# Total days of each month in chronological order.
	day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	# Leap year + Febuary = 29 days:
	leap = day[month -1]
	if month == 2 and is_year_leap(year):
		leap = 29
	return leap

# "Short testing code" ;; Expanded to include more test cases:
test_years = [1900, 2000, 2016, 1987, 1985, 1581, 2012, 1600]
test_months = [2, 2, 1, 11, 12, 5, 2, 13]
test_results = [28, 29, 31, 30, 0, 31, 28, 5]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	da = test_results[i]					# da added so it too can be output,
	print(yr, mo, da, "-> ", end="")		# to aid in examining the testing code.
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")	# Also, results from year or month being out of scope # None 

