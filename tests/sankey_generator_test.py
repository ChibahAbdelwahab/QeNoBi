import os

import pytest

from core.data_api.sankey_generator import SankeyGenerator
from settings.settings import GROUPS_FOLDER


def test_sankey_generator():
    sg = SankeyGenerator()
    input_file = "M-12-[1-2]-[sex]-lcm.out"
    e = sg.sankey_preprocessing(input_file, keep_all_groups_in_periods=[])
    assert os.path.isfile(f"{GROUPS_FOLDER}/{input_file}")


if __name__ == '__main__':
    pytest.main(["-vv", __file__])
