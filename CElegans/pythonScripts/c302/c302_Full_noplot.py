import c302
import sys

def setup(parameter_set,
          generate=False,
          duration=6000,
          dt=0.05,
          target_directory='noplot/1110',
          include_muscles = True):

    exec('from parameters_%s import ParameterisedModel'%parameter_set)
    params = ParameterisedModel()

    # Some random set of neurons
    # cells_to_stimulate = ["ADAL", "ADAR", "M1","M2L","M3L","M3R","M4","I1R","I2L","I5","I6","MI","NSMR","MCL","ASEL", "AVEL", "AWAR", "DB1", "DVC", "RIAR", "RMDDL"]
    cells_to_stimulate = ['ASEL', 'ASER']

    # Plot some directly stimulated & some not stimulated
    # cells_to_plot      = ["ADAL", "ADAR", "PVDR", "BDUR","I1R","I2L"]
    # cells_to_plot      = ['AVBL','AVBR','PVCL', 'PVCR', 'DB1','DB2','VB1','VB2','DD1','DD2','VD1','VD2']
    cells_to_plot = ['AVAL', 'RIM', 'ASEL', 'ASER', 'PVCL', 'AVEL']

    reference = "c302_%s_Full_noplot"%parameter_set

    cell_names, conns = c302.get_cell_names_and_connection()

    if generate:
        c302.generate(reference,
             params,
             cells_to_plot=cells_to_plot,
             cells_to_stimulate=cells_to_stimulate,
             include_muscles = include_muscles,
             duration=duration,
             dt=dt,
             vmin=-72 if parameter_set=='A' else -52,
             vmax=-48 if parameter_set=='A' else -28,
             validate=(parameter_set!='B'),
             target_directory=target_directory)

    return cell_names, cells_to_stimulate, params, include_muscles


if __name__ == '__main__':

    parameter_set = sys.argv[1] if len(sys.argv)==2 else 'A'

    setup(parameter_set, generate=True)
