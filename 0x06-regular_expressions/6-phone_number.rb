#!/usr/bin/env ruby

re = /^\d{10}$/

puts ARGV[0].scan(re).join
