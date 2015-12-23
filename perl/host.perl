#!/usr/bin/perl

use Socket;
use Sys::Hostname;
my $host = hostname();
($name, $aliases, $addrtype, $length, @addrs) = gethostbyname $host;
print "Host name is $name\n";
print "Aliases are $aliases\n";
print "Type is $addrtype\n";
print "Length is $length\n";
foreach (@addrs){  print "IP: ".join( '.', unpack( 'C4', $_ ) )."\n"; }
