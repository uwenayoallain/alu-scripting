#!/usr/bin/env ruby

from = ARGV[0].scan(/from:(.*?)\]/).flatten[0]
to = ARGV[0].scan(/to:(.*?)\]/).flatten[0]
flags = ARGV[0].scan(/flags:(.*?)\]/).flatten[0]
puts [from, to, flags].join(',')
