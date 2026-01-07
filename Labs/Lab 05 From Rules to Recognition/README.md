# From Rules to Recognition

**Prerequisites:** Understanding of supervised/unsupervised learning concepts

## Part 1: Understanding Decision Trees (30 minutes)

**Activity:** Work through http://www.r2d3.us/visual-intro-to-machine-learning-part-1/

### Section A: Initial Exploration (10 min)

Read through the visualization carefully, interacting with all scroll-triggered animations.

1. What was the first feature (variable) the article suggested for classifying homes? At what value did it split? Why didn't this single feature work well?

2. When they added price per square foot as a second dimension, what two thresholds did they use? Draw a simple 2x2 grid showing the four regions created.

3. How many dimensions (features) does the full dataset have? List at least 4 of them that you can see in the scatterplot matrix.

### Section B: Building Trees (10 min)

4. The article shows finding the "best split" at 240 meters. What percentage of homes are correctly classified with just this one split? What are "false positives" and "false negatives" in this context?

5. Trace through the decision tree for a home with:
   - Elevation: 300 meters
   - Price per sqft: $800
   - Price: $400,000
   
   Which city does the tree predict? Show your path.

6. The article mentions "recursion" - explain what this means in building decision trees. Why can't a computer just test every possible tree?

### Section C: Overfitting Analysis (10 min)

7. The article shows a tree with 100% training accuracy but only 57% test accuracy. Calculate the drop in performance. What does this tell you?

8. Define "overfitting" using the tree visualization as your example. Then give TWO real-world examples where overfitting would be problematic (not houses).

9. If you were a bank using a decision tree to approve loans, would you want a simple tree (maybe 70% accurate) or a complex tree (95% accurate on training data)? Justify your answer.

10. The article ends with "coming up next." Based on what you learned, what do you think the "bias-variance tradeoff" might mean?

## Part 2: Neural Networks in Action (30 minutes)

**Activity:** Play Quick, Draw! at https://quickdraw.withgoogle.com/

### Section A: Initial Exploration (10 min)

Play 6 rounds, varying your drawing style. For each round, note:

| Drawing | AI Guesses | Time to Recognize | Success? |
| --- | --- | --- | --- |
| 1. |  |  |  |
| 2. |  |  |  |
| 3. |  |  |  |
| 4. |  |  |  |
| 5. |  |  |  |
| 6. |  |  |  |

### Section B: Experimenting with the AI (10 min)

11. Pick one object that the AI recognized successfully. Draw it again but:
    - **First:** As simple as possible (minimum lines)
    - **Second:** With lots of extra detail
    - **Third:** From an unusual angle
    
    Which version worked best? What does this tell you about the training data?

12. When the AI fails, what does it guess instead? Pick one failure and explain why the AI might have confused these two objects.

13. Try to "trick" the AI by drawing something that looks like one object but is labeled as another (e.g., draw a circle when it asks for a square). What happens? What does this tell you about how the system learns?

### Section C: Comparing Approaches (10 min)

14. Compare Quick Draw to the decision tree from Part 1:

| Aspect | Decision Tree | Quick Draw |
| --- | --- | --- |
| Type of input data |  |  |
| How it makes decisions |  |  |
| Can it handle messy/imperfect input? |  |  |
| How does it improve? |  |  |

15. Quick Draw says "the more you play, the more it will learn." If you drew 1000 terrible drawings of cats, what would happen to the AI's ability to recognize well-drawn cats? Connect this to overfitting from Part 1.

16. Imagine you're building a system to recognize handwritten medical prescriptions. Would you use a decision tree approach (like Part 1) or a neural network approach (like Quick Draw)? Give 3 reasons for your choice.

17. **Synthesis Question:** Both systems learn from examples (supervised learning from Unit 3). What are the key differences in:
    - How they learn patterns
    - What types of problems they solve best
    - Their strengths and weaknesses

## Submission Requirements

- Answer all numbered questions
- Include your data tables from Quick Draw experiments
- Submit as a single document (PDF or Word)
