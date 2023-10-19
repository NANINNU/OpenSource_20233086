#!/usr/bin/bash

read num1 operator num2

if [ $operator = '+' ] ; then
        result=$(($num1 + $num2))
elif [ $operator = '-' ] ; then
        result=$(($num1 - $num2))
fi

echo $result
