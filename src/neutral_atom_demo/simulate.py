import qutip as qt
import numpy as np

import neutral_atom_demo.hamiltonians as ham
import neutral_atom_demo.collapse as col
import neutral_atom_demo.metrics as met

def make_init():
	"""
	Creates the initial state to be time evolved in drive_two_qubit_hamiltonian.
	"""
	zero_state = qt.basis(3,0)*qt.basis(3,0).dag()
	return qt.tensor(zero_state, zero_state)


def drive_two_qubit_hamiltonian(cfg):
	"""
	Generate a 2 qubit system with a Rabi laser driving both qubits. 
	"""
	H_1q = ham.make_one_qubit_hamiltonian()
	c_ops_1q = col.make_collapse(cfg)
	c_ops = qt.tensor(c_ops_1q[0], c_ops_1q[0])
	c_ops += qt.tensor(c_ops_1q[1], c_ops_1q[1])	

	e_ops = met.track_pops()
	
	H_rabi_drive = qt.tensor(H_1q[0], H_1q[0])
	H_detune_drive = qt.tensor(H_1q[1] , H_1q[1])
	H_static = cfg.omega_r * qt.tensor(H_1q[2], H_1q[2])
	H_static += cfg.delta_r *  qt.tensor(H_1q[3], H_1q[3])
	H_static += ham.make_blockade(cfg)

	init_state = make_init()
	t_list = np.linspace(0, cfg.t_gate, cfg.n_steps)
	
	omega = ham.rabi_drive(cfg)
	delta = ham.detune_drive(cfg)

	sol = qt.mesolve([H_static, [H_rabi_drive, omega], [H_detune_drive, delta]], init_state, t_list, c_ops, e_ops)

	return sol
	
