# AMUSE-Tutorial

Here are a number of small AMUSE tutorials in the form of python
notebooks.  These tutorial will (in part) be used for the lecture
series on Simulation and Modeling in astrophysics at Leiden
Observatory of Leiden University, year 2020 September to December.

Further course information can be found at the
[wiki](https://github.com/spzwart/AMUSE-Tutorial/wiki)

Responsibility --so-far-- is by Simon Portegies Zwart
But anybody who would like to contribute is welcome.

The course is composed of 12 lectures with an equal number of
assignmnets. In the middele, after 6 lectures (assignmnets) there will
be a small test, and there is a final test at the end.

# List of tutorials:

## scalar_units.ipynb
Exploring some of the capabilities of units in AMUSE

#### Learning objectives
 * How to import AMUSE modules.
 * Declare variable and parameters with units.
 * Perform simple mathematical operations on variables with units.
 * Printing results in your preferred units.
 
## particles.ipynb
Handling particles

#### Learning objectives
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

## Nemesis_and_the_Sun.ipynb
Learn how to use modules and set up binary and multiple systems.

#### Learning objectives
 * Set-up a particle set.
 * Initialize planetary system.
 * Converting orbital elements to Cartesian coordinates.
 * Generate binary from orbital elements.

## running_an_Nbody_code.ipynb   
perform simple N-boyd simulation

#### Learning objectives
 * How to generate inital conditions using built-in functions:
   * How to generate a mass-function.
   * How to generate a point-symmetric density distribution of particles.
 * Initializing a direct gravitational N-body code.
 * Initialize and use channels for intra-code data transfer.
 * Detecting binaries.
 * Simple plotting using *matplotlib* and AMUSE-native overloads.
 * Making cumulative distributions

## running_stellarevolution.ipynb  
Perform simple stellar evolution calculation by setting up a stellar
mass-function, declaring the stellar evolution code and run it to a
certain moment in time.

#### Learning objectives
 * Generate stellar mass-function from internal AMUSE routine.
 * Plot the results.
 * Use channels from and to running modules.

##  running_Nbdoy_with_stellar.ipynb  
Run a stellar evolution code as well as an N-body code and assure that
the result is self consistent.

#### Learning objectives
 * Initiate multiple independent codes.
 * exchange information from one code to another.
 * Use Channels across modules.
 * Plot results.

##  running_Nbody_with_collisions.ipynb
Perform an N-body calculation that includes stellar evolution and
collisions between stars.

#### Learning objectives
 * Channels
 * Generate initial conditions.
 * Initialize stellar and N-body codes.
 * More advanced channels for copying specific attributes.
 * Sstopping conditions.
 * Initiate collision detection.
 * Find a specific particle in another particle set.
 * Merge stars.
 * How to find an interacting subset of particles

##  bridged_Nbody_with_Galaxy.ipynb   
Simulate a single star (and a cluster) in orbit around the Galactic
center.

#### Learning objectives
 * Single-directional hierarchical code coupling strategy (i.e. classice bridge).
 * Bridge timesteps.
 * Constructing classes in Python
 * Incorporating an external potential to an N-body simulation
 * Appreciate the role of get_gravity_at_point function in bridge.
 * Appreciate the role of get_potential_at_point function in bridge.

##  gravity_cascaded_bridges.ipynb
Simulate several planetary system, each with their own N-body
integrator, and the lot integrated in another N-body code.  Note that
here the interactions of one planet to the planets around another star
are ignored in this implementation.

#### Learning objectives
 * use a cascade of bridges

## high_order_bridge.ipynb
**Not yet documented**
**Not yet working**
You simulate a debris disk around a moon, in orbit around a planet, in
orbit around a star. This requires a higher order bridge, in order to
assure that the orbital integration is performed with sufficient
precision and accuracy.

#### Learning objectives
 * Initialize a two-way bridge
 * High-order bridge initalization
 * How to construct a disk around a celestial body.

## hierachical_bridges.ipynb
**Not yet documented**
Construct a hierarchial bridge to integrate a highly hierarchical
system of star and planets.

#### Learning objectives
 * Non-linear coupling strategies (bridge).
 * Hierarchical coupling strategies (bridge).
 * Multiple channels to single particle set.

##  running_hydrodynamics.ipynb
Evolve a massive single star up to the moment it explodes in a
supernova. After this we inject energy into the inner-region of the
star and follow the hydrodynamics of the explosion by means of a
smoothed-particle hydrodynamics code. 

#### Learning objectives
 * Run another AMUSE module to generate initial conditions for yet another code.
 * How to recove the crash of a code and pick-up the result.
 * Store simulation data in the form if python pickel files, and recover from those.
 * plot the result of a hydrodynamical simulation.
 * make an animation of simulation results.
 * Run an AMUSE module as a parallel job.

## bridge_gravity_with_hydro.ipynb


## running_radiative_transport.ipynb
**Not yet constructed**


### License
[MIT](http://www.opensource.org/licenses/mit-license.php)

