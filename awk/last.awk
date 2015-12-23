# ADIL KHOKHAR
# CLID: axk9375
# CMPS 499
# Last script, filled with your choice of spaghetti code.
# Displays time-related statistics for the last command.
# Usage: awk -f last.awk <last file>
# 	 awk -f last.awk last.txt
# OR:	 last | awk -f last.awk

# Nothing to initialize.
BEGIN {
}
# If system boot or end of last command on record, skip.
{
if($2 == "system")
	{
	next;
	}
else if($1 == "wtmp")
	{
	next;
	}
# Remote usage, terminal was opened from remote user.
else if($2 ~ /pts.[0-9]/ && $3 != ":0.0")
	{
	# Get time, remove parenthesis.
	str = $10;
	days = 0;
	sub(/^\(/, "", str);
	sub(/\)/, "", str);

	# If user logged on for a day or more, throw it into days.
	if(str ~ /^[0-9]*\+/)
		{
		match(str, /(^[0-9]*)/, d);
		days = d[1];
		sub(/^[0-9]*\+/, "", str);
		}
	
	# Split ##:## up into an array.
	split(str,a,":");
	
	# Add back in time.	
	remote[$1] += ((days * 24 * 60) + (a[1] * 60) + a[2]);	
	}

# Local usage, terminal opened locally. Copy pasted code from above.
else if($2 == ":0" && $9 !="(00:00)")
	{
	str = $9;
	days = 0;
	sub(/^\(/, "", str);
	sub(/\)$/, "", str);
	if(str ~ /^[0-9]*\+/)
		{
		match(str, /(^[0-9]*)/, d);
		days = d[1];
		sub(/^[0-9]*\+/, "", str);
		}
	split(str,a,":");
	user[$1] += ((days * 24 * 60) + (a[1] * 60) + a[2]);
	}
else
	next;
}

# After processing records, print statistics.
END{

# Start with any user that has local usage or local + remote usage.
for (var in user)
	if(user[var] != 0)
		{
		# Convert all the minutes back into hours = minutes.
		minutes = user[var] % 60;
		hours = (user[var] - minutes) / 60;
		print "\tUser:",var,"\t\tTime:",hours,"hours and ", minutes, "minutes.";

		# If local + remote usage, print remote on next line.
		if(remote[var] != 0)
			{
			rmin = remote[var] % 60;
			rhr = (remote[var] - rmin) / 60;
			print "\tRemote Usage:", var, "\tTime:",rhr,"hours and ", rmin, "minutes.";	
			}
		}

# Copy pasted remote usage, except this is if any user has any remote usage.
for (var in remote)
	if(user[var] == 0)
	{
	rmin = remote[var] % 60;
	rhr = (remote[var] - rmin) / 60;
	print "\tRemote Usage:", var, "\tTime:",rhr,"hours and ", rmin, "minutes.";
	}

}
