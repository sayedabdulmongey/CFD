# Heat Equation Simulation in 3D

In this directory, you will find a Python script that simulates heat diffusion on a 2D plate using the Finite Difference Method (FDM). The simulation solves the heat equation numerically and visualizes the temperature distribution over time in a 3D animated plot.

## Features
- Implements the heat equation using FDM with central differencing.
- Configurable thermal properties and plate dimensions.
- Stability condition enforced for numerical accuracy.
- Boundary conditions applied to simulate a heated plate.
- Generates a 3D animation of the temperature distribution.

## Prerequisites
To run the script, ensure you have the following installed:

- Python 3.7 or later
- Required libraries:
  - `numpy`
  - `matplotlib`
  - `ffmpeg` (for saving the animation as a video)

You can install the Python dependencies with:
```bash
pip install numpy matplotlib
```

To install `ffmpeg`, follow the instructions for your operating system:
- **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html).
- **Linux:** Use your package manager (e.g., `sudo apt install ffmpeg`).
- **MacOS:** Install via Homebrew (`brew install ffmpeg`).

## How It Works

1. **Thermal Properties and Plate Dimensions**:
   - Thermal diffusivity (e.g., copper's diffusivity is used). See [Wikipedia](https://en.wikipedia.org/wiki/Thermal_diffusivity) for more details about thermal diffusivity based on the material.
   - Dimensions of the plate are specified in millimeters.

2. **Finite Difference Method**:
   - The plate is discretized into a grid of nodes.
   - The temperature at each node is updated iteratively based on the heat equation.

3. **Boundary Conditions**:
   - Edges of the plate are fixed at 200°C.
   - Initial temperature of the plate is 25°C.

4. **Simulation Loop**:
   - Updates the temperature at each node over time using the stability condition.
   - Saves the temperature states for visualization.

5. **3D Visualization**:
   - Uses Matplotlib's 3D plotting to display the temperature distribution.
   - The simulation is animated and saved as an MP4 video.

## Code Overview

### Parameters
- `alpha`: Thermal diffusivity of the material (m²/s).
- `Lx, Ly`: Plate dimensions (mm).
- `N`: Number of nodes in each dimension.
- `dx, dy`: Distance between nodes.
- `dt`: Time step for stability.
- `time`: Total simulation duration (seconds).

### Main Sections
- **Initialization**: Sets up the grid, initial temperature, and boundary conditions.
- **Simulation**: Iterates over time steps to compute temperature using FDM.
- **Visualization**: Creates a 3D surface plot and animates the simulation.

## Output
- The animation is saved as `heat_equation_3d_simulation.mp4` in the current directory.

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/sayedabdulmongey/CFD.git
   cd CFD/heat_equation_simulation
   ```

2. Run the script:
   ```bash
   python heat_equation_simulation.py
   ```

3. View the generated video `heat_equation_3d_simulation.mp4`.

## Example
For an example of simulating 2D and 1D heating equations, refer to this [YouTube video](https://www.youtube.com/watch?v=CXOrkQs4WYo).

## Notes
- Ensure the thermal diffusivity matches the material you are simulating.
- The stability condition is critical for accurate results. Avoid altering `dt` without recalculating it based on the stability condition.

---

Feel free to contribute or raise issues for improvements. Happy coding!

