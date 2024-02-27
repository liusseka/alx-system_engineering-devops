#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: ./1-repetition_token_0.rb <text>"
  exit(1)
end

text = ARGV[0]
regex = ^(.).*(.).*\1$

if text =~ regex
  puts text
end