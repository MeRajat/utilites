mkdir valid
# No of validation files
ls train |sort -R |tail -100 |while read file; do
    mv train/$file valid/
done
#  create sample data to verify algorithm/ neural net
mkdir -p sample/train
mkdir -p sample/valid 
# 100 is number of sample files in train
ls train |sort -R |tail -100 |while read file; do  
    mv train/$file sample/train
done
# 20 is no of valid files 
ls train |sort -R |tail -20 |while read file; do
    mv train/$file sample/valid
done
