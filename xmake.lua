set_project("opencv_cpp_starter")
set_languages("c++17")

add_requires("opencv", "libavif")

target("opencv_cpp_starter")
    set_kind("binary")
    add_files("src/*.cpp")
    add_packages("opencv", "libavif")
    

