#!/usr/bin/env ruby

re = /hbt{2,5}n/
str = ARGV[0]

puts str.scan(re).join
