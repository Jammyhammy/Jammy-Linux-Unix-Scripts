#!/bin/sh
# Adil Khokhar
# axk9375
# CMPS 499
# user script for assignment 4


#Prompt for name of roster file
echo -n "Enter name of roster file IE, roster:"
read filename
echo $filename


#Prompt for name of course
echo -n "Enter course name IE, MATH143:"
read course
echo $course


#Prompt for course section number
echo -n "Enter course section number IE, 001:"
read section
echo $section


#Initialize the variables
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


echo $homedir

for i in $homeuser
do
	mkdir -p $homedir/$i
	outfile0=" .profile"
	echo $profile >> $homedir/$i/"$outfile0"
done

#One giant awk command to process the roster.
roster=`echo $homedir | awk -v homedir=$homedir < $filename 'BEGIN{userid = 1000;}{ printf "%s::%d:1000:%s%s:%s\\\%s\\\:loginsh\n", $1, userid, $3, $2, homedir, $1; userid++; }END{}'`

echo "$roster" >> passwd

#todoTrap for interrupt
#todo restrict users

