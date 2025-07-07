import os
os.system("cat cpp_source/example.cpp | ollama run codellama:latest -f instructions/initial_prompt.yaml > tests/example_test.cpp")
os.system("cd build && cmake .. && make && ./runTests")
os.system("lcov --capture --directory . --output-file coverage.info")
os.system("genhtml coverage.info --output-directory coverage")
