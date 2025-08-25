#!/bin/bash

# xmake build script for OpenCV C++ Starter
set -e

echo "Building OpenCV C++ Starter with xmake..."

# Check if xmake is installed
if ! command -v xmake &> /dev/null; then
    echo "Error: xmake is not installed."
    echo "Please install xmake first:"
    echo "  curl -fsSL https://xmake.io/shget.text | bash"
    echo "  or visit: https://xmake.io/#/getting_started?id=installation"
    exit 1
fi

# Clean previous build (optional)
if [ "$1" = "clean" ]; then
    echo "Cleaning previous build..."
    xmake clean
    exit 0
fi

# Install required packages
echo "Installing required packages..."
xrepo install -y opencv libavif

# Configure and build
echo "Configuring project..."
xmake config

echo "Building project..."
xmake build

echo "Build completed successfully!"

# Run the executable if requested
if [ "$1" = "run" ]; then
    echo "Running executable..."
    xmake run
fi
