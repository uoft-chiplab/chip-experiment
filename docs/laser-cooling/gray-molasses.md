## Context

<figure markdown>
  ![Overall effect](imgs/gm_fernandes_diagram.png){ width="400" }
  Atoms are in dressed into superpositions of (B)right and (D)ark states. Bright states climb potential hills before getting optically pumped into a dark state. Motional coupling brings dark states back towards bright states near potential valleys. Image taken from Fig. 4.2.1 of Diogo Rio Fernandes' PhD thesis, 2014.
</figure>

A type of sub-Doppler cooling that combines a polarization gradient cooling, a two-photon $\Lambda$ transition, and dark-state coupling. Normal PGC is not as effective for the K-40 D2 line compared to Rb-87 because the hyperfine manifold is not as well resolved. Gray molasses cooling on the D1 line is utilized instead.

<figure markdown>
  ![Level structures](imgs/gm_level_structure.png){ width="400" }
  We lock to the F=1 to F'=2 transition of K-39 on the left. On the right for K-40, we utilize F=9/2 to F'=7/2 for the "cooler" leg, and F=7/2 to F'=7/2 for the "repumper" leg.
</figure>


## Setup and Hamiltonians
A simplified diagram of the states involved in the so-called "Lambda" transition is shown below.

<figure markdown>
  ![Lambda transition](imgs/gm_lambda_diagram.png){ width="400" }
  We will refer to F=9/2 and F=7/2 as ground states one and two -- $\ket{g_1}$ and $\ket{g_2}$. The excited state is F'=7/2 or $\ket{e}$.
</figure>

Note that both arms are blue-detuned with common-mode detuning $\Delta>0$. Here the differential is $\delta = \Delta_1 - \Delta_2$ which has been suggestively set to 0. In the semi-classical picture under the RWA, the interaction Hamiltonian is 

$$H_\mathrm{int} = \frac{\hbar}{2} [\Omega_1 e^{-i\omega_1 t} \ket{e}\bra{g_1} + \Omega_2 e^{-i\omega_2 t} \ket{e}\bra{g_2}]$$

where the zero of energy has been set at $\ket{g_1}$, such that $\omega_1 \equiv \omega_{g\to e} + \Delta_1$ and $\omega_2 \equiv \omega_{g \to e} + \Delta_2 - \omega_{hf}$. Here, $\omega_{hf} = 1285.8$ MHz is fixed by our D1 level structure. Let us remove the time dependence by transforming into a rotating frame. That is, we seek to do the transformation 

$$H \to UHU^\dag + i\hbar \dot{U} U^\dag$$

where $U(t)= e^{i\sum_n \theta_n\ket{n}\bra{n}}$ is some unitary operator, that when acting on a state $\ket{\psi} = \sum_n c_n \ket{n}$, transforms $\tilde{c}_n = e^{i\theta_n(t)} c_n$. Since $U$ is diagonal, 

$$U \ket{m} \bra{n} U^\dag = e^{i\theta_m} \ket{m} \bra{n} e^{-i\theta_n} = e^{i(\theta_m - \theta_n)} \ket{m}\bra{n}$$

and therefore we expect to see:

- diagonal terms ($m=n$) will be unchanged
- off-diagonal terms get difference-phase prefactors

Explicitly, the transformation creates

$$
\Omega_1 e^{-i\omega_{L1}t}|e\rangle\langle g_1| \;\longrightarrow\; \Omega_1\,e^{i(\theta_e-\theta_{g_1}-\omega_{L1}t)}|e\rangle\langle g_1|
$$

$$
\Omega_2 e^{-i\omega_{L2}t}|e\rangle\langle g_2| \;\longrightarrow\; \Omega_2\,e^{i(\theta_e-\theta_{g_2}-\omega_{L2}t)}|e\rangle\langle g_2|
$$

Demanding that both exponents vanish (i.e: imposing stacisity) gives

$$
\boxed{\ \theta_e - \theta_{g_1} = \omega_{L1}t, \qquad \theta_e - \theta_{g_2} = \omega_{L2}t\ }
$$

Lastly, we stay consistent with fixing the energy of $\ket{g_1}$ to be zero and do some gauge-fixing by setting $\theta_{g_1} \to 0$ as well. This causes $\theta_e = \omega_1 t$ and $\theta_{g_2} = \omega_1 t - \omega_2 t$. The final unitary is

$$
U(t) = \exp\Big(i\big[\omega_{1}|e\rangle\langle e| + (\omega_{1}-\omega_{2})|g_2\rangle\langle g_2|\big]t\Big) \equiv e^{iRt}
$$

Now we perform the transformation. Intuitively, the non-diagonal terms will become stationary. But because $U$ was diagonal and commutes with the bare $H_\mathrm{atom}$, its effect will be to shift the bare atom energies. That is, 

$$
|e\rangle:\quad \hbar\omega_e - \hbar\omega_{1} = -\hbar\Delta_1
$$

$$
|g_2\rangle:\quad \hbar\omega_{\rm hf} - \hbar(\omega_{1}-\omega_{2}) = -\hbar\big[(\omega_{1}-\omega_{2}) - \omega_{\rm hf}\big] = -\hbar\delta
$$

And our final Hamiltonian is

$$
\boxed{\ H = -\hbar\Delta_1|e\rangle\langle e| \;-\; \hbar\delta\,|g_2\rangle\langle g_2|
\;+\; \frac{\hbar}{2}\Big(\Omega_1|e\rangle\langle g_1| + \Omega_2|e\rangle\langle g_2| + \mathrm{h.c.}\Big)\ }
$$

### Interpretation

- The excited-state energy in this rotating frame is just the one-photon detuning.
- The hyperfine splitting has been absorbed; the ground-state spitting depends on the two-photon differential detuning.
- Off-diagonal terms are now stationary states.
- The signs of the energy shifts depend on the definition of $\delta = \Delta_1 - \Delta_2$ in this case.
- When $\delta = 0$, the ground-state splitting disappears; the two ground states become degenerate. This will be shown to be necessary for forming coherent superpositions of bright and dark states.

## Bright and dark states








## Experiment

- capture velocity is low 
- circ to circ polarization is weird
- optical setup, diagram
- repumper EOM
- blue detuning