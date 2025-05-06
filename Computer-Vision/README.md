# Teachable Machine Lab: The "Desk Object Sorter" with GitHub README Reflection

**Objective:**
Students will learn the fundamentals of supervised machine learning, specifically image classification, by training a model to recognize common desk objects. You will understand training data, classes, model training, testing, and the impact of data quality. You will also explore bias in AI. **A key outcome will be exporting the trained model, managing it within a GitHub repository, and documenting your learning and reflections directly in the project's README file.**

**Estimated Time:** 2 - 3 hours (including data gathering, training, testing, model export, GitHub submission with README reflection)

**Core AI Concepts Covered:**
* Supervised Learning
* Image Classification
* Training Data, Classes/Labels
* Model Training, Testing & Evaluation
* Confidence Score
* Iteration & Refinement
* Bias in AI (Introduction)
* Model Export & Portability
* Version Control & Project Documentation (via GitHub README)

**Materials Needed:**
* A computer with internet access and a webcam.
* Access to the Teachable Machine website (g.co/teachablemachine).
* A variety of 3-5 common, distinct objects from a student's desk.
* A GitHub account.
* Optional: Smartphone camera for still photos.

**Deliverables:**
1.  A link to a public GitHub repository containing:
    * Their exported Teachable Machine model files (`model.json`, `weights.bin`, `metadata.json`).
    * A comprehensive `README.md` file that includes:
        * A project title and brief description.
        * A list of the classes their model can identify.
        * **Thoughtful answers to the Discussion & Reflection questions (listed below).**
        * (Optional but encouraged) Any other interesting observations, challenges faced, or a screenshot of their Teachable Machine interface.

# Introduction

Alright, let's dive into the exciting world of machine learning without needing to write a single line of code! This lab will introduce you to Google's Teachable Machine, a fantastic and accessible web-based tool that empowers you to create your own machine learning models using just your webcam, microphone, or files.

Forget complex algorithms and endless lines of Python. With Teachable Machine, you'll experience the core concepts of machine learning – data collection, training, and model evaluation – in a hands-on and intuitive way. You'll be amazed at how quickly you can teach a computer to recognize images, sounds, or even poses!

In this session, we'll guide you through the simple steps of:

* **Gathering your own data:** You'll use your creativity to collect examples that your model will learn from.
* **Training your model:** You'll witness how the magic happens as the tool learns patterns from your data.
* **Testing and refining your model:** You'll put your creation to the test and see how well it performs, making adjustments as needed.

By the end of this lab, you'll not only have a working machine learning model but also a fundamental understanding of how these powerful technologies work. So, get ready to unleash your inner data scientist and discover the incredible possibilities of Teachable Machine! Let's get started!

# Lab Procedure

**Part 1: Planning & Data Collection (Approx. 30-45 minutes)**

1.  Open a browser and visit [Teachable Machine](https://teachablemachine.withgoogle.com/)
2.  Once the page loads, you'll see a few options. We want to create a new project. Look for a button that says something like 'Get Started' or 'Create new project'. Click on that button.  
3. For this lab, we'll be working with images. You'll see three project types: Image Project, Audio Project, and Pose Project. Click on 'Image Project'.
4. Now you'll have a choice between 'Standard' and 'Embedded' image projects. For today's lab, let's choose the 'Standard' image project. Click on that option.
5. Now you're in the main workspace. Notice the section labeled 'Gather'. Here, we'll define the different categories, or 'classes,' that our machine learning model will learn to recognize. You'll see a default 'Class 1'. Click on the word 'Class 1' to rename it to your first category. For example, if you want to teach the machine to recognize pictures of pencils, type in 'Pencils' and press Enter.
2.  **Define Your Classes (5 mins):** Students choose 3-5 distinct desk objects.
3.  **Gather Training Data (20-35 mins):**
    * Open Teachable Machine ("Image Project").
    * For each class: Name it, use "Webcam" to capture **30-50+ images**, ensuring variety (angles, backgrounds, lighting, distances) and avoiding clutter.

**Part 2: Model Training & Initial Testing (Approx. 20-30 minutes)**

1.  **Train the Model (5-10 mins):** Click "Train Model."
2.  **Initial Testing & Evaluation (15-20 mins):** Use "Preview" pane (webcam) to test with training objects, variations, and negative examples. Observe predictions and confidence scores.

**Part 3: Iteration, Refinement & Model Export (Approx. 30-45 minutes)**

1.  **Identify Weaknesses & Iterate (15-20 mins):**
    * Based on testing, identify where the model struggles. Add more targeted image samples to weaker classes.
    * Retrain and test again.
2.  **Export Your Model (15-25 mins):**
    * Once reasonably satisfied, click "Export Model."
    * Under "Tensorflow.js" tab, click "**Download**" to get the model files (`model.json`, `weights.bin`, `metadata.json`). Save these in a dedicated project folder.

**Part 4: GitHub Submission & README Reflection (Approx. 45-75 minutes)**

1.  **Prepare GitHub Repository & Upload Files (15-25 mins):**
    * Go to GitHub. Create a new public repository (e.g., "desk-object-sorter-ai") or a new folder in an existing course repository.
    * Upload the `model.json`, `weights.bin`, and `metadata.json` files to this repository/folder (via Git commands or GitHub web upload).
2.  **Create/Update README.md with Integrated Reflection (30-50 mins):**
    * In the same GitHub repository/folder, create or edit a `README.md` file.
    * This file **must** include the following sections:

        ```markdown
        # [Your Project Title - e.g., AI Desk Object Sorter]

        ## Project Description
        A brief (1-2 sentence) description of your project. For example: "This project uses Google's Teachable Machine to classify common objects found on my desk."

        ## Classes Identified
        List the objects your model was trained to identify:
        * Class 1 (e.g., Mug)
        * Class 2 (e.g., Pen)
        * Class 3 (e.g., Keys)
        * [Add more as needed]

        ## Discussion & Reflection
        *(Please answer the following questions thoughtfully)*

        1.  **Model Performance & Iteration:**
            * How accurate was your first trained model?
            * What steps did you take to iterate and improve its performance? (e.g., added more images, diversified image types for a specific class).
            * How did these changes affect the model's accuracy and confidence scores?

        2.  **Challenges & Observations:**
            * Which objects were the easiest for your model to learn and distinguish? Why do you think that was?
            * Which objects were the most challenging? What made them difficult (e.g., similar shapes, variable appearances)?
            * What happened when you showed the model an object it wasn't trained on? How did the confidence scores behave, and why is this significant?

        3.  **Bias in AI:**
            * If you only trained your "mug" class with images of *your specific mug* (and didn't vary color, shape, etc.), how well do you think it would recognize other students' significantly different mugs? How does this illustrate the concept of bias being introduced through training data?
            * Imagine all your training images were taken in very bright, direct lighting. What might happen if you tried to use the model in a dimly lit room or with strong shadows? How does this relate to the robustness and potential biases of AI models?

        4.  **Model Limitations & Usefulness:**
            * What are some key limitations of the model you created?
            * Why is it useful to be able to download your trained model files (like `model.json`, `weights.bin`) and share them (e.g., via GitHub)? What does this enable?

        5.  **Real-World Applications & Ethics:**
            * Brainstorm 2-3 real-world applications where a similar image classification model could be useful.
            * Briefly discuss one ethical consideration that developers should keep in mind when building and deploying image recognition AI in the real world (e.g., related to fairness, privacy, misuse).

        ## (Optional) Challenges Faced / Interesting Discoveries
        * Add any other specific challenges you encountered or interesting things you discovered during this lab.

        ## (Optional) Screenshot
        * You can embed a screenshot of your Teachable Machine interface here if you like.
        ```
    * Students should fill in all sections, especially providing detailed answers to the Discussion & Reflection questions.

