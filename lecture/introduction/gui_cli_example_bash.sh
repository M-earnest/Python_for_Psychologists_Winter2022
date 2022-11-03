#!/bin/bash
names=" pugsley gomez foster"

for name in $names
do
    mkdir -p /home/michael/Desktop/adams_family/$name
    cd /home/michael/Desktop/adams_family/$name
    for id in {1..10}
    do
        touch scooby_doo_$id.txt
    done
    mkdir /home/michaelDesktop/the_new_yorker
    for file in ./*
    do 
        file_id=$(echo "${file%.*}" | awk -F'[_.]' '{print $4}') 
        if [ $((file_id%2)) -eq 0 ];
        then
        mv $file /home/michael/Desktop/the_new_yorker/${file//.txt/_$name.txt}
        fi
    done
done