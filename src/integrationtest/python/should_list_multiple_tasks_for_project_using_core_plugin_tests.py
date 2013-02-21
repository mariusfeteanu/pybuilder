#  This file is part of Python Builder
#
#  Copyright 2011-2013 PyBuilder Team
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import unittest

from integrationtest_support import IntegrationTestSupport

class Test (IntegrationTestSupport):
    def test (self):
        self.write_build_file("""
from pybuilder.core import use_plugin

use_plugin("core")
        """)
        reactor = self.prepare_reactor()

        tasks = reactor.get_tasks()

        self.assertEquals(8, len(tasks))

        task_names = list(map(lambda task: task.name, tasks))

        self.assertTrue("clean" in task_names)
        self.assertTrue("publish" in task_names)

if __name__ == "__main__":
    unittest.main()
