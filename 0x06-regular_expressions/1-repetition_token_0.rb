#!/usr/bin/env ruby

input_string = ARGV[0]

matches = input_string.scan(/hbt{2,5}n/)

puts matches.join