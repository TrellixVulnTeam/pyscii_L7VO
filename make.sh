#!/usr/bin/bash

printf "
  _____        _____      _ _   _____           _        _ _ 
 |  __ \      / ____|    (_|_) |_   _|         | |      | | |
 | |__) |   _| (___   ___ _ _    | |  _ __  ___| |_ __ _| | |
 |  ___/ | | |\___ \ / __| | |   | | | '_ \/ __| __/ _' | | |
 | |   | |_| |____) | (__| | |  _| |_| | | \__ \ || (_| | | |
 |_|    \__, |_____/ \___|_|_| |_____|_| |_|___/\__\__,_|_|_|
         __/ |                                             
        |___/
"

cd ./GeckoDriver
wget https://github.com/mozilla/geckodriver/releases/tag/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
tar -C /usr/local/bin/ -xvf

currentPath=$(pwd)
export PATH=$PATH:$currentPath
