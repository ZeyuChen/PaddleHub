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

import argparse

from paddlehub.common.logger import logger
from paddlehub.common import utils
from paddlehub.common.downloader import default_downloader
from paddlehub.common.hub_server import default_hub_server
from paddlehub.commands.base_command import BaseCommand, ENTRY


class DownloadCommand(BaseCommand):
    name = "download"

    def __init__(self, name):
        super(DownloadCommand, self).__init__(name)
        self.show_in_help = True
        self.description = "Download PaddlePaddle pretrained model files."
        self.parser = self.parser = argparse.ArgumentParser(
            description=self.__class__.__doc__,
            prog='%s %s <module_name>' % (ENTRY, name),
            usage='%(prog)s [options]',
            add_help=False)
        # yapf: disable
        self.add_arg('--output_path',  str,  ".",   "path to save the model" )
        self.add_arg('--uncompress',   bool, False,  "uncompress the download package or not" )
        # yapf: enable

    def exec(self, argv):
        if not argv:
            print("ERROR: Please specify a model name\n")
            self.help()
            return False
        model_name = argv[0]
        model_version = None if "==" not in model_name else model_name.split(
            "==")[1]
        model_name = model_name if "==" not in model_name else model_name.split(
            "==")[0]
        self.args = self.parser.parse_args(argv[1:])
        if not self.args.output_path:
            self.args.output_path = "."
        utils.check_path(self.args.output_path)

        url = default_hub_server.get_model_url(
            model_name, version=model_version)
        if not url:
            tips = "can't found model %s" % model_name
            if model_version:
                tips += " with version %s" % model_version
            print(tips)
            return True

        if self.args.uncompress:
            result, tips, file = default_downloader.download_file_and_uncompress(
                url=url, save_path=self.args.output_path, print_progress=True)
        else:
            result, tips, file = default_downloader.download_file(
                url=url, save_path=self.args.output_path, print_progress=True)
        print(tips)
        return True


command = DownloadCommand.instance()
