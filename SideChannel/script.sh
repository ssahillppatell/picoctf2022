#!/bin/bash
for i in 48390510 48390511 48390512 48390513 48390514 48390515 48390516 48390517 48390518 48390519; do
    out=$(eval "./pin_checker <<< $i")
    echo $i
    ./timescript.sh <<< $i
done