### PART A_a / A_b


import numpy as np
import gillespy2
from gillespy2 import Model, Species, Reaction, Parameter, RateRule, AssignmentRule, FunctionDefinition
from gillespy2 import EventAssignment, EventTrigger, Event
from matplotlib import pyplot as plt

class Lotkavolterra_Oscillator(Model):
    def __init__(self, parameter_values=None):
        Model.__init__(self, name="Lotkavolterra_Oscillator")
        self.volume = 1

        # Define the parameters of the system
        self.add_parameter(Parameter(name="gamma_a", expression=1))     
        self.add_parameter(Parameter(name="gamma_c", expression=2))  
        self.add_parameter(Parameter(name="gamma_r", expression=1))   
        self.add_parameter(Parameter(name="delta_a", expression=1))
        self.add_parameter(Parameter(name="delta_r", expression=0.2))
        self.add_parameter(Parameter(name="delta_ma", expression=10))
        self.add_parameter(Parameter(name="delta_mr", expression=0.5))
        self.add_parameter(Parameter(name="beta_a", expression=50))
        self.add_parameter(Parameter(name="beta_r", expression=5))
        self.add_parameter(Parameter(name="theta_a", expression=50))
        self.add_parameter(Parameter(name="theta_r", expression=100))
        self.add_parameter(Parameter(name="alfa_a", expression=50))
        self.add_parameter(Parameter(name="alfa_prim_a", expression=500))
        self.add_parameter(Parameter(name="alfa_r", expression=0.01))
        self.add_parameter(Parameter(name="alfa_prim_r", expression=50))   
        

        # Add species and define the initial condition (count or concentration) of each species
        self.add_species(Species(name="A", initial_value=0, mode="2"))    
        self.add_species(Species(name="R", initial_value=0, mode="discrete"))     
        self.add_species(Species(name="C", initial_value=0, mode="discrete"))
        self.add_species(Species(name="D_a", initial_value=1, mode="discrete"))
        self.add_species(Species(name="D_r", initial_value=1, mode="discrete"))
        self.add_species(Species(name="D_prim_a", initial_value=0, mode="discrete"))
        self.add_species(Species(name="D_prim_r", initial_value=0, mode="discrete"))
        self.add_species(Species(name="M_a", initial_value=0, mode="discrete"))
        self.add_species(Species(name="M_r", initial_value=0, mode="discrete"))
        
        
        # Reactions
        self.add_reaction(Reaction(name="r1", reactants={'A': 1, 'R' : 1}, products={'C': 1}, rate=self.listOfParameters['gamma_c']))
        self.add_reaction(Reaction(name="r2", reactants={'A': 1}, products={}, rate=self.listOfParameters['delta_a']))
        self.add_reaction(Reaction(name="r3", reactants={'C': 1}, products={'R' : 1}, rate=self.listOfParameters['delta_a']))
        self.add_reaction(Reaction(name="r4", reactants={'R': 1}, products={}, rate=self.listOfParameters['delta_r']))
        self.add_reaction(Reaction(name="r5", reactants={'D_a': 1, 'A' : 1}, products={'D_prim_a' : 1}, rate=self.listOfParameters['gamma_a']))
        self.add_reaction(Reaction(name="r6", reactants={'D_r': 1, 'A' : 1}, products={'D_prim_r': 1}, rate=self.listOfParameters['gamma_r']))
        self.add_reaction(Reaction(name="r7", reactants={'D_prim_a': 1}, products={'A' : 1, 'D_a' : 1}, rate=self.listOfParameters['theta_a']))
        self.add_reaction(Reaction(name="r8", reactants={'D_a' : 1}, products={'D_a': 1,'M_a': 1}, rate=self.listOfParameters['alfa_a']))
        self.add_reaction(Reaction(name="r9", reactants={'D_prim_a' : 1}, products={'D_prim_a':1, 'M_a' : 1}, rate=self.listOfParameters['alfa_prim_a']))
        self.add_reaction(Reaction(name="r10", reactants={'M_a' : 1}, products={}, rate=self.listOfParameters['delta_ma']))
        self.add_reaction(Reaction(name="r11", reactants={'M_a' : 1}, products={'A': 1, "M_a" : 1}, rate=self.listOfParameters['beta_a']))
        self.add_reaction(Reaction(name="r12", reactants={'D_prim_r' : 1}, products={'A': 1, "D_r" : 1}, rate=self.listOfParameters['theta_r']))
        self.add_reaction(Reaction(name="r13", reactants={'D_r': 1}, products={'D_r': 1, "M_r" : 1}, rate=self.listOfParameters['alfa_r']))
        self.add_reaction(Reaction(name="r14", reactants={'D_prim_r': 1}, products={'D_prim_r': 1, "M_r" : 1}, rate=self.listOfParameters['alfa_prim_r']))
        self.add_reaction(Reaction(name="r15", reactants={'M_r': 1}, products={}, rate=self.listOfParameters['delta_mr']))
        self.add_reaction(Reaction(name="r16", reactants={'M_r': 1}, products={'M_r': 1, "R" : 1}, rate=self.listOfParameters['beta_r']))
        # Timespan
        self.timespan(np.linspace(0, 400, 401 ))
        
model = Lotkavolterra_Oscillator()        
        

results = model.run(algorithm = "SSA", number_of_trajectories=1) #change to “ODE” for part a

A = results['A']
R = results['R']
time = results['time']

#plot A time evolution
plt.title('A time evolution SSA')
plt.xlabel('Time')
plt.ylabel('Population')

plt.plot(time, A) 
plt.show()

#plot R time evolution
plt.title('R time evolution SSA')
plt.xlabel('Time(h)')
plt.ylabel('Population')

plt.plot(time, R) 
plt.show()

results.plot(yaxis_label='Population', title='Lotka-Volterra Model: SSA')
