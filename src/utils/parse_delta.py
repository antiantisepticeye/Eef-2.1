from datetime import datetime, timedelta

def parse_delta(delta: timedelta) -> str:
	s = delta.seconds
	days, remainder_1 = divmod(s, 3600 * 24)
	hours, remainder_2 = divmod(remainder_1, 3600)
	minutes, seconds = divmod(remainder_2, 60)
	retrun_str = ""

	if days > 0:
		retrun_str += f"{days} days"
	
	if hours > 0:
		string_to_be_added = f"{hours} hours"
		if days > 0: string_to_be_added = ", " + string_to_be_added
		if len(retrun_str) + len(string_to_be_added) < 20:
			retrun_str += string_to_be_added
	
	if minutes > 0:
		string_to_be_added = f"{minutes} minutes"
		if hours > 0: string_to_be_added = ", " + string_to_be_added
		if len(retrun_str) + len(string_to_be_added) < 20:
			retrun_str += string_to_be_added
	
	if seconds > 0:
		string_to_be_added = f"{seconds} seconds"
		if minutes > 0: string_to_be_added = ", " + string_to_be_added
		if len(retrun_str) + len(string_to_be_added) < 20:
			retrun_str += string_to_be_added

	
	return retrun_str
