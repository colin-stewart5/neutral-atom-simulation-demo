import qutip as qt
import numpy as np

def make_one_qubit_hamiltonian():
	"""
	Create the Hamiltonian that describes a single Rydberg atom. Output is a vector of each term within the Hamiltonian.
	"""
	H_01 =  0.5 * (qt.basis(3,0)*qt.basis(3,1).dag() + qt.basis(3,1)*qt.basis(3,0).dag())
	H_11 = qt.basis(3,1)*qt.basis(3,1).dag()
	H_1r = 0.5 * (qt.basis(3,1)*qt.basis(3,2).dag() + qt.basis(3,2)*qt.basis(3,1).dag())
	H_rr = qt.basis(3,2)*qt.basis(3,2).dag()
	return [H_01, H_11, H_1r, H_rr]

def rabi_drive(cfg):
	"""
	Defines the pulse applied to a qubit to induce Rabi oscillations.
	"""
	omega_01 = cfg.omega_01
	def omega(t, args=None):
		return omega_01*np.sin(2*np.pi*t/cfg.t_gate)
	return omega

def detune_drive(cfg):
	"""
	Defines the detuning applied to a qubit from the Rabi laser phase.
	"""
	delta_11 = cfg.delta_1
	def delta(t, args=None):
		return delta_11*np.cos(2*t/cfg.t_gate)
	return delta

def make_blockade(cfg):
	"""
	Creates the Rydberg blockade term for a 2 qubit neutral atom system.
	"""
	return cfg.B * qt.tensor(qt.basis(3,2)*qt.basis(3,2).dag(), qt.basis(3,2)*qt.basis(3,2).dag())
