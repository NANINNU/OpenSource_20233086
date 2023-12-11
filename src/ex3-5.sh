#!/usr/bin/bash

echo "프로그램을 시작합니다."
function inf(){
	echo "함수 안으로 들어왔음"
	local directory="$1"
	local option="$2"
	
	if [ -z "$directory" ]; then
		directory="."
	fi
	
	ls $options "$directory"
}

inf
echo "프로그램을 종료합니다"