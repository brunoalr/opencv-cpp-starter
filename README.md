# OpenCV C++ Starter

A starter project for OpenCV development in C++ using CMake build system.

## Prerequisites

- CMake (version 3.10 or higher)
- C++ compiler (GCC, Clang, or MSVC)
- OpenCV library

### Installing OpenCV

#### macOS (using Homebrew)
```bash
brew install opencv
```

#### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install libopencv-dev
```

#### Windows
Download and install OpenCV from [opencv.org](https://opencv.org/releases/)

## Building the Project

1. Create a build directory:
```bash
mkdir build
cd build
```

2. Configure with CMake:
```bash
cmake ..
```

3. Build the project:
```bash
make
```

## Project Structure

```
opencv-cpp-starter/
├── CMakeLists.txt      # CMake configuration
├── src/
│   └── main.cpp        # Main source file
├── hello.png           # Sample image
├── README.md           # This file
└── LICENSE             # MIT License
```

## Usage

After building, run the executable:
```bash
./opencv_cpp_starter
```

## Development

This is a starter template. You can:
- Add more source files in the `src/` directory
- Modify `CMakeLists.txt` to add new dependencies
- Add test images in the project root
- Extend the functionality in `main.cpp`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
