## Magneto-Optical Trap (MOT)

Atoms can be trapped by lasers with the correct polarization and a magnetic field gradient. The gradient does not trap by itself; it causes an imbalance in [[scattering force]] such that the [[radiation force]] nudges moving atoms towards the center of the trap. The nudges are in the form of photon kicks, cooling the sample as well.

#### Example
Consider a quadrupole magnetic field produced by Helmholtz coils that has zero magnetic field at its center and we assume that there is a uniform field gradient close to the center. 

Consider an atom on which we address a $J=0 \to J'=1$ transition. The J'=1 level has 3 sublevels $M_J=-1,0,1$. Because of the presence of the magnetic field gradient, the [[Zeeman effect]] causes the energy of the sublevels to vary linearly in space. 

((picture))

For a complete trap we require three orthogonal pairs of red-detuned $\sigma^+-\sigma^-$ beams. For simplicity consider an atom moving along the z-direction as in the picture. When it moves such that $z>0$, the Zeeman shift lowers the energy of the $M_J=-1$ state. Eventually the atom will move to a point where this energy matches the energy of the oncoming $\sigma^-$ beam. Absorption of a photon causes a kickback towards the center of the trap. The opposite situation occurs in the reverse direction.

#### Math 
The trapping force is given by the [[Optical Molasses]] force with the addition of the Zeeman effect (assumed to be linear).

$$F_{MOT} = F_{sc}^{\sigma^+}(\omega - kv - (\omega_0 + \beta z)) - F_{sc}^{\sigma^-}(\omega + kv - (\omega_0 - \beta z))$$
$$F_{MOT} \approx -2\frac{\partial F}{\partial \omega}kv + 2\frac{\partial F}{\partial \omega_0}\beta z$$
How?..... (see Foot, Eq. 9.15).
#Assumptions:
- Small Zeeman shift $\beta z \ll \Gamma$
- Small velocity approximation $kv \ll \Gamma$

The term $\omega_0 + \beta z$ is the resonant absorption frequency for the $\Delta M_J=1$ transition at position $z$ and the coefficient $\beta$ is given by
$$\beta z = \frac{g \mu_B}{\hbar}\frac{dB}{dz}z$$
In this case $g=g_J$ but more generally $g=g_{F'}M_{F'} - g_F M_F$ for a transition between hyperfine levels.

$F_{MOT}$ depends on the frequency detuning $\delta = \omega - \omega_0$. For small detuning $\omega \approx - \omega_0$ and thus
$$F_{MOT}=-2 \frac{\partial F}{\partial \omega}(kv+\beta z)$$$$F_{MOT}=-\alpha v - \frac{\alpha \beta}{k}z$$
Which we interpret as a [[restoring force]], caused by the field gradient, generating an [[overdamping]] condition with spring constant $\frac{\alpha \beta}{k}$.

#### Application
- our 40K system
- [[phase space density]]
- temperatures
- numbers

#### References
Atomic Physics, Foot.

