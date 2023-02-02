#!/bin/env/zsh
echo "Running $1 on the matrix"
if [ -z "$(ls -A /mnt/d)" ]; then
    # Can't access the drive until it's mounted 
    sudo mount -t drvfs D: /mnt/d; 
fi
cp $1 code.py
cp -r -t /mnt/d/ code.py