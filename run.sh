#! /usr/bin/sh

script_path="$( realpath "$0" )"
script_dir="$( dirname $script_path )"
cd "$script_dir/src"
../.venv/bin/python -m http.server
