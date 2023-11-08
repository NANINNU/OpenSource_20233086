#!/usr/bin/bash

if [ ! -f "DB.txt" ];then
	touch DB.txt
fi

while true; do
	echo "무엇을 하시겠습니까?( reset = 목록 초기화, exit = 종료 )"
	read command
	
	if [ "$command" == "exit" ]; then
		break
	elif [ "%command" == "reset" ]; then
		echo "파일이 초기화 되었습니다"
	else 
		read name
		read info
		echo "$name $info" >> DB.txt
	fi
done
