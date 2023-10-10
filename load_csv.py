import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame:
    '''
    Takes a path as argument, writes the dimensions of the data set and
    returns it
    '''
    try:
        assert type(path) is str, "Path is bad"
        pd.options.display.max_rows = 1
        pd.options.display.max_columns = 10
        pd.options.display.show_dimensions = False
        df = pd.read_csv(path)
        assert len(df) > 1 and df.shape[1] > 1, "Bad format"
    except (FileNotFoundError, PermissionError):
        print("AssertionError: Path is bad")
        return None
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return None
    except BaseException as e:
        print(f"type{e}.__name__")
        return None
    else:
        print("Loading dataset of dimensions {}".format(df.shape))
        return df
