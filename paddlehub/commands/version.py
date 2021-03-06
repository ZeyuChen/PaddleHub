# Copyright (c) 2019  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from paddlehub.common.logger import logger
from paddlehub import version
from paddlehub.commands.base_command import BaseCommand


class VersionCommand(BaseCommand):
    name = "version"

    def __init__(self, name):
        super(VersionCommand, self).__init__(name)
        self.show_in_help = True
        self.description = "Show PaddleHub's version."

    def exec(self, argv):
        print("hub %s" % version.hub_version)
        return True


command = VersionCommand.instance()
