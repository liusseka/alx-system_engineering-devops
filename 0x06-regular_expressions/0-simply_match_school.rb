#!/usr/bin/env ruby

# Ensure we have the required command-line argument
if ARGV.length != 1
  puts "Usage: ./0-simply_match_school.rb <text>"
  exit(1)
end

# Retrieve the text to search from the command-line
text_to_search = ARGV[0]

# The simple regular expression to match the word "School"
regex = /School/

# Check for a match within the provided text
if text_to_search =~ regex
  puts text_to_search
end
