import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the planetary data using the provided orbital elements
orbital_elements = {
    'Mercury': {
        'a': 0.38709927, 'e': 0.20563593, 'I': 7.00497902,
        'L': 252.25032350, 'long_peri': 77.45779628, 'long_node': 48.33076593
    },
    'Venus': {
        'a': 0.72333566, 'e': 0.00677672, 'I': 3.39467605,
        'L': 181.97909950, 'long_peri': 131.60246718, 'long_node': 76.67984255
    },
    'Earth': {
        'a': 1.00000261, 'e': 0.01671123, 'I': -0.00001531,
        'L': 100.46457166, 'long_peri': 102.93768193, 'long_node': 0.0
    },
    'Mars': {
        'a': 1.52371034, 'e': 0.09339410, 'I': 1.84969142,
        'L': -4.55343205, 'long_peri': -23.94362959, 'long_node': 49.55953891
    },
    'Jupiter': {
        'a': 5.20288700, 'e': 0.04838624, 'I': 1.30439695,
        'L': 34.39644051, 'long_peri': 14.72847983, 'long_node': 100.47390909
    },
    'Saturn': {
        'a': 9.53667594, 'e': 0.05386179, 'I': 2.48599187,
        'L': 49.95424423, 'long_peri': 92.59887831, 'long_node': 113.66242448
    },
    'Uranus': {
        'a': 19.18916464, 'e': 0.04725744, 'I': 0.77263783,
        'L': 313.23810451, 'long_peri': 170.95427630, 'long_node': 74.01692503
    },
    'Neptune': {
        'a': 30.06992276, 'e': 0.00859048, 'I': 1.77004347,
        'L': -55.12002969, 'long_peri': 44.96476227, 'long_node': 131.78422574
    },
}

# Function to calculate positions
def keplerian_orbit(planet, t):
    # Constants
    mu = 398600.4418  # Earth's gravitational parameter in km^3/s^2

    # Get orbital elements
    a = orbital_elements[planet]['a'] * 149597870.7  # Convert AU to km
    e = orbital_elements[planet]['e']
    I = np.radians(orbital_elements[planet]['I'])
    L = np.radians(orbital_elements[planet]['L'])
    long_peri = np.radians(orbital_elements[planet]['long_peri'])
    long_node = np.radians(orbital_elements[planet]['long_node'])

    # Mean anomaly
    M = L - long_peri
    M = M + (mu * t) / (a ** 1.5)  # Update M over time

    # Solve Kepler's equation for Eccentric Anomaly
    E = M
    for _ in range(10):  # Simple iterative solution
        E = M + e * np.sin(E)

    # Calculate the true anomaly
    true_anomaly = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2), np.sqrt(1 - e) * np.cos(E / 2))

    # Calculate the distance from the sun
    r = a * (1 - e * np.cos(E))

    # Calculate the position in the orbital plane
    x_orbit = r * np.cos(true_anomaly)
    y_orbit = r * np.sin(true_anomaly)

    # Convert to 3D coordinates (assuming circular orbits in the orbital plane)
    z_orbit = r * np.sin(I)

    # Return position
    return x_orbit, y_orbit, z_orbit

# Time settings for the simulation
time_steps = np.linspace(0, 365.25, 100)  # One year in days
colors = ['gray', 'orange', 'blue', 'red', 'brown', 'gold', 'lightblue', 'darkblue']

# Create an interactive 3D plot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Plotting the orbits
for idx, planet in enumerate(orbital_elements.keys()):
    x, y, z = keplerian_orbit(planet, time_steps)
    ax.plot(x, y, z, label=planet, color=colors[idx])

ax.set_title('Orbits of Planets in the Solar System')
ax.set_xlabel('X Position (km)')
ax.set_ylabel('Y Position (km)')
ax.set_zlabel('Z Position (km)')
ax.legend()
ax.view_init(elev=20, azim=30)  # Set initial view angle

plt.show()
