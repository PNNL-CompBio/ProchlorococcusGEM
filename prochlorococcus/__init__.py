import cobra
import pathlib

path = pathlib.Path(__file__).parent

model = cobra.io.read_sbml_model(
    path.joinpath('prochlorococcus.xml').__str__()
)

exp_file_path = path.joinpath('data', 'experiments.yml').__str__()