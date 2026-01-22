import qutip as qt
import numpy as np

def make_collapse(cfg):
	"""
	Create collapse operators describring the branching between the (0,1) and r states.
	"""
	L_0r = np.sqrt(cfg.b_0r * cfg.gamma) * qt.basis(3,0)*qt.basis(3,2).dag()
	L_1r = np.sqrt(cfg.b_1r * cfg.gamma) * qt.basis(3,1)*qt.basis(3,2).dag()
	return [L_0r, L_1r]	
