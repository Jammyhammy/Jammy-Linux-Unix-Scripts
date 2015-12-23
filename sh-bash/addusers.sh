#!/bin/sh
# Adil Khokhar
# axk9375
# CMPS 499
# user script for assignment 4

#Doesn't work to check authorized user. It will always exit.
#if [ $USER != "root" ] || [ $USER != "axk9375" ] || [ $USER != "crs2411" ] || [ $USER != "user" ]
#then
#	echo "Error: $USER is not crs2411, root, user, or axk9375"
#	exit 2
#fi

#Trap for interrupts
trap '' 2


#Prompt for name of roster file
echo -n "Enter name of roster file IE, roster:"
read filename


#Prompt for name of course
echo -n "Enter course name IE, MATH143:"
read course


#Prompt for course section number
echo -n "Enter course section number IE, 001:"
read section

#Initialize variables and format the homedir.

homesec=`echo $section | cut -c 3`
homedir=$course$homesec
homeuser=`awk < $filename '{ print $1 }'`
profiler="if [ \"$TERM\" = \"\" ]then
        if /bin/i386
        then
                TERM=sun-color
        else
                TERM=xterm
        fi
        export TERM
fi"

#Create first userid

userid=1000

#Read in roster file

while read nameid last first
do
	#Would be passfile="${passfile}${nameid}::${userid}:1000:${first}${last}:${homedir}/${nameid}:pts1\n"
	#But for some reason \n does not work, but having an actual newline does.
	#For login shell, we will assume it is /bin/sh.
	passfile="${passfile}${nameid}::${userid}:1000:${first} ${last}:${homedir}/${nameid}:/bin/sh\n"
	#Increment userid
	userid=`expr $userid + 1`
	#Create user directory
	mkdir -p $homedir/$nameid
	#Create initial profile file, strange bug here, it should work by just having ".profile" 
	#but this causes an abrupt stop in the shell script on this version of CentOS (5.6) 
	#So we have to include in a space for it to work, that's why it's " .profile"
	outfile0=" .profile"
	echo "$profiler" > $homedir/$nameid/"$outfile0"
	echo "Created ${homedir}/${nameid}";
done < $filename 

#Create passwd file.

echo "$passfile" > passwd

trap 2

#todo restrict users/

