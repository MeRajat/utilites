# This file creates validation dataset and create a sample for sanity check of the model
# It assumes data is in 


mkdir valid
# No of validation files
ls train |sort -R |tail -100 |while read file; do
    cp train/$file valid/
done
#  create sample data to verify algorithm/ neural net
mkdir -p sample/train
mkdir -p sample/valid 
# 100 is number of sample files in train
ls train |sort -R |tail -100 |while read file; do  
   cp train/$file sample/train
done
# 20 is no of valid files 
ls train |sort -R |tail -20 |while read file; do
    cp train/$file sample/valid
done



# When train data contains folder for different category
for dir in train/*/
do
    dir=${dir%*/}
    echo ${dir##*/}
    mkdir -p "valid/${dir##*/}"
    ls "train/${dir##*/}" |sort -R |tail -20 |while read file; do
    	mv "train/${dir##*/}/$file" "valid/${dir##*/}"
	done
done
