# OpenCV C++ Starter

> **Disclaimer**: This project was vibe coded using [Cursor](https://cursor.sh), an AI-powered code editor.

A simple C++ project template for getting started with OpenCV.

## Prerequisites

- CMake (version 3.16 or higher)
- C++ compiler (GCC, Clang, or MSVC)
- OpenCV (installed on your system)

### Installing OpenCV

#### macOS
```bash
# Using Homebrew (recommended)
brew install opencv

# Alternative: Using MacPorts
sudo port install opencv
```

#### Ubuntu/Debian
```bash
# Update package list
sudo apt-get update

# Install OpenCV development libraries
sudo apt-get install libopencv-dev

# Optional: Install additional OpenCV modules
sudo apt-get install libopencv-contrib-dev
```

#### CentOS/RHEL/Fedora
```bash
# Fedora
sudo dnf install opencv-devel

# CentOS/RHEL 8+
sudo dnf install opencv-devel

# CentOS/RHEL 7
sudo yum install opencv-devel
```

#### Windows
1. **Using Chocolatey:**
   ```bash
   choco install opencv
   ```

2. **Manual installation:**
   - Download OpenCV from [opencv.org](https://opencv.org/releases/)
   - Extract to a directory (e.g., `C:\opencv`)
   - Set environment variable `OpenCV_DIR` to point to the build directory
   - Add OpenCV bin directory to your PATH

## Building the Project

### Option 1: Using CMake (Default)

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

### Option 2: Using xmake (Alternative)

xmake is a modern build system that can automatically handle dependencies and provide a simpler build experience.

1. **Install xmake:**
   ```bash
   curl -fsSL https://xmake.io/shget.text | bash
   ```
   Or visit: https://xmake.io/#/getting_started?id=installation

2. **Build with xmake:**
   ```bash
   # Using the build script
   ./build_xmake.sh
   
   # Or directly with xmake
   xmake config
   xmake build
   ```

3. **Run with xmake:**
   ```bash
   # Build and run in one command
   ./build_xmake.sh run
   
   # Or directly
   xmake run
   ```

## Running the Application

After building, you can run the application:

```bash
# CMake build
cd build
./bin/opencv_cpp_starter

# xmake build
./build/xmake/bin/opencv_cpp_starter
```

The application will create a simple image file called `hello.png` in the current directory.

## Project Structure

```
opencv-cpp-starter/
├── CMakeLists.txt      # CMake configuration
├── xmake.lua           # xmake configuration
├── build_xmake.sh      # xmake build script
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
4. **xmake not found**: Install xmake using the provided installation command
5. **xmake package errors**: xmake will automatically download and configure OpenCV if not found on your system

### Platform-Specific Notes

- **macOS**: OpenCV installed via Homebrew should be found automatically. If using MacPorts, you may need to set `CMAKE_PREFIX_PATH`.
- **Linux**: System-installed OpenCV should be found automatically. For custom installations, set `OpenCV_DIR` to the cmake directory.
- **Windows**:
  - For manual installation, set `OpenCV_DIR` environment variable to point to the build directory (e.g., `C:\opencv\build`)
  - Add OpenCV bin directory to your PATH environment variable

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
