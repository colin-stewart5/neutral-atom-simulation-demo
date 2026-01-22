import qutip as qt

def track_pops():
	"""
	Create expectation operators on the first qubit to analyze how the populations in the 0, 1, and r states vary over time in the 2 qubit system.
	"""
	zero_pop = qt.basis(3,0)*qt.basis(3,0).dag()
	one_pop = qt.basis(3,1)*qt.basis(3,1).dag()
	r_pop = qt.basis(3,2)*qt.basis(3,2).dag()
	I = qt.qeye(3)
	return [qt.tensor(zero_pop, I), qt.tensor(one_pop, I), qt.tensor(r_pop, I)]
