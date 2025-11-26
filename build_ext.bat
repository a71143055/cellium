@echo off
setlocal

if not exist build mkdir build
cd build

cmake .. -A x64 -DCMAKE_BUILD_TYPE=Release
cmake --build . --config Release

cd ..
echo Build finished.
