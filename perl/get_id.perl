#!/usr/bin/perl


# IP address of room410
$ip = "130.70.40.21"; # IPV4 address.

# split it up into an array
@numbers = split(/\./, $ip);

# sanity check
if (scalar(@numbers) != 4)
{
    print "$ip is not a valid IP address.\n";
    next;
}

# convert to internal representation
$ip_addr = pack("C4", @numbers);

# First element of the array returned by gethostbyaddr is host name.
($name) = (gethostbyaddr($ip_addr, 2))[0];

# won't work if I call it with the original IP string format
($myname) = (gethostbyaddr($ip, 2))[0];

print "name is $name\n";
print "myname is $myname\n";
