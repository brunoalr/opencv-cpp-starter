# OpenCV C++ Starter

A simple C++ project template for getting started with OpenCV.

## Prerequisites

- CMake (version 3.16 or higher)
- C++ compiler (GCC, Clang, or MSVC)
- OpenCV (installed on your system)

### Installing OpenCV

#### macOS
```bash
brew install opencv
```

#### Ubuntu/Debian
```bash
sudo apt-get install libopencv-dev
```

#### Windows
Download and install OpenCV from [opencv.org](https://opencv.org/releases/)

## Building the Project

1. Create a build directory and configure:
```bash
mkdir build
cd build
cmake ..
```

2. Build the project:
```bash
cmake --build .
```

## Running the Application

After building, you can run the application:

```bash
cd build
./bin/opencv_cpp_starter
```

The application will create a simple image file called `hello.png` in the current directory.

## Project Structure

```
opencv-cpp-starter/
├── CMakeLists.txt      # CMake configuration
├── src/
│   └── main.cpp        # Main source file
├── README.md           # This file
└── LICENSE             # MIT License
```

## Troubleshooting

### Common Issues

1. **OpenCV not found**: Make sure OpenCV is installed and CMake can find it
2. **CMake errors**: Ensure you're using CMake 3.16 or higher
3. **Build errors**: Check that your C++ compiler supports C++17

### Platform-Specific Notes

- **macOS**: OpenCV installed via Homebrew should be found automatically
- **Linux**: System-installed OpenCV should be found automatically
- **Windows**: You may need to set `OpenCV_DIR` environment variable to point to your OpenCV installation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
