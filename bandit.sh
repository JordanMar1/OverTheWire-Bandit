#!/bin/sh

for file in $(ls task*.py | sort -V); do
    python3 "$file"
done