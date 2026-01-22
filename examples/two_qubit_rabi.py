import neutral_atom_demo as demo
import numpy as np
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore", category=FutureWarning)


cfg = demo.simconfig(omega_01 = 1.0,
			delta_1 = 1.0,
			omega_r = 0.0,
			delta_r = 0.0,
			gamma = 1/5,
			b_0r = 1/16,
			b_1r = 1/16,
			B = 100.0,
			t_gate = 100.0,
			n_steps = 100
)

sol = demo.drive_two_qubit_hamiltonian(cfg)

pops = np.real(sol.expect)
t = sol.times

plt.figure(figsize=(7,4))
plt.plot(t, pops[0], label=r"$P|0\rangle)$", linewidth=2)
plt.plot(t, pops[1], label=r"$P|1\rangle)$", linewidth=2)
plt.plot(t, pops[2], label=r"$P|r\rangle)$", linewidth=2)

plt.xlabel("Time (ms)")
plt.ylabel("Population")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
plt.savefig("figures/rabi_population.png", dpi=200)
