cmake_minimum_required(VERSION 3.15)

project(game-match LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 11)

add_subdirectory(database)
add_subdirectory(match_system)