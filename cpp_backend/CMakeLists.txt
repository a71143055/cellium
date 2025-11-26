cmake_minimum_required(VERSION 3.15)
project(sim_core LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
find_package(pybind11 REQUIRED)

pybind11_add_module(sim_core src/sim_core.cpp)
target_include_directories(sim_core PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/include)
