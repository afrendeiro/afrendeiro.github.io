---
layout: post
title: "Screencasting on Ubuntu - ffmpeg FTW!"
description: "Screencasting on Ubuntu - ffmpeg FTW!"
category: notebook
tags: [video, ubuntu, screencast]
---
{% include JB/setup %}


Sometimes I have to create recordings of a presentation beforehand for recruiting people (PhD program) or conferences.

I've used Zoom previously for this, but it was not very good.

Here's my little guide for creating high-quality screencast recordings on an Ubuntu Linux laptop.

It uses utilities like `guvcview`, `xprop`, `xdpyinfo`, and (of course) `ffmpeg` to customize and optimize the recording process.

The process is roughly like this:
 - Have a little window on your screen showing your camera always on top of any window (`guvcview`)
 - Record whole screen with `ffmpeg` (raw mkv full resolution)
 - Edit (trim) and convert to mp4 for sharing

`recordmydesktop` at first seemed like a good option but [it has a bug which ruined my recording :/](https://github.com/Enselic/recordmydesktop/issues/23).

## My setup (`guvcview`, `ffmpeg`)

### Display own video on screen
`guvcview` provides a very minimal camera window that is ideal for screencasts.
Run `guvcview` to get your own camera on the screen, select "Always on top" on its window, drag to corner.

#### Hide gnome top bar of guvcview window
`guvcview` uses the native window manager (gnome in Ubuntu) and this still has decorations (top bar window). Use `xprop` to temporarily remove the gnome top bar window:
Click on window to hide:
```bash
xprop -format _MOTIF_WM_HINTS 32c -set _MOTIF_WM_HINTS 2
```
Specify window name beforehand:
```bash
xprop -name 'Your window name' -format _MOTIF_WM_HINTS 32c -set _MOTIF_WM_HINTS 2
```

### Query display dimensions (for ffmpeg)
```bash
xdpyinfo | grep dimensions
```
Note: `xrandr | grep '*' ` does not work correctly in high dpi screens.

### Record desktop with `ffmpeg`, edit and convert with ffmpeg
```bash
RESOLUTION=5120x3200  # laptop screen
RESOLUTION=6144x3456  # external display
ffmpeg -f x11grab -framerate 30 -video_size $RESOLUTION -i $DISPLAY -f pulse -ac 2 -i default -c:v libx264 -preset ultrafast -crf 0 -c:a aac -strict experimental -b:a 128k output.mkv
```
This will output a massive video file in full quality (~4Gb per 10 min).

Downsample to 1080p and convert to mp4:
```bash
ffmpeg -i output.mkv -vf "scale=1920:-1" -c:v libx264 -preset slow -crf 22 -c:a aac output.mp4
```

Trim first 5 seconds re-encoding (better to re-encode otherwise it may not match a keyframe) - should've been done already from the mkv but forgot!
```bash
ffmpeg -ss 5 -i output.mp4 -c:v libx264 -preset fast -crf 22 -c:a aac -strict experimental output.trimmed.mp4
```

## Alternative: `recordmydesktop` (not recommended!)

```bash
recordmydesktop --no-frame --fps 30 --v_quality 22 --s_quality 10
```

Beware of this issue: https://github.com/Enselic/recordmydesktop/issues/23
Last time it meant my recording was unusable - none of the solutions online worked!

Trim the top and bottom 160 pixels
```bash
recordmydesktop --no-frame --fps 30 --v_quality 22 --s_quality 10 --width 5120 --height 3040 -y 160
```

