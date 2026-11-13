# LEPTONdipole

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24182752.svg)](https://doi.org/10.5281/zenodo.24182752)

A [FeynRules](https://feynrules.irmp.ucl.ac.be/) model implementing dimension-6 **flavor-diagonal leptonic dipole operators** within the Standard Model Effective Field Theory (SMEFT).

This model provides a simplified, lightweight, and dedicated framework focusing strictly on the individual electromagnetic and weak dipole moments of the three charged leptons ($e, \mu, \tau$), intentionally excluding flavor-changing transitions to strictly respect experimental cLFV limits.

> [!TIP]
> **Looking for the full Quark & Lepton Dipole Model?**
> For the complete $3\times 3$ flavor matrix dipole model including both quarks and leptons with general flavor structures (flavor-changing and flavor-diagonal), see the companion repository (coming soon):
> 👉 **[`SMEFTdipole`](https://github.com/YangPhy/SMEFTdipole)**.

---

## 1. Physical Content

### 1.1 Effective Operators
The model extends the Standard Model (SM) with dimension-6 dipole operators restricted to flavor-diagonal entries ($i = j \in \{e, \mu, \tau\}$):

$$
\mathcal{O}_{lW}^{ii} = (\bar{L}_i \sigma^{\mu\nu} \tau^I e_{R,i}) \Phi W_{\mu\nu}^I, \qquad
\mathcal{O}_{lB}^{ii} = (\bar{L}_i \sigma^{\mu\nu} e_{R,i}) \Phi B_{\mu\nu}
$$

The effective interaction Lagrangian is parametrized as:

$$
\mathcal{L}_{\text{BSM}} = \sum_{l = e, \mu, \tau} \left[ \frac{C_{lW}}{\Lambda^2} \mathcal{O}_{lW} + \frac{C_{lB}}{\Lambda^2} \mathcal{O}_{lB} + \text{h.c.} \right]
$$

where each Wilson coefficient is split into its real and imaginary parts:
- **Real parts** ($C_{lB}^{\text{Re}}, C_{lW}^{\text{Re}}$): CP-conserving;
- **Imaginary parts** ($C_{lB}^{\text{Im}}, C_{lW}^{\text{Im}}$): CP-violating.

### 1.2 Mapping to Physical Dipole Moments
After electroweak symmetry breaking, the gauge eigenstates rotate into the photon ($F_{\mu\nu}$) and $Z$ boson ($Z_{\mu\nu}$) field strength tensors:

$$
C_{l\gamma} = \cos\theta_W C_{lB} - \sin\theta_W C_{lW}, \qquad
C_{lZ} = -\sin\theta_W C_{lB} - \cos\theta_W C_{lW}
$$

This directly connects the Wilson coefficients to the experimental observables:

**Anomalous Magnetic Dipole Moment** ($\Delta a_l \equiv (g-2)_l / 2$):

$$
\Delta a_l = \frac{4 \sqrt{2} \, m_l v}{e \, \Lambda^2} \text{Re}(C_{l\gamma})
$$

**Electric Dipole Moment** ($d_l$):

$$
d_l = \frac{\sqrt{2} \, e \, v}{\Lambda^2} \text{Im}(C_{l\gamma})
$$

---

## 2. Directory Structure

- [`SM.fr`](SM.fr): Standard Model base definition.
- [`LEPTONdipole.fr`](LEPTONdipole.fr): Dedicated flavor-diagonal leptonic dipole model definition.
- [`LEPTONdipole.m`](LEPTONdipole.m): Mathematica script for batch model generation in clean kernels.
- [`run.sh`](run.sh): Shell executable wrapper for automated model generation.

---

## 3. Generating the Model Files

Run the provided helper script:

```bash
# 1. Generate ALL model files (Unitary & Feynman gauges for both FA and UFO)
./run.sh

# 2. Generate only UFO models (both Unitary and Feynman gauges)
./run.sh UFO

# 3. Generate only FeynArts models (both Unitary and Feynman gauges)
./run.sh FA

# 4. Generate a single specific target
./run.sh UFO_Unitary     # UFO in Unitary Gauge (recommended for tree-level MG5)
./run.sh UFO_Feynman     # UFO in Feynman Gauge
./run.sh FA_Unitary      # FeynArts in Unitary Gauge
./run.sh FA_Feynman      # FeynArts in Feynman Gauge
```

### 3.1 Generated Outputs

All generated models are strictly **tree-level**:

| Target | Output Directory | Format | Gauge | Recommended Use |
|:---|:---|:---|:---|:---|
| `UFO_Unitary` | `LEPTONdipole_UnitaryGauge_UFO` | UFO (Python) | Unitary | Standard tree-level event generation in MadGraph5 |
| `UFO_Feynman` | `LEPTONdipole_FeynmanGauge_UFO` | UFO (Python) | Feynman | Tree-level with explicit Goldstone and ghost couplings |
| `FA_Unitary`  | `LEPTONdipole_UnitaryGauge_FA`  | FeynArts (`.gen`, `.mod`) | Unitary | Tree-level calculations in FeynArts |
| `FA_Feynman`  | `LEPTONdipole_FeynmanGauge_FA`  | FeynArts (`.gen`, `.mod`) | Feynman | Tree-level calculations in FeynArts |

---

## 4. Using the UFO Model in MadGraph5_aMC@NLO

### 4.1 Installation in MadGraph5

```bash
cp -r LEPTONdipole_UnitaryGauge_UFO /path/to/MG5_aMC_v3_x_x/models/
```

### 4.2 Coupling Orders Hierarchy

| Coupling Order | Scope | Description |
|:---|:---|:---|
| **`NP`** | Global EFT | Overall EFT power expansion ($\Lambda^{-2}$) |
| **`NPRe`** / **`NPIm`** | Global CP | Global switch to filter all CP-even (real) or all CP-odd (imaginary) interactions |
| **`NPCeB`**, **`NPCeW`**, etc. | Operator | Filters a specific operator (both Re and Im parts) |
| **`NPCeWRe`**, **`NPCeWIm`**, **`NPCtaBRe`**, etc. | Component | Filters the real or imaginary part of a specific operator (name = `NPC` + lepton `e`/`mu`/`ta` + `W`/`B` + `Re`/`Im`, no brackets) |

### 4.3 Practical MadGraph5 Examples

```text
MG5_aMC> import model LEPTONdipole_UnitaryGauge_UFO

# SM baseline only (NP = 0)
generate e+ e- > ta+ ta- NP=0

# Isolate the linear SM - CtaW(Re) interference term (tau g-2 effect):
generate e+ e- > ta+ ta- NP^2==1 NPCtaWRe==1

# Isolate the linear SM - CtaW(Im) interference term (tau EDM effect):
generate e+ e- > ta+ ta- NP^2==1 NPCtaWIm==1

# Global CP-odd studies:
generate p p > mu+ mu- NP^2==1 NPIm==1
```

---

## 5. Setting Parameters in `param_card.dat`

### 5.1 Cutoff Scale: `BLOCK EFTINPUTS`
```text
Block EFTINPUTS
    1   1.000000e+03   # LambdaEFT (in GeV, default: 1000.0)
```

### 5.2 Real Parts of Wilson Coefficients: `BLOCK RealWCs`
```text
Block RealWCs
    1   1.000000e+00   # CeBRe   (Real part of CeB)
    2   1.000000e+00   # CeWRe   (Real part of CeW)
    3   1.000000e+00   # CmuBRe  (Real part of CmuB)
    4   1.000000e+00   # CmuWRe  (Real part of CmuW)
    5   1.000000e+00   # CtaBRe  (Real part of CtaB)
    6   1.000000e+00   # CtaWRe  (Real part of CtaW)
```

### 5.3 Imaginary Parts of Wilson Coefficients: `BLOCK ImaginaryWCs`
```text
Block ImaginaryWCs
    1   1.000000e+00   # CeBIm   (Imaginary part of CeB)
    2   1.000000e+00   # CeWIm   (Imaginary part of CeW)
    3   1.000000e+00   # CmuBIm  (Imaginary part of CmuB)
    4   1.000000e+00   # CmuWIm  (Imaginary part of CmuW)
    5   1.000000e+00   # CtaBIm  (Imaginary part of CtaB)
    6   1.000000e+00   # CtaWIm  (Imaginary part of CtaW)
```

---

## 6. Known Issues

1. **Truncated floating-point coupling in some generated UFO files (down-type quark couplings only).**
   Depending on gauge and generation, FeynRules may write a coupling as a long decimal instead of an exact fraction, e.g. in `couplings.py`:
   `value = '-0.3333333333333333*(ee*complex(0,1)*sw)/cw'` (currently `GC_220` in `LEPTONdipole_FeynmanGauge_UFO`; the affected coupling number can change between generations).
   MadGraph5 writes such literals into Fortran with only 7 significant digits (`-3.333333D-01`), so the $Z$ ($\gamma$) coupling to $d$, $s$, $b$ quarks carries a relative error of about $10^{-7}$, i.e. about $5\times 10^{-9}$ in $|M|^2$ for processes such as `e+ e- > b b~`. **Lepton processes (the purpose of this model) are not affected.** To remove the effect, replace the literal by an exact fraction in `couplings.py` (e.g. `-(ee*complex(0,1)*sw)/(3.*cw)`).

2. **Feynman vs. Unitary gauge: small differences from fixed widths.**
   For processes with an internal top quark and a Higgs (e.g. `mu+ mu- > t t~ h`), the SM$\times$dipole interference term can differ between the two gauges by $10^{-4}$ to $10^{-3}$ of the interference term itself ($\sim 10^{-6}$ of the SM rate), because the fixed-width propagators slightly break the Ward identities. The difference vanishes when the widths are set to zero. Importing the Feynman-gauge UFO with `set gauge unitary` reproduces the Unitary-gauge result.


---

## 7. Author Information

- **Author**: Yang Ma (Université catholique de Louvain)
- **Contact**: `mayangluon@pitt.edu`
- **FeynRules Version**: 2.3+

---

## 8. Citation

If you use **LEPTONdipole** in your research, please cite our series of papers:

- D. Buttazzo, G. Levati, Y. Ma, F. Maltoni, P. Paradisi, and Z. Q. Wang, *"Probing $\tau$ lepton dipole moments at future lepton colliders"*, [arXiv:2604.14281](https://arxiv.org/abs/2604.14281) [hep-ph].
- D. Buttazzo, G. Levati, Y. Ma, F. Maltoni, P. Paradisi, and Z. Q. Wang, *"Probing $\tau$ lepton dipole moments at FCC-ee"*, [arXiv:2610.12623](https://arxiv.org/abs/2610.12623) [hep-ph].
- D. Buttazzo, G. Levati, Y. Ma, F. Maltoni, P. Paradisi, and Z. Q. Wang, *"Probing $\tau$ lepton dipole moments at multi-TeV muon colliders"* (*in preparation; arXiv link to be added upon submission*).

Software: [doi:10.5281/zenodo.24182752](https://doi.org/10.5281/zenodo.24182752)

<details>
<summary>BibTeX entries</summary>

```bibtex
@software{Ma:2026LEPTONdipole,
    author    = {Ma, Yang},
    title     = {{LEPTONdipole: Flavor-diagonal charged-lepton dipole operators in the SMEFT (FeynRules / UFO / FeynArts)}},
    year      = {2026},
    publisher = {Zenodo},
    doi       = {10.5281/zenodo.24182752},
    url       = {https://doi.org/10.5281/zenodo.24182752}
}

@article{Buttazzo:2026amk,
    author = "Buttazzo, Dario and Levati, Gabriele and Ma, Yang and Maltoni, Fabio and Paradisi, Paride and Wang, ZeQiang",
    title = "{Probing $\tau$ lepton dipole moments at future Lepton Colliders}",
    eprint = "2604.14281",
    archivePrefix = "arXiv",
    primaryClass = "hep-ph",
    reportNumber = "IRMP-CP3-26-07, CERN-TH-2026-089, COMETA-2026-06",
    month = "4",
    year = "2026"
}

@article{Buttazzo:2026ulg,
    author = "Buttazzo, Dario and Levati, Gabriele and Ma, Yang and Maltoni, Fabio and Paradisi, Paride and Wang, ZeQiang",
    title = "{Probing $\tau$ lepton dipole moments at FCC-ee}",
    eprint = "2610.12623",
    archivePrefix = "arXiv",
    primaryClass = "hep-ph",
    reportNumber = "IRMP-CP3-26-08, COMETA-2026-07",
    month = "10",
    year = "2026"
}
```

</details>
