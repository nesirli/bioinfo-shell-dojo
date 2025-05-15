cd shell-lesson-data/exercise-data/creatures

for filename in *.dat
do
    echo cp $filename original-$filename
done