# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
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

"""This script is used to synthesize generated parts of this library."""
import synthtool as s
from synthtool import gcp

gapic = gcp.GAPICGenerator()


#----------------------------------------------------------------------------
# Generate error_reporting client
#----------------------------------------------------------------------------
library = gapic.py_library(
    'error_reporting',
    'v1beta1',
    config_path='/google/devtools/clouderrorreporting'
                '/artman_errorreporting.yaml',
    artman_output_name='error-reporting-v1beta1')

s.move(library / 'google/cloud/errorreporting_v1beta1/proto')
s.move(library / 'google/cloud/errorreporting_v1beta1/gapic')

# Fix up imports
s.replace(
    'google/**/*.py',
    r"from google.devtools.clouderrorreporting_v1beta1.proto import ",
    r"from google.cloud.errorreporting_v1beta1.proto import ",
)