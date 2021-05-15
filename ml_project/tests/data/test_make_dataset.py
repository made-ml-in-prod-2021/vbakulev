from src.data.make_dataset import read_data, split_train_val_data
from src.entities.split_params import SplittingParams


RANDOM_STATE = 13
VAL_SIZE = 0.2


def test_load_dataset(dataset_path, target_col: str):
    data = read_data(dataset_path)
    assert len(data) > 10
    assert target_col in data.keys()


def test_split_dataset(tmpdir, dataset_path):
    splitting_params = SplittingParams(random_state=RANDOM_STATE, val_size=VAL_SIZE,)
    data = read_data(dataset_path)
    train, val = split_train_val_data(data, splitting_params)
    assert train.shape[0] > 60
    assert val.shape[0] > 10
