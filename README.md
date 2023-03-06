# AkariLib
AkariLib - AkariSpecification's Python Lib for HPC

## Installation
```bash
pip install git+https://github.com/AkariSpecification/AkariLibrary
```

## Usage
```python
from akarilib import akarilib

# SSH Connection
connection = akarilib.rsaConnection("hostname","username", "id_rsa")

# SSH Command Execution
result = akarilib.run(connection, "ls -l")
print(result)

# SSH File Transfer
akarilib.put(connection, "local_file", "remote_file")

# SSH File Download
akarilib.get(connection, "remote_file", "local_file")

# SSH Files(Directory) Transfer
akarilib.putFiles(connection, "local_dir", "remote_dir")

# SSH Files(Directory) Download
akarilib.getFiles(connection, "remote_dir", "local_dir")

# Example
# Execute GCC Compile in Remote Host
result = put(connection, "/home/localuser/hello.c", "/home/remoteuser/hello.c")
print(result)
result = akarilib.run(connection, "cd /home/remoteuser/")
print(result)
result = akarilib.run(connection, "gcc -o hello hello.c")
print(result)
# Run Remote Host's Executable File
result = akarilib.run(connection, "./hello")
print(result)

# Close SSH Connection
akarilib.disconnect(connection)
```

## License
MIT License (c) 2023 AkariSpecification
