#!/bin/bash

# Cleanup
echo removing older protogen
rm -rf ./src/logic/protogen
mkdir ./src/logic/protogen

# Protogen
echo generating protogen
python -m grpc_tools.protoc -I./proto --python_out=./src/logic/protogen --grpc_python_out=./src/logic/protogen ./proto/user.proto
python -m grpc_tools.protoc -I./proto --python_out=./src/logic/protogen --grpc_python_out=./src/logic/protogen ./proto/group.proto
python -m grpc_tools.protoc -I./proto --python_out=./src/logic/protogen --grpc_python_out=./src/logic/protogen ./proto/student.proto
python -m grpc_tools.protoc -I./proto --python_out=./src/logic/protogen --grpc_python_out=./src/logic/protogen ./proto/teacher.proto

echo Ok