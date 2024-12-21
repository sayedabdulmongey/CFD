# Data-driven Subgrid-scale Modeling of Forced Burgers Turbulence using Deep Learning

## Paper
This implementation is based on the paper:
**[Data-driven subgrid-scale modeling of forced Burgers turbulence using deep learning with generalization to higher Reynolds numbers via transfer learning](https://arxiv.org/abs/2012.06664v1)**.

## Overview
This repository contains the implementation of the deep learning-based model described in the paper. The goal is to develop a subgrid-scale model for forced Burgers turbulence using neural networks.

## Dataset
The dataset used for this implementation is sourced from the paper and can be found [here](https://doi.org/10.5281/zenodo.4316338). It includes simulation data generated for training and evaluation of the subgrid-scale model.

## Code Implementation
The notebook implements the following:

### Data Preparation
- Loading and preprocessing the dataset.
- Preparing the input features and labels required for training the neural network.

### Model Development
- A deep learning model is constructed to predict the subgrid-scale term based on the inputs.
- Utilization of standard deep learning libraries such as Keras (as used in the notebook).
- Implementation of the loss function as described in the paper to minimize the prediction error.

### Training
- The model is trained on the dataset with appropriate training parameters.
- Validation is performed to monitor model performance.

### Evaluation
- The trained model is evaluated on test data to measure its accuracy and generalization ability.
- Metrics such as mean squared error (MSE) and other relevant evaluation criteria are computed.

## External Resources
This implementation follows the methodology and resources provided by the authors. You can find the original implementation [here](https://github.com/envfluids/Burgers_DDP_and_TL).

## Requirements
To run this notebook, ensure you have the following:
- Python 3.7+
- Libraries: TensorFlow, Keras, NumPy, Matplotlib, Scipy

## How to Use
1. Clone this repository and download the dataset from the provided link.
2. Open the notebook and set the path to the dataset.
3. Run the notebook step by step to train and evaluate the model.

## Results
The results, including the model's performance on the test set and its ability to generalize to higher Reynolds numbers, are visualized and discussed in the notebook.

## References
- Paper: [Data-driven subgrid-scale modeling of forced Burgers turbulence using deep learning with generalization to higher Reynolds numbers via transfer learning](https://arxiv.org/abs/2012.06664v1)
- Dataset: [Zenodo Link](https://doi.org/10.5281/zenodo.4316338)
- Original Implementation: [GitHub Repository](https://github.com/envfluids/Burgers_DDP_and_TL)
