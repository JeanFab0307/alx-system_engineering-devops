#!/usr/bin/env ruby
puts ARGV[0].scan(/\A\d\d{9}\Z/).join
