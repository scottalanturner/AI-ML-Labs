# 🧠 Neural Network Playground — Instructor Build Guide

This guide explains how to create a single Google Colab notebook for a 45–60 minute hands-on lab suitable for beginners (even middle schoolers).

---

## 🪜 Overview

Students will explore how neural networks learn through **three short visual experiments** — all runnable without any coding knowledge.

1. **Teach the Computer to Read Numbers (MNIST)** — supervised learning.  
2. **Too Smart for Its Own Good** — overfitting demonstration.  
3. **Draw the Decision Boundary** — how neural networks separate groups.

Students only press “Run” and adjust dropdowns/sliders.

---

## 🧩 Step 1 – Create a New Colab Notebook

1. Go to [Google Colab](https://colab.research.google.com/).  
2. Click **File → New Notebook**.  
3. Rename it: `Neural_Network_Playground.ipynb`.

---

## 🧩 Step 2 – Title + Introduction

**Add a new Markdown cell** and paste:

```markdown
### 🧠 Neural Network Playground  
**Time:** 45–60 minutes  
**Goal:** See how a neural network learns, makes mistakes, and changes as we make it bigger or smaller — without writing code.

We’ll run 3 quick experiments:
1. Teach the computer to **read numbers** (supervised learning).  
2. See when a model becomes **too smart for its own good** (overfitting).  
3. Watch how neural nets **draw decision boundaries** between two groups.

Just click **Runtime → Run all** or press ▶️ in each section.  
You **don’t need to change code** — just follow the prompts.
```

---

## 🧩 Step 3 – Setup

**Add a new code cell** and paste:

```python
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import ipywidgets as widgets
from IPython.display import display, clear_output

print("✅ Environment ready.")
```

---

## 🧩 Step 4 – Part 1: Teach the Computer to Read Numbers

### Markdown cell

```markdown
## 🧩 Part 1: Teach the Computer to Read Numbers
A neural network learns patterns from examples — just like us.

We’ll train a simple model to recognize handwritten digits (0–9).

**Steps:**
1. Run the training cell.
2. Watch accuracy improve.
3. Pick an image number (0–99) and see what the model guesses.
```

### Code cell

```python
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model1 = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model1.compile(optimizer='adam',
               loss='sparse_categorical_crossentropy',
               metrics=['accuracy'])

print("Training the model (about 15 sec)...")
history = model1.fit(x_train, y_train, epochs=5, validation_split=0.1, verbose=0)

plt.plot(history.history['accuracy'], label='Train Acc')
plt.plot(history.history['val_accuracy'], label='Val Acc')
plt.title('Training Progress')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
```

### Interactive cell

```python
index_slider = widgets.IntSlider(min=0, max=99, step=1, value=0, description="Test image #")
display(index_slider)

def show_prediction(change=None):
    idx = index_slider.value
    img = x_test[idx]
    true_label = y_test[idx]
    pred = np.argmax(model1.predict(img.reshape(1, 28, 28)))
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.title(f"Prediction: {pred} | True: {true_label}")
    plt.show()

index_slider.observe(show_prediction, names='value')
show_prediction()
```

---

## 🧩 Step 5 – Part 2: Too Smart for Its Own Good (Overfitting)

### Markdown cell

```markdown
## 🧩 Part 2: Too Smart for Its Own Good
Sometimes bigger models memorize training data but perform worse on new data — that’s called **overfitting**.

You’ll compare a **small** model and a **big** model on the same problem.
```

### Code cell

```python
X, y = make_moons(noise=0.2, random_state=42, n_samples=1000)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

def build_model(size="small"):
    model = keras.Sequential()
    model.add(keras.layers.Input(shape=(2,)))
    if size == "big":
        for _ in range(5):
            model.add(keras.layers.Dense(32, activation='relu'))
    else:
        model.add(keras.layers.Dense(8, activation='relu'))
    model.add(keras.layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train_and_plot(size="small"):
    clear_output(wait=True)
    print(f"Training {size} model...")
    model = build_model(size)
    history = model.fit(X_train, y_train, epochs=20, verbose=0, validation_data=(X_test, y_test))
    plt.plot(history.history['accuracy'], label='Train Acc')
    plt.plot(history.history['val_accuracy'], label='Val Acc')
    plt.title(f"{size.capitalize()} Model Accuracy")
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()

dropdown = widgets.Dropdown(options=['small', 'big'], value='small', description='Model size:')
widgets.interactive(train_and_plot, size=dropdown)
```

---

## 🧩 Step 6 – Part 3: Draw the Decision Boundary

### Markdown cell

```markdown
## 🧩 Part 3: Draw the Decision Boundary
Neural networks learn “shapes” to separate different classes.

Move the slider below to see how changing the number of neurons
makes the decision boundary more or less wiggly.
```

### Code cell

```python
X, y = make_moons(noise=0.25, random_state=1, n_samples=300)

def plot_boundary(neurons=4):
    clear_output(wait=True)
    model = keras.Sequential([
        keras.layers.Dense(neurons, activation='tanh', input_shape=(2,)),
        keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X, y, epochs=30, verbose=0)
    
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                         np.linspace(y_min, y_max, 200))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    plt.contourf(xx, yy, Z, alpha=0.6, cmap='coolwarm')
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolors='k')
    plt.title(f"Neurons: {neurons}")
    plt.show()

slider = widgets.IntSlider(min=2, max=32, step=2, value=4, description='Neurons:')
widgets.interactive(plot_boundary, neurons=slider)
```

---

## 🧩 Step 7 – Wrap-Up

**Add a Markdown cell:**

```markdown
## 🧩 Wrap-Up & Reflection

Answer these quick questions (in your notes or discussion):
1. What did the model learn to do in Part 1?  
2. Why did the "big" model in Part 2 perform worse on new data?  
3. In Part 3, what did increasing neurons change about the border shape?  

⭐ **Key idea:** Neural networks learn patterns.  
Small ones may be too simple; big ones may memorize too much.  
We want the model to be *just right* for new data.
```

---

## ✅ Timing Suggestion (Instructor)

| Section | Time | Notes |
|----------|------|-------|
| Setup & Part 1 | 15 min | Run & visualize digit recognition |
| Part 2 | 15 min | Overfitting demo |
| Part 3 | 15 min | Decision boundaries |
| Wrap-Up | 5 min | Discussion |

---

**End of Guide**
