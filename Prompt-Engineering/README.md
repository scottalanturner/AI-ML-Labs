# Prompt Engineering Assignment

## Overview
In this assignment, you will apply prompt engineering techniques to generate a SWOT (Strengths, Weaknesses, Opportunities, Threats) analysis for a company of your choice within your desired field of work. You will explore job postings on Indeed.com to select a company, use multiple Large Language Models (LLMs) available to you to generate SWOT analyses, and refine your prompts iteratively to improve outcomes, culminating in a final revision that ties your field of study to an interview context. This lab focuses on the process of achieving a high-quality result through experimentation and comparison, resulting in a polished deliverable set.

## Learning Outcomes
By the end of this lab, you will:
- Understand iterative prompt engineering tailored to real-world scenarios.
- Compare accessible LLMs for practical tasks.
- Apply your field of study to an interview-relevant SWOT analysis.
- Develop skills in documenting and presenting work using GitHub.

## Instructions

### Step 1: Select a Company
**Explore Job Postings:**
- Visit Indeed.com and search for job postings in your desired field of work (e.g., software development, healthcare, marketing, data analytics, etc.).
- Identify a company that interests you based on the job description, company details, or industry relevance. Note the company name and any relevant details (e.g., industry, size, location) that might inform your SWOT analysis.

### Step 2: Set Up Your Environment
**Choose LLMs:**
- Select at least two LLMs from the following options:
  - University-Provided LLMs: Free access is available to university-hosted models.
  - Free or Pre-Subscribed Services: You may also use Perplexity, Duck.ai, or any paid service you already have a subscription to (e.g., ChatGPT, if you've paid for it personally).
- Justify your choices briefly (e.g., ease of use, perceived capability, familiarity) in your Google Doc under a "LLM Selection" heading. Note: You will not have access to playgrounds or paid APIs beyond what you already subscribe to or what the university provides.

**Create a GitHub Repository:**
- Set up a public GitHub repository named AI-ML-Prompt-Engineering-Lab.
- Initialize it with a README.md file describing the lab purpose and your selected company.
- Hint: Use prompting to get instructions on how to do this, step-by-step. 

### Step 3: Initial Prompt Design and Execution
**Craft an Initial Prompt:**
- Develop a simple initial prompt to generate a SWOT analysis for your chosen company. For example:
  - "Generate a SWOT analysis for [Company Name], a [industry] company based in [location]."
- Keep it broad to establish a baseline.

**Run the Prompt:**
- Execute this prompt on both selected LLMs.
- Save the raw outputs in a single Google Doc titled Prompt_Revisions_[YourName]. Use headings like "SWOT Initial Prompt #1 - [LLM Name]" and "SWOT Initial Prompt #2 - [LLM Name]" for each output.

### Step 4: Analyze and Revise Prompts
**Evaluate Initial Outputs:**
- Review the SWOT analyses from both LLMs. Note strengths (e.g., detail, relevance), weaknesses (e.g., vagueness, inaccuracies), and differences between the models in your Google Doc under a "Comparison and Analysis" heading after each iteration.

**Revise Your Prompt (Iteration 1):**
- Refine the prompt to improve clarity, specificity, or structure. For example:
  - "Generate a SWOT analysis for [Company Name], a [industry] company based in [location]. Include specific examples for each category (Strengths, Weaknesses, Opportunities, Threats) and focus on [specific aspect, e.g., technology, market position]."
- Run the revised prompt on both LLMs and record outputs in the Google Doc under headings like "SWOT Iteration 1 #1 - [LLM Name]" and "SWOT Iteration 1 #2 - [LLM Name]".

**Revise Again (Iteration 2):**
- Further refine the prompt, adding constraints (e.g., tone, length) or format specifications (e.g., bullet points). For example:
  - "Generate a SWOT analysis for [Company Name] in a concise, bullet-point format. Focus on [specific aspect] and use a professional tone."
- Record outputs under "SWOT Iteration 2 #1 - [LLM Name]" and "SWOT Iteration 2 #2 - [LLM Name]".

**Final Revision (Iteration 3 - Field-Specific Interview Context):**
- Revise the prompt to incorporate your field of study as it applies to a potential interview question a candidate might face, linking it to the company's SWOT analysis. For example, if your field is data analytics:
  - "Generate a SWOT analysis for [Company Name], a [industry] company based in [location], from the perspective of a data analytics candidate preparing for an interview. In a concise, bullet-point format, highlight how data analytics impacts the company's Strengths (e.g., leveraging data for decision-making), Weaknesses (e.g., lack of data infrastructure), Opportunities (e.g., predictive analytics for growth), and Threats (e.g., data privacy risks). Use a professional tone."
- Tailor the prompt to your specific field (e.g., IT security might focus on cybersecurity strengths or threats; marketing might focus on campaign analytics). Record outputs under "SWOT Iteration 3 #1 - [LLM Name]" and "SWOT Iteration 3 #2 - [LLM Name]".

### Step 5: Compare and Select the Best Output
**Compare Results:**
- Analyze outputs from all iterations across both LLMs in your Google Doc under the "Comparison and Analysis" heading after each iteration. Consider accuracy, completeness, readability, and relevance, especially how well Iteration 3 prepares you for an interview scenario in your field.
- Summarize which LLM and iteration produced the best result and why.

**Select the Final SWOT:**
- Choose the best SWOT analysis output (from any iteration and LLM) as your final deliverable. Refine it manually if needed (e.g., correct errors, improve formatting).

### Step 6: Prepare Deliverables
**GitHub Repository Setup:**
- Organize your repo with the following structure:

```
AI-ML-Prompt-Engineering-Lab/
├── README.md              # Lab overview and company name
├── Prompt_Revisions.docx  # Google Doc downloaded as .docx
└── swot_analysis.pdf      # Final SWOT analysis
```

**Google Doc (Prompt_Revisions.docx):**
- Structure it with the following headings:
  - LLM Selection: Brief justification of chosen LLMs.
  - SWOT Initial Prompt #1 - [LLM Name]: Raw output.
  - SWOT Initial Prompt #2 - [LLM Name]: Raw output.
  - Comparison and Analysis (Initial): Evaluation of initial outputs.
  - SWOT Iteration 1 #1 - [LLM Name]: Raw output.
  - SWOT Iteration 1 #2 - [LLM Name]: Raw output.
  - Comparison and Analysis (Iteration 1): Evaluation.
  - SWOT Iteration 2 #1 - [LLM Name]: Raw output.
  - SWOT Iteration 2 #2 - [LLM Name]: Raw output.
  - Comparison and Analysis (Iteration 2): Evaluation.
  - SWOT Iteration 3 #1 - [LLM Name]: Field-specific interview context output.
  - SWOT Iteration 3 #2 - [LLM Name]: Field-specific interview context output.
  - Comparison and Analysis (Iteration 3): Final comparison and best output selection.

**PDF Deliverable (swot_analysis.pdf):**
- Create a polished SWOT analysis based on your selected output. Use a clear format (e.g., table or sections with headings) and ensure it's professional and error-free.

### Step 7: Submission
- Push all files to your GitHub repository.
- Submit the repository URL by the due date.

## Grading

| Category | Points | Criteria |
|----------|--------|----------|
| Company Selection | 10 | Company is relevant to student's field and sourced from Indeed.com. |
| GitHub Setup | 15 | Repo is well-organized, includes all required files, and has a clear README. |
| Prompt Iterations | 30 | Required prompt versions (including field-specific interview context) documented. |
| LLM Comparison | 20 | Clear comparison of two LLMs across iterations in Google Doc. |
| SWOT Analysis Quality | 25 | Final PDF is polished, accurate, and reflects field-specific interview insights. |