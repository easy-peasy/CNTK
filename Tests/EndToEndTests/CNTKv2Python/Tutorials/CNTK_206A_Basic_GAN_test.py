# Copyright (c) Microsoft. All rights reserved.

# Licensed under the MIT license. See LICENSE.md file in the project root
# for full license information.
# ==============================================================================

import os
import sys
import pytest
import re
import numpy as np

abs_path = os.path.dirname(os.path.abspath(__file__))
notebook = os.path.join(abs_path, "..", "..", "..", "..", "Tutorials", "CNTK_206A_Basic_GAN.ipynb")

def test_cntk_206A_basic_gan_noErrors(nb):
    if os.getenv("OS")=="Windows_NT" and sys.version_info[0] == 2:
        pytest.skip('tests with Python 2.7 on Windows are not stable in the CI environment. ')
    errors = [output for cell in nb.cells if 'outputs' in cell
              for output in cell['outputs'] if output.output_type == "error"]
    assert errors == []

# TODO: Enable the test once the results can be deterministically determined
# expectedEvalErrorByDeviceId = { -1: 5.0, 0: 5.0 }

#def test_cntk_206A_basic_gan_evalCorrect(nb, device_id):
#    testCell = [cell for cell in nb.cells
#                if cell.cell_type == 'code' and re.search('# Print the generator loss', cell.source)]
#    assert len(testCell) == 1
#    m = re.match(r"Training loss of the generator is: (?P<actualEvalError>\d+\.\d+)\r?$", testCell[0].outputs[0]['text'])
    
#    assert (float(m.group('actualEvalError')) > expectedEvalErrorByDeviceId[device_id]) 
  