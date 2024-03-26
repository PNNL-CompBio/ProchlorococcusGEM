import cobra
import pathlib
import pandas as pd

path = pathlib.Path(__file__).parent

model = cobra.io.read_sbml_model(
    path.joinpath('Rhodo_Toru.xml').__str__()
)
mar_model = cobra.io.read_sbml_model(
    path.joinpath('Rhodo_Toru_marana.xml').__str__()
)
exp_file_path = path.joinpath('data', 'experiments.yml').__str__()
expected_metab = pd.read_csv(
    path.joinpath('data', 'excreted', 'metabolites.csv').__str__(),

).bigg_id

m9_media = {
    'EX_ca2_e': 1000,
    'EX_cl_e': 1000,
    'EX_co2_e': 1000,
    #'EX_cobalt2_e': 1000,
    'EX_cu2_e': 1000,
    'EX_fe2_e': 1000,
    'EX_fe3_e': 1000,
    'EX_h_e': 1000,
    'EX_h2o_e': 1000,
    'EX_k_e': 1000,
    'EX_mg2_e': 1000,
    'EX_mn2_e': 1000,
    #'EX_mobd_e': 1000,
    'EX_na1_e': 1000,
    #'EX_tungs_e': 1000,
    'EX_zn2_e': 1000,
    #'EX_ni2_e': 1000,
    #'EX_sel_e': 1000,
    #'EX_slnt_e': 1000,
    'EX_so4_e': 1000,
    'EX_nh4_e': 1000,
    'EX_pi_e': 1000,
    #'EX_cbl1_e': .01,
    'EX_o2_e': 20
}
