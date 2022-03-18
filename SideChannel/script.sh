#!/bin/bash
for i in {00000001..99999999}; do
    out=$(eval "./pin_checker <<< $i")
    if [[ "$out" == *"granted"* ]]; then
        echo $i
        break
    fi
done