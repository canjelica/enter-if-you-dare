"""dig clock change hour and min, one time to change from 7 to 830
one change eon hour and change on minute

given a time and target time, how many clicks to get to target time. can go backwards

"""
def set_alarm(time, alarm):
	#find difference between first two and last two digits
	#convert to string and split
	#find difference between hours, and minutes both ways
	#see which is smaller
	#add to total

	#test 0030, 1:30
	

	clicks = 0

	time_str = str(time)
	alarm_str = str(alarm)

	time_hr = time_str[0] + time_str[1]
	time_mins = time_str[2] + time_str[3]

	alarm_hr = alarm_str[0] + alarm_str[1]
	alarm_mins = alarm_str[2] + alarm_str[3]
	
	if alarm_hr != time_hr:
		hr_clicks = abs(int(time_hr) - int(alarm_hr))	
	else:
		hr_clicks = 0
	
	if alarm_mins != time_mins:
		mins_clicks = abs(int(time_mins) - int(alarm_mins))	
	else:
		mins_clicks = 0

	clicks = mins_clicks + hr_clicks

	return clicks


def alarmClock(setTime, timeToSet):
	shifts = 0
	
	if setTime == timeToSet:
		return 0
	
	setTime_hr = setTime[0] + setTime[1]
	if setTime_hr[0] == 0:
		setTime_hr = int(setTime_hr[1])
	else: 
		setTime_hr = int(setTime_hr)
			
	setTime_mins = setTime[3] + setTime[4]
	if setTime_mins[0] == 0:
		setTime_mins = int(setTime_mins[1])
	else: 
		setTime_mins = int(setTime_mins)
	
	alarm_hr = timeToSet[0] + timeToSet[1]   
	if alarm_hr[0] == 0:
		alarm_hr = int(alarm_hr[1])
	else:
		alarm_hr = int(alarm_hr)
	
	alarm_mins = timeToSet[3] + timeToSet[4]   
	if alarm_mins[0] == 0:
		alarm_mins = int(alarm_mins[1])
	else:
		alarm_mins = int(alarm_mins)
	
	if abs(setTime_hr - alarm_hr) <= 12:
		hr_shifts = abs(setTime_hr - alarm_hr)
			
	else:
		hr_shifts = 24 - alarm_hr
			
	
	if abs(setTime_mins - alarm_mins) <= 30:
			min_shifts = abs(setTime_mins - alarm_mins)
		
	else:
		min_shifts = (60 - setTime_mins) + alarm_mins

	shifts = hr_shifts + min_shifts
	
	return shifts
	

	# 13:48
	# 14:10

	# 1-27
	# 1+48

# Pseudocode:
	# parameters are strings
	# Need to split out the hour and minutes, convert to ints
	# Find difference between set hr and alarm hr, set mins and             alarm mins
	# Absolute value of difference
	# add differences to shifts


# Manual test:
# "07:30", "08:00"
# setTime_hr = "07"
# setTime_hr = 7
# setTime_mins = "30"
# setTime_mins = 30

# alarm_hr = "08"
# alarm_hr = 8
# alarm_mins = "00"
# alarm_mins = 0

# hr_shifts = abs(7 - 8) -> -1 -> 1
# min_shifts = abs(30-0) -> 30

#shifts = 1 + 30 -> 31
