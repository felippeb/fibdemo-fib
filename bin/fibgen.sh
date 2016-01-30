#!/bin/bash

num=$1

if [ "${num}" == 0 ]; then
    echo "well then why did you ask me to run in the first place?"
elif [ "${num}" == 1 ]; then
    echo "You have input 1. Calculating fibonacci to 1 digits:"
    echo "position in sequence: 1"
    echo "fib number in this position: 1"
elif [ "${num}" -lt 0 ]; then
    echo "You have entered a number below 0, please enter a positive integer"
else
    echo "You have input ${num}. Calculating fibonacci to ${num} digits starting at 1:"
    prevnum=0
    curnum=1
    fibseq=()
    for n in $(seq 2 "${num}"); do
        if [ "${n}" == 2 ]; then
            echo -n "1 "
        fi
        fibnum=$(echo ${curnum}+${prevnum} | bc)
        fibseq+=("${fibnum}")
        export prevnum=${curnum}
        export curnum=${fibnum}
    done
    echo "${fibseq[@]}"
fi
