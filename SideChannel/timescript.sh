#!/bin/sh
start=`date +%s.%N`
./pin_checker
end=`date +%s.%N`

runtime=$( echo "$end - $start" | bc -l )
echo "time: $runtime"