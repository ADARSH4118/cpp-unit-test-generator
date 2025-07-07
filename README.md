# 🚀 C++ Unit Test Generator using AI (Ollama + CodeLLaMA)

This project uses a local LLM (CodeLLaMA via Ollama) to automatically generate unit tests for any C++ application. It supports test refinement, error recovery, and code coverage analysis using GNU tools.

---

## 🧠 Key Features

- 🧪 **Unit Test Generation**: LLM creates initial Google Test cases
- 🔁 **Refinement & Debugging**: Improve tests based on feedback & build errors
- 📊 **Coverage Analysis**: Measure test effectiveness using `lcov`
- ⚙️ **Automation**: YAML prompts and shell/Python script for streamlined flow

---

## 📁 Project Structure

cpp-unit-test-generator/
├── cpp_source/ # Original C++ files
├── tests/ # AI-generated test files
├── instructions/ # YAML prompts for LLM
├── build/ # (ignored) Build files
├── scripts/ # (optional) Automation scripts
├── CMakeLists.txt # Build instructions
└── report.md # Final coverage report
