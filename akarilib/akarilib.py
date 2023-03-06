# AkariLib - AkariSpecification's Python Lib
# Author: Takahashi Akari <akaritakahashioss@gmail.com>
# License: MIT License Copyright (c) 2023 Takahashi Akari <akaritakahashioss@gmail.com>
# Version: 0.0.0
# Date: 2023-03-06
# Python: 3.10.9
# Description: AkariLib - AkariSpecification's Python Lib

# You can run your source code on other computers using the SSH protocol.
# Use the Fabric library.
# This library is AkariSpecification's Python library.
# This library is released under the MIT license.

import fabric

def rsaConnection(host, username, key_filename):
    return fabric.Connection(host, user=username, connect_kwargs={"key_filename": key_filename})

def passwordConnection(host, username, password):
    return fabric.Connection(host, user=username, connect_kwargs={"password": password})

def disconnect(connection):
    return connection.close()

def run(connection, command):
    return connection.run(command)

def sudo(connection, command):
    return connection.sudo(command)

def put(connection, local, remote):
    return connection.put(local, remote)

def get(connection, remote, local):
    return connection.get(remote, local)

def putFiles(connection, local, remote):
    return connection.put(local, remote, recursive=True)

def getFiles(connection, remote, local):
    return connection.get(remote, local, recursive=True)
