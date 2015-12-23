#!/usr/bin/env ruby
# Adil Khokhar
# CLID: axk9375
# CMPS 499 Ruby Assignment

# The mySwitch class provides a switch object

class MySwitch

#	Constructor Function:
#	Default Constructor
	def initialize( hash )
		@hash = Hash.new {|k, v| k[v] = Proc.new{ puts "Exec DefaultCase" }}
		@hash['default'] = Proc.new {puts "Executing default case"}
		@storebreak = Array.new
		@breakname = Array.new
		@storebreak.push('default')
		@breakname.push(0)
	end
#	addCase:
#	Add a case name and the associated block of code to the hash.
	def addCase( name, fallthr, &ablk )
		puts "Adding case #{name}"
		@hash[name] = ablk
		if fallthr == 1
			@storename.push(name)
		end
		printCase()
	end
#	getCase:
#	Get the case name and the associated block of code, and if there are any args to pass to the block of the 
#	code, pass those args.
	def getCase( name, arg )
		puts "Calling case #{name}"
		@hash[name].call(arg)
	end

#	printCase:
#	Prints out all the current cases in the hash.	

	def printCase()
		puts "List of proc objects in hash:"
		puts @hash.inspect
	end
end

# Start main script.
# Create and initialize a new mySwitch object and create test cases.
# You must create a new object using mySwitch.new ( hash ), example below 
s = MySwitch.new( hash )

# To add cases, use objname.addCase( case name, break value ) { (block of code here to represent code in switch statement) }
s.addCase(1, 0){ |i| 2.times { puts i} }
s.addCase(2, 0){ |i| puts i+i }
s.addCase(3, 0){ |i| puts i*i }
s.addCase(4, 0){ |i| puts i }


# To get a case and execute the following block of code, use objname.getCase( case name, any args to pass to the code ). Following are examples.
s.getCase(1, 'This is a case')
s.getCase(4, 'Yup')
s.getCase(2, 1)
s.getCase(3, 1)
s.getCase(1, 'This is the same case but with something else')
s.getCase('default', 'This is the default case')

# Breaks are unimplemented. If they were implemented, breakname would store the cases in an array.
# If the user specifies that there is to be no break by putting in s.addCase(1, 1) { block } then
# the code would fall through and execute previous switch cases until it reaches a case where the
# break is specified.


