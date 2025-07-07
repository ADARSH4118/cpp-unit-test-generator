 cmake_minimum_required(VERSION 3.10)
project(UnitTestGen)

set(CMAKE_CXX_STANDARD 17)

enable_testing()

include_directories(/usr/include)

file(GLOB SRC_FILES "cpp_source/*.cpp")
file(GLOB TEST_FILES "tests/*.cpp")

add_executable(runTests ${SRC_FILES} ${TEST_FILES})
target_link_libraries(runTests gtest pthread)
add_test(NAME RunAllTests COMMAND runTests)
