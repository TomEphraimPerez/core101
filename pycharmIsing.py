
# ISING eg day-1
# https://support.dwavesys.com/hc/en-us/articles/360003718693-Define-a-Simple-Problem-and-Submit-It-to-a-QPU-Ising-Example-
# $ pip install dimod                           # !
# $ pip install dwave-system                    # !
# /Users/thomasperez/pycharmcore101/core101/pycharmIsing.py
# Ask tutor re no qubits

from dwave.system import DWaveSampler           # ! >>>
from dwave.system import EmbeddingComposite

print('\nHello Ising Example')
solver = DWaveSampler()

sampler = EmbeddingComposite(solver)
print('\n', solver.properties.keys())          # was 'solver'


qubits = solver.properties['qubits']
couplers = solver.properties['couplers']        # was 'solver'

qubit_1 = 0
qubit_2 = 4
coupler = [qubit_1, qubit_2]

if (qubit_1 in qubits) and \
   (qubit_2 in qubits) and \
   (coupler in couplers):
    print('\nQubits {} and {} and their coupler {} are available'.format(qubit_1, qubit_2, coupler))

else:
   print('\nNo qubit_1, qubit_2, and coupler\n')

h = {qubit_1:-1,qubit_2:-1}
J = {tuple(coupler): -1}

solution = sampler.sample_ising(h, J, num_reads=10)    # was 'solver'