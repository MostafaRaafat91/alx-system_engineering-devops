#!/usr/bin/env ruby
#Auth: Mostafa R
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
