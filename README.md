# Fablib

Wrappers around Fabric for nicer usage as a library.

Each host is represented with and object called Machine, on which you can run
remote commands. It hides away the global `env` variable that gets used in
Fabric.

## Example:

    from fablib import Server, parallel_run

    server1 = Server('10.34.68.x', 'user1', '123456')
    server2 = Server('10.34.68.y', 'root', key_filename='~/key.pem')
    localhost = Server('localhost', password='123456')

    server1.run('echo "abc"')
    parallel_run([server1, server2, localhost], 'uname -a')
