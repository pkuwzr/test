#!/bin/bash

cd $1
for f in `ls`; do
    if [ -d $f ]; then
        cd $f
        grep -irq 'jquery' .
        if [ $? = 0 ]; then
            echo $f
        fi
        cd ..
    fi
done
