from dataclasses import dataclass

@dataclass
class simconfig:
	omega_01: float
	delta_1: float
	omega_r: float
	delta_r: float
	gamma: float
	b_0r: float
	b_1r: float
	B: float
	t_gate: float
	n_steps: int	
	
