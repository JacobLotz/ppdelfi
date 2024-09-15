# Script for creating vertically stacked figures

cp 0000.png selection.png
#declare -a arr=("0007.png" "0014.png" "0022.png" "0029.png" "0037.png" "0044.png" "0052.png")
declare -a arr=("0014.png" "0029.png" "0044.png")

convert selection.png -shave 200x60 selection.png

for i in "${arr[@]}"
do
   echo "$i"
   cp $i precrop.png
   convert precrop.png -shave 200x60 precrop.png
   convert selection.png precrop.png\
            -size 10x10 xc:White +swap \
            -gravity Center -background White -append  selection.png
done
