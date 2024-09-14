rm  large_file.csv

python3 create-big-data2.py

rm ./split/*

python3 split_large_file2.py

srun --mpi=pmix -n 4 python3 /clusterfs/big-data/mpi_sum5.py

python3 check2.py
