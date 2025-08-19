cmake_minimum_required(VERSION 3.16)
project(opencv_cpp_starter LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(OpenCV REQUIRED)

add_executable(opencv_cpp_starter src/main.cpp)
target_include_directories(opencv_cpp_starter PRIVATE ${OpenCV_INCLUDE_DIRS})
target_link_libraries(opencv_cpp_starter PRIVATE ${OpenCV_LIBS})
set_target_properties(opencv_cpp_starter PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
