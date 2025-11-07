# Neural Network Playground

## Overview

The **Neural Network Playground** is an interactive Jupyter notebook designed for beginners (including middle school students) to explore how neural networks learn through hands-on experiments. This 45-60 minute lab requires no coding knowledge — students simply run cells and interact with sliders and dropdowns to see neural networks in action.

### What Students Will Learn

The notebook contains **three interactive experiments**:

1. **Teach the Computer to Read Numbers (MNIST)**
   - Students watch a neural network learn to recognize handwritten digits (0-9)
   - Interactive slider lets them test the model on new images
   - Visualizes training progress and prediction confidence

2. **Too Smart for Its Own Good (Overfitting)**
   - Compares simple vs. complex neural networks
   - Demonstrates how bigger models can "memorize" training data but fail on new data
   - Interactive dropdown to switch between model sizes

3. **Draw the Decision Boundary**
   - Visualizes how neural networks separate different groups of data
   - Interactive slider to adjust model complexity
   - Shows how more neurons create more complex (and sometimes problematic) boundaries

### Key Features

- **No coding required** — Students only interact with widgets
- **Visual and interactive** — Graphs, sliders, and real-time predictions
- **Age-appropriate explanations** — Technical concepts explained in simple terms
- **Built with PyTorch** — Uses modern deep learning framework
- **Self-contained** — All dependencies clearly explained

---

## Why Use Google Colab?

### 🚀 **Open in Google Colab** 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sturner/AI-ML-Labs/blob/main/Labs/Module%209%20Deep%20Learning/Neural_Network_Playground.ipynb)

### Benefits of Using Colab

1. **Zero Setup Required**
   - No need to install Python, PyTorch, or any libraries
   - No environment configuration or dependency management
   - Students can start learning immediately

2. **Pre-Configured Environment**
   - All required libraries (PyTorch, NumPy, Matplotlib, etc.) are pre-installed
   - GPU access available for free (though not needed for this notebook)
   - Consistent environment for all students

3. **Easy Access & Sharing**
   - Works on any device with a web browser (Chromebooks, tablets, etc.)
   - No software installation needed on school computers
   - Share with a single link — no file downloads required

4. **Cloud-Based & Auto-Save**
   - Work is automatically saved to Google Drive
   - No risk of losing work if a computer crashes
   - Students can access their work from any device

5. **Free & Accessible**
   - No cost for students or schools
   - No account required for basic use (though saving requires a Google account)
   - Works on low-end devices since computation happens in the cloud

6. **Perfect for Education**
   - Eliminates technical barriers that prevent students from learning
   - Allows focus on concepts rather than troubleshooting setup issues
   - Enables remote learning and asynchronous instruction

### Alternative: Local Installation

If you prefer to run the notebook locally, you'll need:
- Python 3.7+
- PyTorch
- NumPy, Matplotlib, scikit-learn
- Jupyter Notebook or JupyterLab
- ipywidgets

However, for educational settings, **Colab is strongly recommended** to ensure all students can participate without technical barriers.

---

## Usage Instructions

1. Click the "Open in Colab" badge above (or upload the notebook to Colab)
2. Click **Runtime → Run All** to execute all cells
3. Follow the markdown instructions in each section
4. Interact with sliders and dropdowns to explore the experiments
5. No code modification needed — just run and explore!

---

## Learning Objectives

By the end of this lab, students will understand:
- How neural networks learn from examples
- The concept of training vs. test accuracy
- What overfitting is and why it's a problem
- How model complexity affects learning
- The relationship between neurons and decision boundaries

---

## Files in This Directory

- `Neural_Network_Playground.ipynb` — The main interactive notebook
- `Neural_Network_Playground_Instructions.md` — Instructor build guide (for creating the notebook)
- `README.md` — This file

---

## Notes for Instructors

- The notebook is designed for 45-60 minutes
- All explanations are written at an 8th-grade reading level
- Technical terms (ReLU, sigmoid, etc.) are explained in simple analogies
- Students don't need to modify any code — just run cells and interact
- Consider having students work in pairs to discuss observations

---

*Last Updated: 2024*

