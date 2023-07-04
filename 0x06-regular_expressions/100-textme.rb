#!/usr/bin/env ruby

re = /\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/
from_re = /\[from:.+?\]/

puts ARGV[0].scan(re).join(",")


