cd data/untrimmed_fastq

for filename in *.fastq
do
    count=0
    while IFS= read -r line && (( count < 100 ))
    do
        if [[ "$line" =~ ^(@SRR[^[:space:]]+) ]]; then
            echo "${BASH_REMATCH[1]}"
            ((count++))
        fi
    done < "$filename"
done