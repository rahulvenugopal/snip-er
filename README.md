# snip-er
 CLI based simple video edits :scissors:

### Many a times I rely on multiple software (GUI based) to do simple video edits

Abhiram R (a friend of mine) wrote this [blogpost](https://abhiramr.com/2020-12-06-What-I-Learnt-FFMpeg/) recently - What I Learnt from 6 hours of tinkering with FFmpeg

### The goal of this repository is to have a set of commands which comes handy to do simple video edits like

1. Cut from specific start and end times in hh:mm:ss formats
2. Merging videos
3. Extract audio only
4. To be updated

```bash
ffmpeg -ss 05:01:10 -i original_video.mp4 -t 00:04:59 -c cut_video.mp4
```

Using ffmpeg, we can cut specific portions of a large video using above command (thanks to abhi)

We need to pass video length from start time in hh:mm:ss

I wrote a small script to find this elapsed time using python :snake:. Code [here](https://github.com/rahulvenugopal/snip-er/blob/main/scripts/clip_time.py)

## To Do

- Set up a batch mode script where start and end times are available as a .csv file and once we run the script, snip-er should cut automagically :angel:
- Adding logos/watermarks
- Merging videos





