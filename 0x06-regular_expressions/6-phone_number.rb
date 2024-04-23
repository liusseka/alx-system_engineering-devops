#!/usr/bin/env ruby

# Capture the argument passed from the command line
input_string = ARGV[0]

# Apply the regular expression to scan for strings matching the pattern
matches = input_string.scan(/^\d{10}$/)

# Print the joined matches
puts matches.join