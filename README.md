# Repository Overview

Welcome to the **Burgers Turbulence and Heat Equation Simulations Repository**. This repository contains implementations of numerical simulations and machine learning-based models applied to fluid dynamics. The main objectives of these projects are to provide insights into physical systems using computational and data-driven approaches.

## Contents of the Repository

### 1. Burgers Turbulence

This folder contains the implementation of the paper:

**"Data-driven subgrid-scale modeling of forced Burgers turbulence using deep learning with generalization to higher Reynolds numbers via transfer learning"**

- **Paper Link**: [https://arxiv.org/abs/2012.06664v1](https://arxiv.org/abs/2012.06664v1)
- **Dataset**: [Zenodo Link](https://doi.org/10.5281/zenodo.4316338)
- **Original Implementation**: [GitHub Repository](https://github.com/envfluids/Burgers_DDP_and_TL)

#### Features:
- Implements a deep learning model for subgrid-scale modeling in forced Burgers turbulence.
- Leverages the dataset provided in the paper for reproducibility and further analysis.

#### Files:
- `vanilla_deeplearning_model.ipynb`: Implementation of the machine learning models and visualization of results.

---

### 2. Heat Equation Simulations

This folder contains a Python script that simulates heat diffusion on a 2D plate using the Finite Difference Method (FDM). The simulation solves the heat equation numerically and visualizes the temperature distribution over time in a 3D animated plot.

#### Features:
- Simulates heat diffusion with configurable thermal properties and plate dimensions.
- Implements the finite difference method (FDM) for numerical solutions.
- Visualizes the results using a 3D animated plot saved as an MP4 video.

#### Prerequisites:
- Python 3.7 or later
- Required libraries: `numpy`, `matplotlib`, `ffmpeg`

#### Files:
- `heat_equation_simulation.py`: The main script for running the simulation.

---

## How to Use
1. **Clone this repository**:
   ```bash
   git clone https://github.com/sayedabdulmongey/CFD.git
   cd CFD
   ```

2. Explore the subfolders for:
   - **Burgers Turbulence**: Implementation of data-driven turbulence modeling.
   - **Heat Equation Simulations**: Numerical simulations of heat diffusion.

3. Follow the individual README files in each folder for specific instructions on running the scripts and notebooks.

## Contribution
Contributions are welcome! Feel free to open issues or submit pull requests to enhance the simulations, documentation, or add new features.


