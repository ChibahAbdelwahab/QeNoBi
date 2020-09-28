import pytest

from core.data_api.dataset_handler import DatasetHandler
from settings.settings import TRANSACTIONS_REQUIRED_FIELDS


def test_data():
    dh = DatasetHandler()
    transactions_df = dh.get_data()
    assert (transactions_df.shape[0] > 0)
    assert all(i in transactions_df.columns for i in TRANSACTIONS_REQUIRED_FIELDS)


if __name__ == '__main__':
    pytest.main(["-vv", __file__])
