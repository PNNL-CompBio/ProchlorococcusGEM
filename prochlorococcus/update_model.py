from memote.suite.cli.reports import diff
import cobra
import os
import logging
from concerto.utils.biolog_help import add_biolog_exchanges
from prochlorococcus.media import m9_media

log = logging.getLogger()
log.setLevel(4)

_file_path = os.path.dirname(__file__)
starting_model_f_name = 'iSO595v7.xml'
s_model_path = os.path.join(_file_path, starting_model_f_name)

starting_model = cobra.io.read_sbml_model(s_model_path)
starting_model.id = "ps"

output_model_name = 'prochlorococcus.xml'
output_model_path = os.path.join(_file_path, output_model_name)


def write_model(model):
    cobra.io.write_sbml_model(model, output_model_path)


def update_1(model):
    # add missing biolog reactions to model
    log.info("Adding biolog reactions to model")
    model = add_biolog_exchanges(model)
    return model


def update_model():
    rxns = {i.id for i in starting_model.reactions}
    print(rxns)
    for i in m9_media:
        if i not in rxns:
            print(i)
    # quit()
    # Fix compartments
    # model = update_1(starting_model)

    write_model(starting_model)



if __name__ == '__main__':
    update_model()
    quit()
    model_paths = [s_model_path, output_model_path]
    diff(
        [
            *model_paths,
            '--filename', os.path.join(_file_path, 'model_differences.html'),
            '--experimental', os.path.join(_file_path, 'data', 'experiments.yml'),
            # '--custom-tests', os.path.join(_file_path, 'custom_tests'),
            '--exclusive', 'test_growth',
        ]
    )
