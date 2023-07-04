#!/usr/bin/env ruby

re = /hb?tn/

puts ARGV[0].scan(re).join
