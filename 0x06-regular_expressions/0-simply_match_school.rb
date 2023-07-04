#!/usr/bin/env ruby

re = /School/
str = ARGV[0]

puts str.scan(re).join
