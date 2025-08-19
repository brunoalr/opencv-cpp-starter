cmake_minimum_required(VERSION 3.16)
project(opencv_cpp_starter LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Find packages using Conan
find_package(opencv REQUIRED)

add_executable(opencv_cpp_starter src/main.cpp)
target_link_libraries(opencv_cpp_starter PRIVATE opencv::opencv)
set_target_properties(opencv_cpp_starter PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
