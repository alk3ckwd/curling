#! /bin/bash
for i in {980..1049}; do
	if [ ! -d "./test$i" ]; then
		mkdir test$i
	fi 
	for j in {1..12}; do
		for k in {1..16}; do
			mv test${i}_${j}_${k}.jpg ./test$i
		done
	done
done