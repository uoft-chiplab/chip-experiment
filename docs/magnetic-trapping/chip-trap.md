# Quick overview

Here I will compare the chip trap to the more commonly used Ioffe-Pritchard trap.
- Chip wires + Zbias + Xbias =  Ioffe-Pritchard

## The magnetic fields

Recall that from Biot-Savart law the magnetic field at a point perpendicular to an infinite wire is given by

$$B(r) = |\bm{B}| = \frac{\mu_0}{4\pi} I_y \int^\infty_{-\infty} dl \frac{r}{(r^2 + l^2)^{3/2}} = \frac{\mu_0}{2\pi r} I_y$$

Let us use the lab frame's usual Cartesian coordinates. Adding a bias field $\bm B_\mathrm{bias} = -B_\mathrm{bias} \bm{z}$ the total B-field is then a quadrupole field:

$$B_\mathrm{quad}(x,y,z) = \bm{B}_\mathrm{wire} + \bm{B}_\mathrm{bias} = (\frac{\mu_0 I_y}{2\pi} \frac{y}{z^2 + y^2} - B_\mathrm{bias} ) \bm{z} - (\frac{\mu_0 I_y}{2\pi}\frac{z}{z^2+y^2}) \bm{y}$$

The magnetic field vanishes along the line $(x, y=y_0, z=0$). The location of $y_0$ can be determined by setting $z=0$ and asking where the field zero is, which ends up being simply $y_0 = \mu_0 I_z / 2\pi B_\mathrm{bias}$.

Field must be added at the ends of the trap along $x$ in order to make a field minimum. This is achieved by the two end-cap pieces of the Z-wire. These expressions involve more Biot-Savart law applications. Lastly, we apply another bias field along $\bm x$ to produce an extra "Ioffe field" that tunes the magnitude of the trap bottom with affecting the trap minimum location. In sum, the total field is

$$B_\mathrm{Z}(x,y,z) = \bm{B}_\mathrm{wire} + \bm{B}_\mathrm{bias} + \bm{B}_\mathrm{endcap} + \bm{B}_\mathrm{Ioffe}= (\frac{\mu_0 I_y}{2\pi} \frac{y}{z^2 + y^2} - B_\mathrm{bias} ) \bm{z} + (B^y_\mathrm{endcap}(x,y)-\frac{\mu_0 I_y}{2\pi}\frac{z}{z^2+y^2}) \bm{y} + (B^x_\mathrm{endcap}(x,y) + B_\mathrm{Ioffe})\bm{x}$$

The primary reason one wants a non-zero trap bottom is because Majorana loss can occur at real field zeros.

## How to calibrate these values

KX has never actually calibrated these experimentally. But if we ever wanted to, see section 3.3.5 in the Extavour thesis.

Looking at those plots carefully, he is honestly surprised that the aspect ratio is so high (about 100). If we had time, would like to do these calibrations.

## Trap depth and shape

If one plots the field potential in units of temperature using $\mu_B B / k_B$ one will find that the trap is actually slightly harmonic near its minima and linear outside of it. When we initially load the chip trap we do so with $B_\mathrm{bias} \approx 20\,G$ (9 to 10 A) and $B_\mathrm{Ioffe} \approx 2\,G$ (about 2 A). This is quite similar to the conditions in Fig. 3.4; taking a simpler estimate of the potential as $\mu_B B_\mathrm{bias} / k_B$, the initial trap depth is about $1.3$ mK.

As RF evaporation proceeds, the we decompress the trap to reduce the density. We do this by halving the current in the Z-wire and the bias field. The trap depth becomes $...$.

## Loading

Atoms are trapped if its energy is less than the trap depth $U$. After trapping, we have a trap-depth-limited trap with a truncated thermal distribution, with a truncation occuring at 

$$U = \eta k_B T$$

This $\eta$ term is a useful metric for evaporation. Note that atoms immediately start evaporating out of the trap due to collisional processes. When $\eta \lesssim 3$, free evaporation occurs. Efficient evaporation occurs for $\eta \gtrsim 5$. Earlier it was mentioned that $U\approx 1.3$ mK. We have measured our QMT-loaded temperature to be about $T \approx 300 \mu K$, so we reach $\eta \approx 4$ upon loading.

The total number of atoms that can be loaded is fundamentally limited by the effective trap volume, which is a function of temperature, density, trap depth, and $\eta$ (so trap depth compared to temperature). The maximum number of atoms can be found to be

$$N_\mathrm{max} = \rho_0 (\frac{M}{2\pi\hbar^2})^{3/2} C_\delta (U/\eta)^{\delta + 3/2}$$

where $\rho_0$ is the phase-space density and $\delta$ is the temperature-dependence of the effective volume, and noting that $U/\eta \implies T$. The value of $\delta$ is not trivial and depends on the trap model. The following table summarizes the result found in section 5.2.1:

| Model | Effective volume | $\delta$ 
| :--- | :--- | :---  
|3D SHO | $(\frac{2\pi}{M \bar{\omega}^2})^{3/2} (k_BT)^{3/2} $| 3/2
|3D quadrupole| $8\pi \bar{F}^{-3} (k_BT)^3$| 3
|2D quadrupole + 1D box| $2\pi L \bar{F}^{-2} (k_BT)^2$| 2

Here $\bar{F}$ is the geometric mean gradient.

A surprising facet of all this is that the max trapped atom number from the chip lab's creation until now is not so different, even with all the changes to the MOT and gray molasses. What these features really likely did is reduce T and increase the phase-space density by a few factors at most.

## Forced rf evaporation

We can cool atoms by forcibly spin-flipping the hotter atoms out of the trap and allowing the rest to collisionally thermalize. Hotter atoms sample regions further out in space. The evaporation should begin at a shell of some $B(r)$ and ramp its way down towards the center of the trap.

### Essential picture

Let us drive RF at some $\nu_\mathrm{rf}$ that is resonant with Zeeman splitting (and perhaps with some thermal energy compensation ignored here): $h\nu_\mathrm{rf} = g_F \mu_B |B(r)|$. The RF will hit atoms that are on a shell of energy, flip them to untrappable states, and leave. We ramp this rf knife at a rate tuned to make evaporation efficient depending on the collision rate, $T$, $\eta$, etc. The trap depth at the end of evaporation is

$$U \propto \mu (B_\mathrm{rf} - B_0)$$

We have not calibrated $B_0$ in a very long time, but we do regularly observe that Rb-87 atoms completely disappear around $\nu_\mathrm{rf} \approx 2.1 $ MHz. We usually stop our rf evaporation around $\nu_\mathrm{rf} \approx 2.28 $ MHz. The trap depth is naively estimated to be on the order of $U \approx 10 \mu K$. This estimate seems small by a few factors, as the optical dipole trap depth is close to this as well.

### RF-dressed picture

This is a lot harder to describe

## Extra notes

- trap is twisted
- corrections due to finite length and width of wires

## Experiment

Table of experiment phases and typically applied values in sequencer with interpreted A or G