#!/usr/bin/env ruby

re = /hbt{1,4}n/

puts ARGV[0].scan(re).join
