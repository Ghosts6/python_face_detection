#!/bin/bash

# macOS
if [ "$(uname)" == "Darwin" ]; then
    if ! command -v brew &> /dev/null; then
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    brew install openblas
    brew install opencv
    brew install cmake
# linux
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    sudo apt-get update
    sudo apt-get install -y libopencv-dev
    sudo apt-get install -y cmake
else
    echo "Unsupported operating system"
    exit 1
fi
pip install numpy && pip install numpy===1.21.2
pip install py-agender face_recognition
