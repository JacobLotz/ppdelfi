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
rm -r slices-uv
mkdir workingdir;

# ********************************
# Create cropped images
# *******************************

# Velocity field u
echo "Step 1/8"
mkdir -p workingdir/crop-u
cd slices-zoom-u
for d in * ; do
    convert $d -crop 1620x534+300+273 ../workingdir/crop-u/$d
done
cd ..;

# Velocity field v
echo "Step 2/8"
mkdir -p workingdir/crop-v
cd slices-zoom-v
for d in * ; do
    convert $d -crop 1620x534+300+273 ../workingdir/crop-v/$d
done
cd ..;

# whitespace between velocityfields
echo "Step 3/8"
mkdir -p workingdir/whitespace
cd slices-zoom-v
for d in * ; do
    convert $d -crop 1620x12+300+0 ../workingdir/whitespace/$d
done
cd ..;

# Legend u
echo "Step 4/8"
mkdir -p workingdir/legend-u
cd slices-zoom-u
for d in * ; do
    convert $d -crop 300x640+0+0 ../workingdir/legend-u/$d
done
cd ..;

# Legend v
echo "Step 5/8"
mkdir -p workingdir/legend-v
cd slices-zoom-v
for d in * ; do
    convert $d -crop 300x440+0+100 ../workingdir/legend-v/$d
done
cd ..;




# ********************************
# Merge figures
# *******************************
# Mergin legends
echo "Step 6/8"
mkdir -p workingdir/legend-total
cd workingdir/legend-u
for d in * ; do
    convert -append $d ../legend-v/$d ../legend-total/$d
done
cd ../..;

# Merging velocityfields and whitespace
echo "Step 7/8"
mkdir -p workingdir/field-total
cd workingdir/crop-u
for d in * ; do
    convert -append $d ../whitespace/$d ../crop-v/$d ../field-total/$d
done
cd ../..;

# Merge legends and velocityfields
echo "Step 8/8"
mkdir slices-uv
cd workingdir/legend-total
for d in * ; do
    convert +append $d ../field-total/$d ../../slices-uv/$d
done
cd ../..;


# Clean up
rm -r workingdir;

# Create video
cd slices-uv
ffmpeg -r 30 -f image2 -s 1920x1080 -i %04d.png -vcodec libx264 -crf 15  -pix_fmt yuv420p vid.mp4
cd ..