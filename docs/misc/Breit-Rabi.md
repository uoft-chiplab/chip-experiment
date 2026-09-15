## Context

I had a brief chat with a professor who was exhibited some confusion about our hyperfine rf spin flips. He was not confused that we use states adiabatically connected to the hyperfine Zeeman states of K-40 in the F=9/2 manifold (i.e: mF = -9/2, -7/2, aand -5/2 usually). He was confused **why the energy splitting between these states was not degenerate, so that we could do rf spin flips we good resolution.** I was confused why he was confused, but realized this is actually the case in both the low- and high-field limits. We operate in the intermediate field regime, where the splitting is not degenerate. It seems rather serendipitous that this regime coincides with our Feshbach resonance region and I wonder if there is some interplay at work here. 

This note serves to explain the energies of the hyperfine-Zeeman states at intermediate field. For alkali atoms, these energies are uniquely calculable analytically through the Breit-Rabi formula, which works across all field, and whose salient features will be described.

A very formal derivation can be found here: https://coldatoms.slack.com/archives/C015SA5D2UA/p1669310583848619

## How do I know we're at intermediate field?

Potassium-40 (J=1/2, I=4) has hyperfine manifolds F=9/2 and F=7/2 with a splitting $\Delta E_{hf}/h \approx 1286$ MHz. We must compare the bare electron Zeeman energy to this splitting, which is $g_J \mu_B B /h \approx 560$ MHz for B=200 G. These are comparable, so neither the low-field (Zeeman) $\ket{F, m_F}$ nor the high-field (Paschen-Back) $\ket{m_I, m_F}$ are good bases.

## Solution
The Breit-Rabi Hamiltonian is 

$$\hat H = \hat H_{hf} + \hat H_Z = A_hf \hat I \cdot \hat J + g_J \mu_B B \hat J_Z + g_I \mu_N B \hat I_Z$$

This describes the magnetic-field coupling of an atom of J=1/2. One can solve this Hamiltonian in the high-field basis (meaning we will keep the nuclear term and use the basis $\ket{I, m_I, J, m_J}$ with the always-terrible Clebsh-Gordan decomposition method and recognizing that 

$$\hat I \cdot \hat J = \hat I_z \hat J_z + \frac12 (\hat I_+ \hat J_- + \hat I_- \hat J_+)$$

These raising and lower operators are integral to the intuitive viewpoint. They are responsible for mixing states together that keep the total $m$ constant. The nonzero matrix elements are

$$\bra{J, m_J, I, m_I} \hat I \cdot \hat J \ket{J, m_J, I, m_I} = \hbar^2 m_J m_I$$

$$\bra{J, m_J, I, m_I} \hat I \cdot \hat J \ket{J, m_J+1, I, m_I-1} = \frac{\hbar^2}{2} \sqrt{(J+m_J)(J-m_J+1)} \times \sqrt{(I-m_I)(I+m_I+1)}$$

$$\bra{J, m_J, I, m_I} \hat I \cdot \hat J \ket{J, m_J-1, I, m_I+1} = \frac{\hbar^2}{2} \sqrt{(J-m_J)(J+m_J+1)} \times \sqrt{(I+m_I)(I-m_I+1)}$$

The energy eigenvalues of the resulting matrix can be shown to be

$$ E_{|F = I \pm 1/2,\, m \rangle}(B) = -\frac{\Delta E_{\mathrm{hf}}}{2(2I+1)} + g_I \mu_{\mathrm{B}}\, m B \pm \frac{\Delta E_{\mathrm{hf}}}{2} \sqrt{1 + \frac{4 m x}{2I+1} + x^2}$$

where 

$$ x \equiv \frac{(g_J - g_I)\,\mu_{\mathrm{B}} B}{\Delta E_{\mathrm{hf}}},
  \qquad
  \Delta E_{\mathrm{hf}} = A_{\mathrm{hf}}\left(I + \tfrac{1}{2}\right).$$

Note that in zero-field $x\to 0$, the original hyperfine splitting is recovered. This equation is nasty but powerful because it correctly gives the energy vs. field for our atom's hyperfine states exactly.

### Comments

This result required connecting states of different magnetic quantum number but same total $m$. This mixing is actually impossible at the stretched states. These states at the end of their respective ladders see less of the intermediate-field mixing, and so one expects their energy curvature to differ from the states in the middle of the ladder. Indeed, there is about 2.5 MHz difference between $\Delta E_{-9/2\to -7/2}$ and $\Delta E_{-7/2 \to -5/2}$ when $B\approx 200$ G.