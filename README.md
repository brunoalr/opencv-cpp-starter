# OpenCV C++ Starter

A simple C++ project template for getting started with OpenCV using Conan package manager.

## Prerequisites

- CMake (version 3.16 or higher)
- C++ compiler (GCC, Clang, or MSVC)
- Conan package manager

### Installing Conan

If you don't have Conan installed, you can install it via pip:

```bash
pip install conan
```

## Building the Project

### Option 1: Using the Build Script (Recommended)

For convenience, you can use the provided build script:

```bash
./build.sh
```

This script will:
1. Install OpenCV and dependencies via Conan
2. Set up the Conan build environment
3. Configure the project with CMake using Ninja
4. Build the project using cmake --build
5. Place the executable in `build/bin/`

### Option 2: Manual Build

1. Install dependencies with Conan:
```bash
conan install . --output-folder=build --build=missing
```

2. Set up Conan environment:
```bash
source build/conanbuild.sh
```

3. Configure with CMake:
```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -G Ninja
```

4. Build the project:
```bash
cmake --build build
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
├── conanfile.txt       # Conan dependencies (OpenCV 4.12.0)
├── build.sh            # Build script
├── src/
│   └── main.cpp        # Main source file
├── README.md           # This file
└── LICENSE             # MIT License
```

## Why This Setup?

This project uses a modern, efficient build system combination:

- **Conan**: Manages C++ dependencies with prebuilt binaries when available
- **CMake 4.1.0**: Latest CMake with modern features and better IDE support
- **Ninja**: Fast, parallel build system that's significantly faster than Make
- **Modern CMake**: Uses `-S` and `-B` flags for cleaner, more portable builds
- **Cross-platform**: Works seamlessly on Windows, macOS, and Linux

## Configuration Details

### Conan Configuration

The project uses Conan for dependency management with the following configuration:

- **OpenCV Version**: 4.12.0 (latest stable)
- **CMake Version**: 4.1.0 (via Conan tool_requires)
- **Ninja Version**: 1.13.1 (via Conan tool_requires)
- **Profile**: Uses Conan's default profile (auto-detects system settings)
- **Build Strategy**: Hybrid approach using prebuilt binaries when available, building from source when needed
- **Build System**: Uses Ninja for fast, parallel builds

### Key Files

- **conanfile.txt**: Defines OpenCV as the main dependency and CMake as build requirement
- **CMakeLists.txt**: Configured to work with Conan-generated package configs

## Troubleshooting

### Common Issues

1. **Conan not found**: Make sure Conan is installed and in your PATH
2. **Build failures**: Try clearing Conan cache: `conan remove "*" -c`
3. **CMake errors**: Ensure you're using the correct generator and build type
4. **Ninja not found**: Ninja is automatically installed via Conan tool_requires

### Platform-Specific Notes

- **All platforms**: Uses Conan's default profile which auto-detects your system settings
- **Cross-platform**: Works automatically on any platform supported by Conan
- **Build performance**: Ninja provides faster incremental builds compared to Make

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
