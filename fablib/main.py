#!/usr/bin/env python
#
# Copyright (c) 2013 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#           http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import fabric.api as fab
import logging

LOG  = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

TIMEOUT = 2*60
REBOOT_TIMEOUT = 5*60

class Server(object):
    def __init__(self, host, user=None, password=None, key_filename=None):
        self.host = host
        if user:
            self.host = user + '@' + host
        fab.env.hosts.append(self.host)
        fab.env.passwords[self.host] = password
        fab.env.use_ssh_config = True
        fab.env.key_filename = key_filename
        LOG.info('Fabric env:\n%s' % fab.env)

    def run(self, command, timeout=TIMEOUT, *kwargs):
        @fab.task
        def task():
            fab.run(command)
        fab.execute(task, host=self.host)

    def reboot(self, timeout=REBOOT_TIMEOUT):
        pass

    def ping(self, count=3):
        pass

    def wait_until_connective(self, timeout=TIMEOUT):
        pass

    def get(self, remote_path, local_path=None):
        pass

    def put(self, local_path, remote_path):
        pass


def run(servers, command, timeout=TIMEOUT):
    """Run a command on all given servers in sequence."""
    hosts = [m.host for m in servers]
    @fab.task
    @fab.serial
    def task():
        fab.run(command)
    fab.execute(task, hosts=hosts)


def parallel_run(servers, command, timeout=TIMEOUT):
    """Run a command on all given servers in parallel."""
    hosts = [m.host for m in servers]
    @fab.task
    @fab.parallel
    def task():
        fab.run(command)
    tmp = fab.env.linewise
    fab.env.linewise = True
    fab.execute(task, hosts=hosts)
    fab.env.linewise = tmp
