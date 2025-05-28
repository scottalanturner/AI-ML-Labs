
# Wine Quality MLOps Lab

## Overview

This lab introduces MLOps (Machine Learning Operations) concepts through wine quality prediction using multiple algorithms. It is designed for undergraduate students learning machine learning model management, experiment tracking, and deployment workflows using industry-standard tools.

## Learning Objectives

By completing this lab, you will:
- Execute end-to-end machine learning workflows in a professional environment
- Utilize experiment tracking tools for model management and comparison
- Interpret model results and feature importance analysis
- Connect ML concepts to career applications in your field

## Getting Started

You will run this lab on [Databricks](https://www.databricks.com/). Databricks is a cloud-based platform used for data engineering, machine learning, and analytics. It’s built on Apache Spark and enables teams to collaborate on big data projects using notebooks and pipelines.

Databricks makes MLOps easier and scalable by combining code, data, experiments, deployment, and monitoring in one place. It’s a one-stop shop for production-ready ML workflows.

Databricks has a free 14-day trial that **does not** require you to input a credit card to use it.

### Prerequisites

- Databricks account access
- Basic understanding of machine learning concepts
- Familiarity with Python programming
- Required libraries (pre-installed on Databricks):
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - mlflow
  - xgboost
  - hyperopt

# Watch these videos first
This lab is going to introduce some new concepts that have not been covered in the course. Watch these two videos to reinforce the topics we have already covered, and to introduce you to some new algorithms and measurments used in the lab. 

- [Decision Trees, Random Forests and Gradient Boosting: What's the Difference?](https://www.youtube.com/watch?v=uV2gdNt2MLc) You've already learned about decision trees and random forests. There is another strategy called boosting that we need to learn to understand the XGBoost algorithm used in this lab. 
- [ROC and AUC, Clearly Explained](https://www.youtube.com/watch?v=4jRBRDbJemM). How do we know if our model is any good? We need a new way to measure.

### Lab Files

- `MLOps on Databricks.ipynb`: The main Jupyter notebook containing all lab instructions, code, and MLOps workflows
- Wine quality dataset (accessed through Databricks datasets)

## Lab Structure

The Jupyter notebook guides you through:

1. MLflow configuration and Unity Catalog setup
2. Data exploration and preprocessing
3. Building baseline and optimized models
4. Experiment tracking with MLflow
5. Model registry and version management
6. Production model deployment workflows

## Homework Submission

Complete all analysis questions at the end of the notebook and submit the required screenshots showing:
- Feature importance results
- MLflow experiment tracking
- Model registry with version management
- Key visualizations from your analysis

As in other labs, you will submit your work to a new folder in your GitHub repo. 

## Resources

If you need additional help:
- Review the explanations provided in each section of the notebook
- Use Databricks documentation for platform-specific questions
- Practice your prompt engineering skills by asking ChatGPT about MLOps concepts
- Email the instructors for technical support
