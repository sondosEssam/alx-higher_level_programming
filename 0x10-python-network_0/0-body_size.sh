#!/bin/bash
#commment
url=$1
curl -s "$1" | wc -c
