find_package(PkgConfig REQUIRED)
find_package(Threads REQUIRED)
# 利用pkg-config寻找库
pkg_check_modules(thrift REQUIRED thrift)

# 创建match_server库
add_library(match_server_lib
    # 只需要.cpp文件
    src/match_server/match_types.cpp
    src/match_server/Match.cpp)

target_link_libraries(match_server_lib
    PRIVATE thrift
    PRIVATE Threads::Threads)

target_include_directories(match_server_lib
    PUBLIC src/match_server/)

# 创建save_client库
add_library(save_client_lib
    src/save_client/Save.cpp)

target_link_libraries(save_client_lib
    PRIVATE thrift)

target_include_directories(save_client_lib
    PUBLIC src/save_client/)

# 可执行文件
add_executable(match_system
    src/match_system.cpp)

target_include_directories(match_system
    PUBLIC src/match_server/
    PUBLIC src/save_client/)

target_link_libraries(match_system
    PRIVATE match_server_lib
    PRIVATE save_client_lib)