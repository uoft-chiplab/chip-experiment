## Context
An atom that absorbs a photon feels a momentum kick $\hbar k$ along the beam propagation direction. Subsequent spontaneous emission is isotropic, so the net force is along the beam. The net steady state force is

$$F = \hbar k R_{sc}$$

where $R_{sc} = \Gamma \rho_{ee}$ is the steady-state scattering rate given by 

$$R_{sc} = \frac{\Gamma}{2} \frac{s}{1+s+4\delta^2/\Gamma^2}$$

which derives from the optical Bloch equations on a two-level system, $s=I/I_\mathrm{sat}$, $\Gamma/2\pi \approx 6$ MHz is the linewidth of the transition, and $\delta$ is the detuning of the beam.

## Cooling to the Doppler limit

Atoms can gain or lose energy from light interaction; we seek to balance the two processes and minimize the achievable temperature.

By red-detuning the laser from resonance and adding beams along all directions, the atom-laser interaction becomes velocity selective because the atom preferentially absorbs photons when moving against a beam and seeing a Doppler-shifted frequency. The velocity-dependent damping force for 1D is 
$$F \approx \alpha v\,.$$

The rate of work for damping (cooling) the atom is then 

$$\langle dE_\mathrm{cool}/dt \rangle = \langle F \cdot v \rangle \approx \alpha \langle v^2 \rangle$$

 where the ensemble average has been taken and $\alpha$ can be shown to be $-8 \hbar k^2 \frac{\delta}{\Gamma} \frac{s}{(1 + s + 4\delta^2/\Gamma^2)^2}$. Successive absorbtion and spontaneous emission events, each giving momentum kick $\hbar k$, causes an increase in the average kinetic energy (heating). If the beams are balanced in power, both processes produce zero mean momentum, but non-zero variance (of $\langle p^2 \rangle = (\hbar k)^2$). Let us consider the variance along one axis for each process:

 * Emission: $\langle cos^2 (\theta) = 1/3 \rangle$ assuming isotropicity
 * Absorption: Only the on-axis beams contribute.

 Multiplying by the scattering rate $R_{sc}$, we then have

$$\langle dE_\mathrm{heat}/dt \rangle  = \frac{d}{dt} \frac{\langle p_z^2 \rangle}{2m} = \frac{d}{dt} \frac{\langle p_{abs}^2 \rangle + \langle p_{sp}^2\rangle}{2m} = \frac{R_{sc} (\hbar k)^2 (1+d/3)}{2m}$$

where $d$ is the number of dimensions considered. For $d=3$, we have $R_{sc} (\hbar k)^2/m$. We look to balance the heating and cooling rates; if we multiply the equations first by $m/2$, we see that the cooling rate is actually the mean kinetic energy per DOF scaled by $\alpha$ which by equipartition is $k_BT/2$. Rearranging the equation to isolate for $k_BT/2$, we have

$$\frac{m \langle v^2 \rangle}{2} = \frac{k_B T}{2} = \frac{R_{sc} \hbar^2 k^2}{2 \alpha}$$

The RHS can be simplified by taking the low-intensity limit $s \ll 1$ and using $\delta = \Gamma /2$ to achieve the max scattering rate. This minimizes the temperature; the so-called Doppler limit is

$$k_B T_D = \frac{\hbar \Gamma}{2}$$

which is $\sim 145$ uK for both Rb and K.

Consider all the assumptions that go into this Doppler limit -- balanced beams, low intensity, ideal geometry, max scattering -- and it becomes easy to see why our MOTs are usually somewhat hotter than this.
