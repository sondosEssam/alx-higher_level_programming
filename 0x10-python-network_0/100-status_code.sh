#!/bin/bash
#commment
curl curl -o /dev/null -s -w "%{http_code}\n"  "$1"
