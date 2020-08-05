def alarmClock(setTime, timeToSet):
	shifts = 0
	
	if setTime == timeToSet:
		return 0
	
	#Code below extracts hour and minute in ints from setTime
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
	
	#Code below extracts hour and minute in ints from timeToSet
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
	
	#Code below calculates differences between setTime and timeToSet 
	if abs(setTime_hr - alarm_hr) <= 12:
		hr_shifts = abs(setTime_hr - alarm_hr)
			
	else:
		hr_shifts = (24 - setTime_hr) + alarm_hr
			
	if abs(setTime_mins - alarm_mins) <= 30:
			min_shifts = abs(setTime_mins - alarm_mins)
		
	else:
		min_shifts = (60 - setTime_mins) + alarm_mins

	shifts = hr_shifts + min_shifts
	
	return shifts
	
