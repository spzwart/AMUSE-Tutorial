# AMUSE-Tutorial

Here are a number of small AMUSE tutorials in the form of python
notebooks.  These tutorial will (in part) be used for the lecture
series on Simulation and Modeling in astrophysics at Leiden
Observatory of Leiden University, year 2020 September to December.

Further course information can be found at the [wiki](https://github.com/spzwart/AMUSE-Tutorial/wiki)

Responsibility --so-far-- is by Simon Portegies Zwart
But anybody who would like to contribute is welcome.

The course is composed of 12 lectures with an equal number of
assignmnets. In the middele, after 6 lectures (assignmnets) there will
be a small test, and there is a final test at the end.

# List of tutorials:

### scalar_units.ipynb
Exploring some of the capabilities of units in AMUSE

#### learning tasks
 * How to import AMUSE modules.
 * Declare variable and parameters with units.
 * Perform simple mathematical operations on variables with units.
 * Printing results in your preferred units.
 
### particles.ipynb               
Handling particles

#### learning tasks
 * Initialize particle sets.
 * Assign values to particle-set attributes.
 * Use particle-set member functions.
 * Assign a new attribute to a particle set.
 * Manipulate particle sets.
 * Query particle sets and get help.
 * Select specific particles from a set.

#### Not discussed in this tutorial, but probably desired are:
 * Initialize vector attributes in a particle set
 * check for the existence of an attribute
 * particle Supersets and Subsets
 * synchronize_to()
 * get_subset_from()

### running_an_Nbody_code.ipynb   
perform simple N-boyd simulation

#### learning tasks
 * How to generate inital conditions using built-in functions:
   * How to generate a mass-function.
   * How to generate a point-symmetric density distribution of particles.
 * Initializing a direct gravitational N-body code.
 * Initialize and use channels for intra-code data transfer.
 * Detecting binaries.
 * Simple plotting using *matplotlib* and AMUSE-native overloads.
 * Making cumulative distributions

### running_stellarevolution.ipynb  
perform simple stellar evolution calculation

###  running_Nbdoy_with_stellar.ipynb  
Run a stellar evolution code as well as an N-body code and assure that
the result is self consistent.

###  running_Nbody_with_collisions.ipynb
Perform an N-body calculation that includes stellar evolution and
collisions between stars.

#### learning tasks
 * Generate initial conditions.
 * Initialize stellar and N-body codes.
 * More advanced channels for copying specific attributes.
 * Setup stopping conditions.
 * Initiate collision detection.
 * Find a specific particle in another particle set.
 * Merge stars.
 * How to find an interacting subset of particles

###  Bridged_Nbody_with_Galaxy.ipynb   
Simulate a single star (and a cluster) in orbit around the Galactic
center.

###  running_hydrodynamics.ipynb
Evolve a massive single star up to the moment it explodes in a
supernova. After this we inject energy into the inner-region of the
star and follow the hydrodynamics of the explosion by means of a
smoothed-particle hydrodynamics code. 

#### learning tasks
 * Run another AMUSE module to generate initial conditions for yet another code.
 * How to recove the crash of a code and pick-up the result.
 * Store simulation data in the form if python pickel files, and recover from those.
 * plot the result of a hydrodynamical simulation.
 * make an animation of simulation results.
 * Run an AMUSE module as a parallel job.
