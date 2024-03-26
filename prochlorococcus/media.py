import pathlib
import pandas as pd

path = pathlib.Path(__file__).parent


m9_path = path.joinpath('data', 'media', 'm9_minimal.csv').__str__()
m9_media = pd.read_csv(m9_path)

m9_media = m9_media.set_index('exchange')['uptake'].to_dict()
