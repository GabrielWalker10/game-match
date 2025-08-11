add_library(database_lib
    src/save_server/save_types.h
    src/save_server/Save.h
    src/save_server/Save.cpp)

find_package(PkgConfig REQUIRED)

# 利用pkg-config寻找库
pkg_check_modules(thrift REQUIRED thrift)

# 寻找库
target_link_libraries(database_lib
    PUBLIC thrift)

# 寻找头文件
target_include_directories(database_lib
    PUBLIC src/save_server/)

# 添加可执行文件
add_executable(database
    src/database.cpp)