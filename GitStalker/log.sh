#!/bin/bash

# call git log on repositories and get formatted output
# store that output in a file using file redirection

currentDir=$(pwd)

paths=($@)
# echo ${paths[*]}

names=()
for i in ${paths[*]}
do
    x=${i%/*}
    x=${x##*/}
    names=("${names[@]}" $x)
done

# call git log with a specific output format, and store output in respective file
# put an empty line at beginning of file to allow Python script to find filename
# (important for later)
declare -i x=0
for i in $@
do
    cd $i
    git log --format="%H, %P, %an, %ae, %ad, %s, %b ====" | awk -F'\n' '{printf "%s", $1}' | awk -F'\r' '{gsub(/\'\r'/, " "); print}' | awk -F'====' '{ gsub(/\====/, "\n"); print }' >> $currentDir/${names[$x]}.txt
    cd $currentDir
    x+=1
done



# git log --format="%s, %b ====" | awk -F'-$' '{ printf "%s", sep $1; sep=/-$/?"":OFS } END{ print "" }' | awk -F'====' '{gsub(/\====/, "\n"); print}'
# git log --format="%s, %b ====" | awk -F'\n' '{printf "%s", $1}'  | awk -F'====' '{gsub(/\====/, "\n"); print}'
# git log --format="%H, %P, %an, %ae, %ad, %s, %b ====" | awk -F'\n' '{printf "%s", sep $1}' | awk -F'====' '{ gsub(/\====/, "\n"); print }'

