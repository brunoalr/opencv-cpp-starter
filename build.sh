#!/bin/bash

# Exit on any error
set -e

echo "Building OpenCV C++ Starter with Conan..."

# Install dependencies with Conan
echo "Installing dependencies with Conan..."
conan install . --output-folder=build --build=missing

# Source Conan environment
echo "Setting up Conan environment..."
source build/conanbuild.sh

# Configure with CMake using Ninja and Conan toolchain
echo "Configuring with CMake..."
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -G Ninja -DCMAKE_TOOLCHAIN_FILE=build/conan_toolchain.cmake

# Build the project
echo "Building the project..."
cmake --build build -j$(nproc)

echo "Build completed successfully!"
echo "Executable location: build/bin/opencv_cpp_starter"
echo "To run: ./bin/opencv_cpp_starter"
