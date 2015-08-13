#!/bin/bash
#This script run every 15 seconds
while (sleep 1 && python /home/admin/plotly/plot.py) &
do
  wait $!
done