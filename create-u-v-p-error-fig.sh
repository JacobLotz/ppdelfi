# In order to create a figure with the u and v velocities we have to make 4 crops
# 1) With the u velocity field
# 2) With the v velocity field
# 3) With the legend of the u velocity
# 4) With the legend of the v velocity
# 
# Then we have to do 3 appends:
# 1) Append the two legends
# 2) Append the two velocity fields
# 3) Append the legends and velocityfields


# Create working directory

mkdir workingdir;

# ********************************
# Create cropped images
# *******************************

dir1="slices-error-zoom-u"
dir2="slices-error-zoom-v"
dir3="slices-error-zoom-p"

dirfinal="slices-error-uvp"
rm -r $dirfinal

echo "Step 1/11: error field u"
mkdir -p workingdir/crop-u
cd $dir1
for d in * ; do
    convert $d -crop 1620x352+300+335 ../workingdir/crop-u/$d
done
cd ..;

echo "Step 2/11: error field v"
mkdir -p workingdir/crop-v
cd $dir2
for d in * ; do
    convert $d -crop 1620x352+300+335 ../workingdir/crop-v/$d
done
cd ..;

echo "Step 3/11: error field p"
mkdir -p workingdir/crop-p
cd $dir3
for d in * ; do
    convert $d -crop 1620x352+300+335 ../workingdir/crop-p/$d
done
cd ..;

echo "Step 4/11: whitespace between velocityfields"
mkdir -p workingdir/whitespace
cd $dir2
for d in * ; do
    convert $d -crop 1620x12+300+0 ../workingdir/whitespace/$d
done
cd ..;

echo "Step 5/11: legend z"
mkdir -p workingdir/legend-z
cd $dir1
for d in * ; do
    convert $d -crop 300x50+0+15 ../workingdir/legend-z/$d
done
cd ..;

echo "Step 6/11: legend u"
mkdir -p workingdir/legend-u
cd $dir1
for d in * ; do
    convert $d -crop 300x310+0+95 ../workingdir/legend-u/$d
done
cd ..;

echo "Step 7/11: legend v"
mkdir -p workingdir/legend-v
cd $dir2
for d in * ; do
    convert $d -crop 300x360+0+65 ../workingdir/legend-v/$d
done
cd ..;

echo "Step 8/11: legend p"
mkdir -p workingdir/legend-p
cd $dir3
for d in * ; do
    convert $d -crop 300x360+0+65 ../workingdir/legend-p/$d
done
cd ..;


# ********************************
# Merge figures
# *******************************
echo "Step 9/11: merging legends"
mkdir -p workingdir/legend-total
cd workingdir/legend-u
for d in * ; do
    convert -append ../legend-z/$d $d ../legend-v/$d ../legend-p/$d ../legend-total/$d
done
cd ../..;

echo "Step 10/11: merging velocityfields and whitespace"
mkdir -p workingdir/field-total
cd workingdir/crop-u
for d in * ; do
    convert -append $d ../whitespace/$d ../crop-v/$d ../whitespace/$d ../crop-p/$d ../field-total/$d
done
cd ../..;

echo "Step 11/11: Merge legends and velocityfields"
mkdir $dirfinal
cd workingdir/legend-total
for d in * ; do
    convert +append $d ../field-total/$d ../../$dirfinal/$d
done
cd ../..;


# Clean up
rm -r workingdir;

# Create video
cd $dirfinal
ffmpeg -r 30 -f image2 -s 1920x1080 -i %04d.png -vcodec libx264 -crf 15  -pix_fmt yuv420p vid.mp4
cd ..
