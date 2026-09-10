The size of a MOT cloud is usually tuned by two parameters: the field gradient, and the laser detuning. The phase-space densities of MOTs are often improved by adding a brief (i.e: hundreds of ms) compressed MOT ("CMOT") phase near the end.

In our current MOT recipe (Sep 2026), we implement CMOT only for K-40 by ramping the detuning $\delta$ of the trap laser closer to resonance, with a final endpoint that is only a fraction of $\Gamma$. We simultaneously greatly reduce the intensities of both the trap and repump lasers (roughly 70% for Trap, maybe 30% or less for RP; numbers purely from memory so take with grain of salt). The intuition is as follows:

- MOTs are built with very red-detuned lasers, so the capture region (and velocity) is quite large.
- To increase phase-space density, slowly ramp the detuning towards resonance to induce more scattering events from the outer shell towards the center.
- But high densities can be bad for MOTs because of light-assisted collisions; reduce collision rate by reducing light intensity (i.e: bare Rabi frequency).

The Saloman group also adds D1 light during CMOT (with optimized frequency and intensity); the intuition is that the D1 light shelves some atoms into dark states, allowing greater MOT density. We do not do this and could incorporate it in the future with better frequency control.