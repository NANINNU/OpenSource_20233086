#!/usr/bin/bash


read folderName

if [ ! -d "${folderName}" ]; then
	mkdir "${folderName}"
fi

cd "${folderName}"

for i in {1..5}
do
	touch "file$i.txt"
done

zip -r "${folderName}.zip" ./*

mkdir "${folderName}_unzip"
unzip "${folderName}.zip" -d "${folderName}_unzip"