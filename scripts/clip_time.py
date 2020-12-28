#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 11:39:38 2020
Finding the time between start and end points
@author: Rahul Venugopal
"""
#%%
# Get input from user
start_time = input('Enter start time: ')
end_time = input('Enter end time: ')

start_hours = start_time[0:2]
start_minutes = start_time[2:4]
start_seconds = start_time[4:6]

end_hours = end_time[0:2]
end_minutes = end_time[2:4]
end_seconds = end_time[4:6]

start_seconds = int(start_hours)*60*60 + int(start_minutes)*60 + int(start_seconds)

end_seconds = int(end_hours)*60*60 + int(end_minutes)*60 + int(end_seconds)

actual_duration = end_seconds - start_seconds

clip_hours = actual_duration // 3600

minutes_duration = actual_duration - clip_hours*3600

clip_minutes = minutes_duration // 60

clip_seconds = minutes_duration - clip_minutes*60

clip_time = "{:02d}".format(clip_hours) + ":" + "{:02d}".format(clip_minutes) + ":" + "{:02d}".format(clip_seconds)

print('The total clip duration in hh:mm:ss is ')
print(clip_time)

# ffmpeg -ss 07:05:24 -i Sketch.mp4 -t 00:14:56 -c copy rvg.mp4