#!/usr/bin/bash

read folderName
mkdir "$folderName"

cd "$folderName"

for i in {1..5}
do
	touch "file$i.txt"
done

for file in *.txt
do
	folder="${file%.txt}"
	mkdir "$folder"
	ln -s "../$file" "$folder/$file"
done
