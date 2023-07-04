#!/usr/bin/env ruby

re = /[A-Z]/

puts ARGV[0].scan(re).join
