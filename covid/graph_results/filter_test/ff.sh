#! /usr/bin/bash

ffmpeg -i cont-africa.png      -vf "scale=iw*.2:ih*.2" cont-africa-0.2.png
ffmpeg -i cont-all-v1.png      -vf "scale=iw*.2:ih*.2" cont-all-v1-0.2.png
ffmpeg -i cont-all-v2.png      -vf "scale=iw*.2:ih*.2" cont-all-v2-0.2.png
ffmpeg -i cont-all-v3.png      -vf "scale=iw*.2:ih*.2" cont-all-v3-0.2.png
ffmpeg -i cont-all-v4.png      -vf "scale=iw*.2:ih*.2" cont-all-v4-0.2.png
ffmpeg -i cont-asia.png        -vf "scale=iw*.2:ih*.2" cont-asia-0.2.png
ffmpeg -i cont-europe-test.png -vf "scale=iw*.2:ih*.2" cont-europe-test-0.2.png
ffmpeg -i cont-na-v1.png       -vf "scale=iw*.2:ih*.2" cont-na-v1-0.2.png
ffmpeg -i cont-na-v2.png       -vf "scale=iw*.2:ih*.2" cont-na-v2-0.2.png
ffmpeg -i cont-oceania.png     -vf "scale=iw*.2:ih*.2" cont-oceania-0.2.png
ffmpeg -i cont-sa.png          -vf "scale=iw*.2:ih*.2" cont-sa-0.2.png
