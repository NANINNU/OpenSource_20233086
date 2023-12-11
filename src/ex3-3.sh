#!/usr/bin/bash

read weight height

bmi=$(($weight / ($height / 100 * $height / 100)*10))

if [ $bmi -lt 185 ]; then
	echo "저체중입니다"
elif [ 185 -ge $bmi ] && [ $bmi -lt 230 ]; then
	echo "정상체중입니다"
elif [ 230 -ge $bmi ] && [ $bmi -lt 250 ]; then 
	echo "과체중입니다"
elif [ 250 -ge $bmi ]; then
	echo "비만입니다"
fi
