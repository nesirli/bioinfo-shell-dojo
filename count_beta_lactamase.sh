grep -i "beta-lactamase" data/amr_genes.fasta >> beta-lactamase.txt
grep -i "beta-lactamase" data/amr_genes.fasta | wc -l
count=$(grep -i "beta-lactamase" data/amr_genes.fasta | wc -l)
echo "beta-lactamase:$count" >> amr_counts.txt