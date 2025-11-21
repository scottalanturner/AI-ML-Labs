# Mining Customer Gold - Text Analytics for Business Intelligence
## Individual Activity

### Overview
Transform raw customer feedback into actionable business insights using NLP tools to analyze sentiment, extract key themes, and identify improvement opportunities - all without writing a single line of code.

**AI Efficiency Principle**: If you find yourself doing something repetitively over time, ask yourself: "How can I do this faster with AI?" If you don't know the answer, ask AI: "How can I do this faster with AI?" This lab is about using AI tools effectively, so don't hesitate to use AI to streamline your workflow.

### Tools Required (All Free & Working)
- **[Google Cloud Natural Language Demo](https://cloud.google.com/natural-language#demo)**
- **[Voyant Tools](https://voyant-tools.org)** - for text visualization
- **ChatGPT or Claude** for analysis
- Google Sheets or Excel for organizing results

---

## Part 1: The Business Rescue Mission

### Scenario
You've been hired as a consultant to help a struggling local business (restaurant, service business, etc.). Your mission: use NLP to analyze their negative reviews, find patterns, and recommend improvements.

### Activity Setup
1. **Find Your Business**: 
   - Go to Google and search for a local restaurant or business in your area with poor ratings (under 3 stars)
   - Good sources: Google Reviews, Yelp, TripAdvisor
   - Choose a business with at least 15 negative reviews available (minimum of 15 reviews required)
   - Note: The business doesn't have to be a restaurant - any service business with reviews works!
   
2. **Collect Your Data**:
   - Copy a minimum of 15 negative or critical reviews (1-3 star reviews)
   - Create a document (Word, Google Doc, or PDF) titled "[Business Name] NLP Analysis"
   - Paste all reviews into your document, one review per paragraph
   - Include the business name and location at the top
   
   **💡 AI Efficiency Tip**: If you find yourself doing something repetitively (like formatting reviews), ask yourself: "How can I do this faster with AI?" You can use ChatGPT to help reformat your reviews (e.g., separating them into clean paragraphs, removing extra formatting). However, **IMPORTANT**: Make sure ChatGPT doesn't rewrite or summarize the reviews - you need the original text exactly as written. Use a prompt like: "Format these reviews so each review is on its own paragraph, but do NOT change, rewrite, or summarize any of the text - keep every word exactly as written."

### Step 1: Google's NLP Power
1. Go to [Google Cloud Natural Language Demo](https://cloud.google.com/natural-language#demo)
2. You'll see a text box - paste your review text into the box
3. Click "Analyze" (or the equivalent button if the interface has changed)
4. Analyze 5 different reviews from your collection
5. For each review, record in your document:
   - Sentiment score (number between -1 and 1) - shown in the results
   - Magnitude (strength of emotion) - shown in the results
   - Key entities detected (what specific things are mentioned) - listed in the results
   - Most emotional sentence (read through the review yourself and identify which sentence seems most emotionally charged, or look for sentences with the strongest negative language)

4. Create a simple table:
```
Review # | Sentiment Score | Magnitude | Main Complaint
---------|----------------|-----------|---------------
1        | -0.8          | 0.9       | Service
2        | -0.5          | 0.7       | Food Quality
[etc.]
```

### Step 2: Pattern Visualization
1. Go to [Voyant Tools](https://voyant-tools.org)
2. Click "Upload" or "Reveal" (the interface may vary) and paste ALL your reviews as one block of text
3. If prompted, you can paste directly into the text box or upload as a file
4. Look at the generated visualizations:
   - **Cirrus** (word cloud) - Take a screenshot of this (PNG or JPG format)
   - **Summary** - Note the most frequent words
   - **Trends** - See which words appear together
5. In your document, list:
   - Top 5 most frequent meaningful words (ignore common words like "the," "was," "is," "a," "an," "and," "or," "but," "it," "this," "that," "they," "we," "you")
   - What patterns do you see?
   - What issues come up repeatedly?
6. Embed or attach your Cirrus screenshot in your document

---

## Part 2: AI-Powered Analysis

### Deep Dive with ChatGPT/Claude
Use this structured prompt approach:

**Prompt 1: Emotion Detection**
```
Analyze these customer reviews for emotional content:
[Paste all your reviews - minimum of 15]

Tell me:
1. What are the top 3 emotions customers are feeling?
2. Which specific issues trigger the strongest negative emotions?
3. Are there any positive elements mentioned even in negative reviews?
```

**Prompt 2: Entity Extraction**
```
From these same reviews, extract:
1. All specific problems mentioned (service, quality, atmosphere, etc.)
2. Any staff members mentioned by name
3. Specific products, services, or menu items mentioned
4. Time-related complaints (wait times, hours, delays, etc.)

Organize them by frequency - what's mentioned most?
```

**Prompt 3: Business Intelligence**
```
You're a business consultant. Based on these negative reviews:
1. What are the 3 most urgent problems to fix?
2. What single change would have the biggest impact?
3. What's the root cause behind most complaints?
4. Write a 3-step action plan for the owner
```

Document each response in your analysis file. You can either:
- Copy and paste the full AI responses, OR
- Summarize the key points from each response
- Label each section clearly (Prompt 1 Response, Prompt 2 Response, Prompt 3 Response)

---

## Part 3: The Comparison Challenge

### Human vs Machine Analysis

Compare your own analysis (from Steps 1 & 2 using Google NLP and Voyant Tools) with what ChatGPT/Claude found. Create a comparison table:

| Analysis Type | What I Found Manually* | What AI Found | What AI Missed |
|--------------|----------------------|---------------|----------------|
| Main Problems | | | |
| Root Causes | | | |
| Customer Emotions | | | |
| Actionable Insights | | | |

*"What I Found Manually" = Your own observations from Google NLP analysis, Voyant Tools visualizations, and your own reading of the reviews (before using ChatGPT/Claude)

You can create this table in Word, Google Docs, or Excel - just make sure it's clear and readable.

### The Business Pitch
Write a 3-sentence elevator pitch to the business owner:
- Sentence 1: The biggest problem revealed by NLP
- Sentence 2: The impact this is having on their business
- Sentence 3: Your #1 recommendation based on the data

---

## Part 4: Real-World Application

### Your Industry Connection
Answer these questions:
1. **Business Type**: What type of business did you analyze?
2. **Pattern Discovery**: What pattern would a human likely miss that NLP caught?
3. **Scalability**: If this business had 10,000 reviews, how would NLP analysis help?
4. **Competitive Intelligence**: How could a competitor use this NLP analysis?

---

## Deliverable

Submit one complete document (Word, Google Doc, or PDF) containing all of the following sections in order:
1. **Business name and location**
2. **Your collected reviews** (minimum of 15 reviews, clearly separated)
3. **Your Google NLP analysis table** (from Step 1, showing all 5 analyzed reviews)
4. **Your Voyant Tools screenshot** (embedded or attached - make sure it's visible)
5. **Your AI prompt responses** (all 3 prompts with their responses, clearly labeled)
6. **Your comparison table (Human vs AI)** (from Part 3)
7. **Your elevator pitch to the owner** (3 sentences)
8. **Your real-world application answers** (all 4 questions from Part 4)

### The Bottom Line
You just turned real negative reviews into actionable business intelligence. This is exactly what consultants charge thousands of dollars to do. NLP tools made it possible in under an hour - imagine the value at enterprise scale with thousands of reviews daily.

### Reflection Question
What surprised you most about the patterns NLP found in the negative reviews? Would the business owner have discovered these insights without NLP tools?