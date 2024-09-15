rm -r cropped legend

mkdir cropped
mkdir legend
convert 0000.png -crop 180x380+80+20 -resize 75% legend/legend.png 

#convert test.png legend.png -thumbnail x25 -geometry  +0+0 -composite

for d in * ; do
    convert $d -crop 1000x562+390+234 cropped/$d
    convert $d -crop 180x380+80+20 -resize 75% legend/legend.png
    convert cropped/$d legend/legend.png -geometry  +0+0 -composite -matte cropped/$d
done


cd cropped
ffmpeg -r 30 -f image2 -s 1920x1080 -i %04d.png -vcodec libx264 -crf 15  -pix_fmt yuv420p vid.mp4
ffmpeg -stream_loop 8 -i vid.mp4 -c copy vid-loop.mp4
cd ..