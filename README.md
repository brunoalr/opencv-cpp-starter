# OpenCV C++ Starter

> **Disclaimer**: This project was vibe coded using [Cursor](https://cursor.sh), an AI-powered code editor.

A simple C++ project template for getting started with OpenCV using xmake as the build system.

## Prerequisites

- xmake (modern build system that handles dependencies automatically)
- C++ compiler (GCC, Clang, or MSVC)
- OpenCV (automatically managed by xmake)
- Python 3 (for build script)

### Installing xmake

```bash
# Install xmake
curl -fsSL https://xmake.io/shget.text | bash

# Or visit: https://xmake.io/#/getting_started?id=installation
```

## Building the Project

xmake is a modern build system that automatically handles dependencies and provides a simpler build experience.

### Quick Start

1. **Build the project:**

   ```bash
   # Using the Python build script
   ./build_xmake.py
   
   # Or directly with xmake
   xmake config
   xmake build
   ```

2. **Run the application:**

   ```bash
   # Build and run in one command
   ./build_xmake.py run
   
   # Or directly
   xmake run
   ```

### Build Options

- **Clean build:** `./build_xmake.py clean` or `xmake clean`
- **Build and run:** `./build_xmake.py run` or `xmake run`
- **Install dependencies:** `xrepo install -y opencv libavif`

## Running the Application

After building, you can run the application:

```bash
# Using xmake
xmake run

# Or directly
./build/xmake/bin/opencv_cpp_starter
```

The application will create a simple image file called `hello.png` in the current directory.

## Build Script

This project provides a Python build script for cross-platform compatibility:

- **`build_xmake.py`**: Python script (cross-platform, requires Python 3)

The script provides the following commands:
- `./build_xmake.py` - Build the project
- `./build_xmake.py run` - Build and run
- `./build_xmake.py clean` - Clean build

## Dependencies

This project uses the following dependencies, automatically managed by xmake:

- **OpenCV**: Computer vision library
- **libavif**: AVIF image format support

xmake will automatically download and configure these dependencies if they're not found on your system.

## Troubleshooting

### Common Issues

1. **xmake not found**: Install xmake using the provided installation command
2. **xmake package errors**: xmake will automatically download and configure OpenCV if not found on your system
3. **Build errors**: Check that your C++ compiler supports C++20
4. **Permission errors**: Make sure the build script is executable: `chmod +x build_xmake.py`
5. **Python script errors**: Ensure Python 3 is installed and the script is executable

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
