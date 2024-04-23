#!/usr/bin/env ruby

# Capture the argument passed from the command line
argument = ARGV[0]

# Apply the regular expression to scan for strings matching the pattern
matches = argument.scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)

# Print the joined matches
puts matches.join(',')

