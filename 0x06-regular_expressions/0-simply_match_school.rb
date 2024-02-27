#!/usr/bin/env ruby

# Ensure we have the required command-line argument
if ARGV.length != 1
  puts "Usage: ./0-simply_match_school.rb <text>"
  exit(1)
end

# Retrieve the text to search from the command-line
text = ARGV[0]

# The simple regular expression to match the word "School"
regex = /\bSchool\b/

# Check for a match within the provided text
matches = text.scan(regex)

# Output all matches found
puts matches.join('')