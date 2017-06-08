'''

    Parameters C1:
        Cells:           Single compartment, conductance based cell models with HH like ion channels
        Chem Synapses:   Analogue/graded synapses; continuous transmission (voltage dependent)
        Gap junctions:   Electrical connection; current linerly depends on difference in voltages 
        
    ASSESSMENT:
        A good prospect, but cell model could be simpler. See C0

'''

from neuroml import GradedSynapse
from neuroml import GapJunction

from parameters_C import ParameterisedModel as ParameterisedModel_C


class ParameterisedModel(ParameterisedModel_C):

    def __init__(self):
        super(ParameterisedModel, self).__init__()
        self.level = "C1"
        self.custom_component_types_definitions = 'cell_C.xml'
        
        self.set_default_bioparameters()
        print("Set default parameters for %s"%self.level)
        

    def set_default_bioparameters(self):

        self.add_bioparameter("cell_diameter", "5", "BlindGuess", "0.1")
        self.add_bioparameter("muscle_length", "20", "BlindGuess", "0.1")

        self.add_bioparameter("initial_memb_pot", "-45 mV", "BlindGuess", "0.1")

        self.add_bioparameter("specific_capacitance", "1 uF_per_cm2", "BlindGuess", "0.1")

        self.add_bioparameter("muscle_spike_thresh", "-20 mV", "BlindGuess", "0.1")
        self.add_bioparameter("neuron_spike_thresh", "-20 mV", "BlindGuess", "0.1")

        self.add_bioparameter("muscle_leak_cond_density", "0.005 mS_per_cm2", "BlindGuess", "0.1")
        self.add_bioparameter("neuron_leak_cond_density", "0.005 mS_per_cm2", "BlindGuess", "0.1")

        self.add_bioparameter("leak_erev", "-50 mV", "BlindGuess", "0.1")

        self.add_bioparameter("muscle_k_slow_cond_density", "0.1408257307011203 mS_per_cm2", "BlindGuess", "0.1")
        self.add_bioparameter("neuron_k_slow_cond_density", "1.8333751019872582 mS_per_cm2", "BlindGuess", "0.1")
        self.add_bioparameter("k_slow_erev", "-60 mV", "BlindGuess", "0.1")

        self.add_bioparameter("muscle_k_fast_cond_density", "0.005 mS_per_cm2", "BlindGuess", "0.1")
        self.add_bioparameter("neuron_k_fast_cond_density", "0.0711643917483308 mS_per_cm2", "BlindGuess", "0.1")
        self.add_bioparameter("k_fast_erev", "-60 mV", "BlindGuess", "0.1")

        self.add_bioparameter("muscle_ca_boyle_cond_density", "1.7139140434941569 mS_per_cm2", "BlindGuess", "0.1")
        self.add_bioparameter("neuron_ca_boyle_cond_density", "1.6862775772264702 mS_per_cm2", "BlindGuess", "0.1")
        
        self.add_bioparameter("ca_boyle_erev", "40 mV", "BlindGuess", "0.1")
        
        self.add_bioparameter("ca_conc_decay_time", "13.811870945509265 ms", "BlindGuess", "0.1")
        self.add_bioparameter("ca_conc_rho", "0.000238919 mol_per_m_per_A_per_s", "BlindGuess", "0.1")


        self.add_bioparameter("neuron_to_neuron_exc_syn_conductance", "0.09 nS", "BlindGuess", "0.1")
        self.add_bioparameter("neuron_to_muscle_exc_syn_conductance", "0.09 nS", "BlindGuess", "0.1")
        
        self.add_bioparameter("exc_syn_delta", "5 mV", "BlindGuess", "0.1")
        self.add_bioparameter("exc_syn_vth", "0 mV", "BlindGuess", "0.1")
        self.add_bioparameter("exc_syn_erev", "0 mV", "BlindGuess", "0.1")
        self.add_bioparameter("exc_syn_k", "0.025per_ms", "BlindGuess", "0.1")

        self.add_bioparameter("neuron_to_neuron_inh_syn_conductance", "0.09 nS", "BlindGuess", "0.1")
        self.add_bioparameter("neuron_to_muscle_inh_syn_conductance", "0.09 nS", "BlindGuess", "0.1")
        
        self.add_bioparameter("inh_syn_delta", "5 mV", "BlindGuess", "0.1")
        self.add_bioparameter("inh_syn_vth", "0 mV", "BlindGuess", "0.1")
        self.add_bioparameter("inh_syn_erev", "-70 mV", "BlindGuess", "0.1")
        self.add_bioparameter("inh_syn_k", "0.025per_ms", "BlindGuess", "0.1")
        

        self.add_bioparameter("neuron_to_neuron_elec_syn_gbase", "0.00052 nS", "BlindGuess", "0.1")
        self.add_bioparameter("neuron_to_muscle_elec_syn_gbase", "0.00052 nS", "BlindGuess", "0.1")

        self.add_bioparameter("unphysiological_offset_current", "5.135697186048022 pA", "KnownError", "0")
        self.add_bioparameter("unphysiological_offset_current_del", "0 ms", "KnownError", "0")
        self.add_bioparameter("unphysiological_offset_current_dur", "2000 ms", "KnownError", "0")



    def create_models(self):
        self.create_generic_muscle_cell()
        self.create_generic_neuron_cell()
        self.create_offsetcurrent_concentrationmodel()
        self.create_neuron_to_neuron_syn()
        self.create_neuron_to_muscle_syn()



    def create_neuron_to_neuron_syn(self):
        self.neuron_to_neuron_exc_syn = GradedSynapse(id="neuron_to_neuron_exc_syn",
                                conductance =        self.get_bioparameter("neuron_to_neuron_exc_syn_conductance").value,
                                delta =              self.get_bioparameter("exc_syn_delta").value,
                                Vth =                self.get_bioparameter("exc_syn_vth").value,
                                erev =               self.get_bioparameter("exc_syn_erev").value,
                                k =                  self.get_bioparameter("exc_syn_k").value)


        self.neuron_to_neuron_inh_syn = GradedSynapse(id="neuron_to_neuron_inh_syn",
                                conductance =        self.get_bioparameter("neuron_to_neuron_inh_syn_conductance").value,
                                delta =              self.get_bioparameter("inh_syn_delta").value,
                                Vth =                self.get_bioparameter("inh_syn_vth").value,
                                erev =               self.get_bioparameter("inh_syn_erev").value,
                                k =                  self.get_bioparameter("inh_syn_k").value)

        self.neuron_to_neuron_elec_syn = GapJunction(id="neuron_to_neuron_elec_syn",
                               conductance =    self.get_bioparameter("neuron_to_neuron_elec_syn_gbase").value)



    def create_neuron_to_muscle_syn(self):
        self.neuron_to_muscle_exc_syn = GradedSynapse(id="neuron_to_muscle_exc_syn",
                                conductance =        self.get_bioparameter("neuron_to_muscle_exc_syn_conductance").value,
                                delta =              self.get_bioparameter("exc_syn_delta").value,
                                Vth =                self.get_bioparameter("exc_syn_vth").value,
                                erev =               self.get_bioparameter("exc_syn_erev").value,
                                k =                  self.get_bioparameter("exc_syn_k").value)


        self.neuron_to_muscle_inh_syn = GradedSynapse(id="neuron_to_muscle_inh_syn",
                                conductance =        self.get_bioparameter("neuron_to_muscle_inh_syn_conductance").value,
                                delta =              self.get_bioparameter("inh_syn_delta").value,
                                Vth =                self.get_bioparameter("inh_syn_vth").value,
                                erev =               self.get_bioparameter("inh_syn_erev").value,
                                k =                  self.get_bioparameter("inh_syn_k").value)

        self.neuron_to_muscle_elec_syn = GapJunction(id="neuron_to_muscle_elec_syn",
                               conductance =    self.get_bioparameter("neuron_to_muscle_elec_syn_gbase").value)


