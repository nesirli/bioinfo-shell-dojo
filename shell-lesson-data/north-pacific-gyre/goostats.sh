#Process experiment files in the directory
for datafile in NENE*A.txt NENE*B.txt
do 
  echo $datafile stats-$datafile
done
