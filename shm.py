# Graph the position and velocity of an object in a simple harmonic motion
import math
import numpy as np
import matplotlib.pyplot as plt


# Calculate position
def position(t: float, v: float, y: float, w: float) -> float:
    return (y * math.cos(w * t)) + ((v / w) * math.sin(w * t))


# Calculate velocity
def velocity(t: float, v: float, y: float, w: float) -> float:
    return ((-y * math.sin(w * t)) * w) + (v * math.cos(w * t))


# Graph position and velocity
def main():
    time_values = []
    position_values = []
    velocity_values = []
    for i in np.linspace(0, 10, 100):
        time_values.append(i)
        position_values.append(position(i, v, y, w))
        velocity_values.append(velocity(i, v, y, w))
    fig, ax1 = plt.subplots()
    ax1.plot(time_values, position_values, label="Position")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Position")
    ax2 = ax1.twinx()
    ax2.plot(time_values, velocity_values, label="Velocity", color='tab:orange')
    ax2.set_ylabel("Velocity")
    fig.legend()
    fig.tight_layout()
    plt.show()


# Program settings
n = 10  # Iterations
m = 10  # Mass
k = 40  # Spring constant
c = 5  # Damping
y = -4  # Start displacement
v = 0  # Start velocity
w = math.sqrt(k / m)  # Angular frequency

if __name__ == '__main__':
    main()
