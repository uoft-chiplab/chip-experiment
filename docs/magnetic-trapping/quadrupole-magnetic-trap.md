## The QMT B-field

Our quadrupole magnetic trap is simply the MOT/FB coils in anti-Helmholtz configuration. By summing the contributions from both coils (with equal current), the B-field can be shown to be

$$B(r) = B'(-x/2, -y/2, z)$$

where $B' = \frac{\partial B_z}{\partial z}|_0$. The modulus of the B-field is 

$$|B| = B' \sqrt{z^2 + \frac14(x^2 + y^2)}$$

The factors of $1/2$ in the B-field vector is enforced by the law $\nabla \cdot \bm{B} = 0$. Having chosen our primary axis to be along $\hat z$, the gradient there must be two times the gradient in each transverse direction. Physically our trap is linear (not harmonic), tighter along $z$ and looser in $x$ and $y$. 

## Adding the XFER coil

When we load from molasses to QMT, we also turn on the XFER coil simultaneously, which is oriented along $y$. In fact, when we initially load our MOT, we also have this XFER coil on -- this means the MOT is not formed at the geometric center of the MOT coils, but actually off-axis in the y by -2.5 cm. This was done because it made it easier to construct coils that would permit the needed transfer distance to the chip(?).

Conceptually, the XFER coil acts like a giant shim coil that shifts the field minimum of the QMT along the $y$ direction, assuming the atoms are oriented perfectly along its axis. The current is simply ramped slowly (and flipped midway) to adiabatically move the field minimum from the MOT location to the chip location.

A strange complication is that there is only one XFER coil. There used to be two, but the one closest to the table was magnetizing it and causing problems. Having a single coil effectively means adding second quadrupole near the atoms. The math for one coil is not really detailed in any thesis I could find. If you have time, please fill in some of these details.

## The QMT + single XFER coil field

## Transport

### Adiabaticity limits

How slow does the ramp need to be?

Probably needs something about adiabatic following like Larmor precession frequency

$$\hbar \omega_L = g_F m_F \mu_B B$$

and a precession rate like 

$$\frac{d\theta}{dt} \ll \omega_L$$

## Experiment notes

- QMT + XFER is on for the MOT and QMT loading phases before transport to chip
- QMT + XFER current during MOT effects both MOT position and gradient (MOT size) -- see Extavour Table 4.2 for old G/A and gradient calculations. Note that this table says the transfer coil produces no dB/dz but I think it should be finite but small.
- XFER transport ramp involves a relay that switches the current direction



