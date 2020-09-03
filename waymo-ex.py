# Write a function that takes in a list/array of maintenance events in chronological order and returns true if all maintenance was processed correctly. Otherwise, return false.

# A MaintenanceEvent is a snapshot of maintenance performed on a self-driving car. When maintenance is started or completed, we capture that in a MaintenanceEvent.

# A MaintenanceEvent can be open, signaling the maintenance is actively ongoing, or can be closed, signaling the maintenance has been completed.
# A car can have multiple, unique, open maintenance.
# If maintenance was properly processed, then:

# MaintenanceEvents were opened/closed in the correct sequence.
# A maintenance was closed after it was opened.
# Any maintenance that was opened at some point in the future was closed.
# There was no duplicate open maintenance of the same type for a car.


class MaintenanceEvent(object):
    def __init__(self, state, car_id, work_type, timestamp):
        self.state = state # 1 means open, 0 means close
        self.car_id = car_id
        self.work_type = work_type
        self.timestamp = timestamp

def IsProcessedCorrectly(events):
	"""Returns True if events have been processed correctly."""
	
	tracker = {}
	
	for event in events:
		if event.car_id in tracker:
			open_events = tracker[event.car_id] 
			removed_event = False

			for open_event in open_events:
				if event.work_type == open_event.work_type and event.state != open_event.state:
					if open_event.timestamp < event.timestamp:
						open_events.remove(open_event)
						removed_event = True

			if not removed_event:
				if event.state == 1:
					tracker[event.car_id].append(event)
				else:
					return False

	for key in tracker:
		if key.values == []:
			return True
		else: 
			return False
	
	else:
		tracker[event.car_id] = [event]


assert(IsProcessedCorrectly(
    [MaintenanceEvent(1, 809, "oil",  1000),
     MaintenanceEvent(1, 600, "tires", 1000),
     MaintenanceEvent(1, 809, "filter", 1015),
     MaintenanceEvent(0, 809, "oil", 1030),
     MaintenanceEvent(0, 809, "filter", 1045),
     MaintenanceEvent(0, 600, "tires",1200)]))

assert(not IsProcessedCorrectly(
    [MaintenanceEvent(1, 81, "brakes",1000), # not closed
     MaintenanceEvent(1, 82, "fuel",  1000),
     MaintenanceEvent(0, 82, "fuel",  1030),
     MaintenanceEvent(0, 82, "oil",   1200)])) # not opened

# assert(!ProcessedCorrectly({{1, 11, "wash",  1000},
#                               {1, 12, "filter",1000},
#                               {0, 12, "filter",1030},
#                               {1, 12, "oil",   1200}, # not closed
#                               {0, 11, "wash",  1200},
#                               {1, 13, "tires", 1200}})); # not closed

# assert(!ProcessedCorrectly({{1, 8099, "wash", 800},
#                               {1, 6780, "fuel", 830},
#                               {1, 8099, "wash", 840}, # duplicate
#                               {0, 6780, "fuel", 845},
#                               {0, 8099, "wash", 1100}}));


#----------------------------PSEUDOCODE--------------------------



#{809: [MaintenanceEvent(1, 809, "oil",  1000), MaintenanceEvent(1, 809, "filter", 1015), MaintenanceEvent(0, 809, "oil",  1030), MaintenanceEvent(0, 809, "filter", 1045)]

#checking if event.car_id is a key in tracker, save event at event.car_id

#check if work type is already in key, check that state is different, if state is 1, save timestamp_opn, state is 0, save timestamp_cls, if timestamp_opn < timestamp_cls, remove events
#check dictionary for values at each existing key, as long as they're all empty, return true, return false

# for each event
#   # see if we have events for the car
    # if yes
       # for each open event
          # do more stuff





