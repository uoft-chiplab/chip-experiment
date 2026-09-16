## Context

MW reanalyzed the unitary expansion thermometry code and found a number of issues, bugs, and concerns.

- Shear viscosity $\alpha$ was constant (from an old fit to aspect ratio I believe) but according to the paper we follow it should be trap-averaged and a function of $E/E_F$. Also needed to fix a power-law fit to ensure $\alpha>0$. Confusion: we use a high-temperature Gaussian distro $\alpha$, not sure how to estimate $E/E_F$ properly.

- ODE solver was quietly failing... oops!

- ODE equations needed a trap frequency to match papers, but now some confusion about dimensionful or dimensionless parameters.

