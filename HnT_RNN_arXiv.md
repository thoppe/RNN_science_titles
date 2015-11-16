# RNN arXiv
_bro, do you even science?_

*[Travis Hoppe](http://thoppe.github.io/)*, [@metasemantic](https://twitter.com/metasemantic)
----------
[https://github.com/thoppe/RNN_science_titles](https://github.com/thoppe/RNN_science_titles)

====

## New machine learning hotness
#### Recurrent Neural Network (RNN) with the Long Short Term Memory (LSTM)

[The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)

====+
<br>
!(figures/gifs/mb3.gif)<<height:220px; transparent>>
!(figures/gifs/mb2.gif)<<height:220px; transparent>>
!(figures/gifs/mb4.gif)<<height:220px; transparent>>

Really, go read this post -- it's amazing!
====*
## `char-rnn`, Andrej Karpathy
Lua/torch [library](https://github.com/karpathy/char-rnn) to implement a RNN-LSTM.
!(figures/charseq.jpeg)<<height:500px; transparent>> 20 second introduction to RNN

====
## [arXiv.org](http://arxiv.org/)
preprint server for physics, mathematics & CS (160+ categories!)
!(figures/arXiv_cap.png) <<height:600px; transparent>> 
====*
## [arXiv.org/astro.ph](http://arxiv.org/list/astro-ph/recent)
titles are short learnable "patterns"
!(figures/arXiv_titles.png) <<height:600px>>
=====
## Data Wrangling

spider arXiv $\rightarrow$ unidecode ($\beta \rightarrow b$) $\rightarrow$ 
strip all characters except `[a-z][A-Z][0-9][_-()]`

## Machine Learning
Trained all categories on the same set of hyperparameters:

`1024` RNN size, `2` layers, `30` max epochs, `0.5` dropout,
`50` sequence length, `0.002` learning rate, `0.97` decay, `50` batch size

Took top cross-validated model (sometimes error exploded!).

=====
# Size Matters!
!(figures/validation_vs_input.png) <<height:600px>> Fixed hyperparameters for all models, exponential fit
====
## Examples (low quality)
chem-ph (validation score 3.19)
    C
    on
    on
    o
    n
    o
    o

q-bio.CB (1.48)
    A Mathematical model
    stochastic model of cells
    Protein
    Expression
    System
    The single cells
    Model of protocells
    Mathematical self-oscillation
    Formation of Plasticity


====*
## Examples (medium quality)
cs.AI (1.02)
    Semantic Based Medical Image Retrieval
    Structure Generation Entropy Space: Advances in Structural Mechanism
    Monitoring E- A complete systems
    Description Logics Design
    Indexer Based Markov Control Assessment
    Estimation of Approximate Datasets
    Local Search Space Selection for Text Constraints
    Approximation by Space Preferences
    Availability of Probability Theory

math.DS (0.91)
    Multifractal analysis for Lebesgue space
    Quadratic Jump Central Triangles
    Turbulence relations and fractal measures
    Wandering points for autonomous resonances
    Limit Sets of Infinite Torus Orbit
    The bifurcation of surface diffeomorphisms with negatively curved manifolds
    Algorithmic entropy and quadratic variables in quasi-topological Dynamical Networks
    Statistical reductions for reaction-diffusion equations


====*
## Examples (high quality)
astro-ph (0.77)
    Geometrical electron capture of July 2000 To 1001
    The Solar Dynamics Observatory
    Constraining the White-Light Flare of Protostellar Outflows with an Edge
    The New Color Laboratory Wave Event of Extremely Open Clusters
    Post-M dwarfs from the NIR spectral indices
    The UV-UV Observations of Sunspot Images
    The Narrow-Band Temporal Properties of Dark Clouds with Accurate Supernova
    Blazhko Relationship between Coronal Wave cores
    Dynamics and Shock Wave Instability in Massive Stars with Massive Stars

hep-ph (0.74)
    Search for CP-Violation in Right-Handed Neutrinos
    Neutron Star Propagation as a Source of the Hadron-Hadron Scattering Measurement at the Planck Scale
    Goldstone bosons and scattering modes from two-dimensional Hamiltonians
    Baryogenesis with Yukawa Unified SUSY GUTs
    Radial scattering and dense quark matter and chiral phase transition of a pseudoscalar meson at finite baryon density
    Transition Form Factor Constant in a Quark-Diquark Model
    A New Theory of Supersymmetry Breaking
    Effective gluon propagator in QCD at zero and finite temperature and and dual gauge QCD in the BCS-BCS limit
    Light scalar pair signals in top quark multiple polarization

====*

## Bro do you even science?

Which of these are real? Which are fake? 

    1. A User-Friendly Code to Diagnose Chromospheric Plasmas
    2. Shock Parameters in Astrophysics
    3. Wormholes in the accelerating universe
    4. Phase recovering by Electron Deconvolution on Gravitational Wave Signals
    5. Averaging and Cosmological Observations
    6. Developments of global mass function
    7. VIMOS total transmission profiles for broad-band filters
    8. Bayesian plane for MACS. Atmospheric Cherenkov Telescopes
    9. Gaseous Inner Disks
    10. Science and Fluorescence Detection Time Scales with Transient Least Squares II. Mask coronagraphs
    11. Dissipation of Magnetic Flux in Primordial Star Formation: From Run-away Phase to Mass Accretion Phase
    12. High-energy Cosmic Ray Shower Observations on Pulsar Disk
    13. Thermal inertia of near-Earth asteroids and implications for the magnitude of the Yarkovsky effect
    14. Activity Ionization and Instrumentation
    15. A 610 MHz Survey of the 1H XMM-Newton Chandra Survey Field
    16. Estimating visible variability in the neutron a cross-correlations

====
# What's next?
Any large, consistent corpus of text...

[Political speeches](http://users.wfu.edu/louden/Political%20Communication/Class%20Information/SPEECHES.html)
Political treaties (eg. [TPP](https://ustr.gov/tpp/))
[DNA](http://www.ncbi.nlm.nih.gov/genbank/), [RNA](http://rnacentral.org/), [protein sequences](http://www.uniprot.org/)
[Rap lyrics](http://rap.genius.com/) & [poems](https://www.poets.org/)
[Paper abstracts](http://www.scopus.com/)


====
# Thanks, you!
Tweet more ideas to [@metasemantic](https://twitter.com/metasemantic)!
