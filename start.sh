#!/bin/bash

sleep 2

open -a "Google Chrome" http://127.0.0.1:8000/ &

python3 -m mkdocs serve
