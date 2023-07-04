#!/usr/bin/env ruby

re = /^h.n$/

puts ARGV[0].scan(re).join
