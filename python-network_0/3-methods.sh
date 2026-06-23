#!/bin/bash
# Displays allowed HTTP methods
curl -sI -X OPTIONS "$1" | grep -i Allow | cut -d' ' -f2-
