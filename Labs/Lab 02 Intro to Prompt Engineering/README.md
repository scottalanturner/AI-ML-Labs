# Prompt Engineering Lab: From Novice to Navigator

**60-Minute Hands-On Practice Session**

## Pre-Lab Setup (5 minutes)

### Choose Your AI Assistant

Select ONE of these free AI platforms to use for today's lab:

- ChatGPT (chat.openai.com) - No account needed for basic access
- Claude (claude.ai) - Free tier with email signup
- Google Gemini (gemini.google.com) - Free with Google account
- Microsoft Copilot (copilot.microsoft.com) - Free with Microsoft account
- Perplexity AI (perplexity.ai) - No account needed for basic access

**Quick Setup Tips:**

- If a platform requires an account, use your email to sign up (takes 2-3 minutes)
- Choose whichever platform loads fastest for you
- Stick with the same platform throughout the lab for consistency

### Your Industry Focus

Before starting, decide on an industry context for your exercises:

- Choose either your current industry OR an industry you aspire to work in
- Examples: healthcare, finance, education, retail, technology, non-profit, entertainment, hospitality, etc.
- You'll apply all exercises to real scenarios from this industry

**Remember:** If you get stuck at any point, ask your AI model for help! For example: "Can you help me improve this prompt?" or "What's a good example of chain-of-thought prompting?"

## Part 1: Foundation Building (15 minutes)

### Understanding the Basics: From Vague to Valuable

#### Exercise 1.1: The Clarity Test (5 minutes)

Start with this intentionally vague prompt:

> "Help me with work"

1. Enter this exact prompt and observe the response
2. Now, transform it using the Essential Components structure from class:
   - **Context:** Who you are and what your role is
   - **Instructions:** Specific task you need help with
   - **Output Format:** How you want the answer structured
   - **Rules:** Any constraints or requirements

Your improved prompt should look something like:

> "I'm a [your role] in the [your industry] industry.  
> I need to [specific task].  
> Please provide [output format].  
> Keep it [constraints/rules]."

**Reflection moment:** Notice how the AI's response changed? The difference between confusion and clarity is in the details you provide.

#### Exercise 1.2: Zero-Shot vs One-Shot Learning (5 minutes)

**Scenario:** You need to write a professional email in your industry.

**First, try zero-shot (no examples):**

> "Write a professional email to a client explaining a project delay in [your industry]"

**Now try one-shot (with an example):**

> "Here's an example of the tone I want:  
> 'Dear Sarah, I wanted to personally reach out regarding your account. We value your partnership and want to ensure you have the best experience possible.'  
> Now write a professional email to a client explaining a project delay in [your industry] using a similar warm, personal tone"

**Real-world insight:** One-shot prompting is like showing someone a sample before asking them to create something similar. In the workplace, this technique helps maintain brand voice and consistency.

#### Exercise 1.3: The Power of Role-Playing (5 minutes)

Compare these two approaches:

**Generic prompt:**

> "Explain [a complex concept from your industry] simply"

**Role-based prompt:**

> "You are an experienced [industry] professional explaining [same concept] to a summer intern on their first day. Use relatable analogies and avoid jargon."

Try it yourself with a concept from your chosen industry. Notice how assigning the AI a specific role changes its communication style?

**Story from the field:** A Richmond marketing firm increased their content quality by 40% simply by starting every prompt with "You are our senior creative director who has won multiple industry awards..."

## Part 2: Techniques That Transform (20 minutes)

### Moving from Basic to Brilliant

#### Exercise 2.1: Chain-of-Thought (CoT) Magic (7 minutes)

Chain-of-Thought prompting is like asking someone to "show their work" in math class. It produces better results because the AI thinks through the problem step-by-step.

**Scenario:** Budget planning in your industry

**Without CoT:**

> "How should I allocate a $10,000 quarterly budget in [your industry]?"

**With CoT:**

> "I have a $10,000 quarterly budget for [your department] in [your industry].  
> Think through this step-by-step:  
> 1. First, identify the top 3-4 priorities for this type of budget  
> 2. Then, consider typical percentage allocations in this industry  
> 3. Account for any seasonal factors this quarter  
> 4. Finally, provide a specific breakdown with justifications  
> Let's think through this systematically:"

**Real-world application:** A local startup used CoT prompting to plan their product launch and discovered three risk factors they hadn't considered. The step-by-step thinking revealed gaps in their original plan.

#### Exercise 2.2: Few-Shot Learning for Consistency (7 minutes)

**Task:** Create social media posts for your industry

**Few-shot prompt structure:**

> "Create a LinkedIn post about [industry topic]. Here are examples of the style I want:  
> 
> Example 1: 'Thrilled to announce our Q3 results! 📈 Three key wins: increased efficiency, happier clients, and a stronger team. What's driving your success this quarter?'  
> 
> Example 2: 'Leadership lesson from today: Sometimes the best decision is to pause and listen. Had a breakthrough with our team by simply asking, 'What do you think?' 🤔 When did listening last lead to your breakthrough?'  
> 
> Now create a post about [your specific topic] following this style:"

**Pro tip:** Few-shot prompting is perfect for maintaining brand voice across different content creators. Many companies now include 2-3 examples in their prompt templates.

#### Exercise 2.3: The Format Formula (6 minutes)

Clear format instructions prevent AI hallucination and ensure usable outputs.

**Try this comparison:**

**Vague format:**

> "Give me ideas for improving customer service in [your industry]"

**Specific format:**

> "Provide exactly 5 customer service improvements for [your industry].  
> Format each as:  
> - Challenge: [specific problem]  
> - Solution: [actionable fix]  
> - Impact: [measurable outcome]  
> - Timeline: [implementation timeframe]"

**Industry insight:** A consulting firm reduced revision requests by 60% by adding specific format requirements to all their prompts. Clear structure = less back-and-forth.

## Part 3: Advanced Applications (15 minutes)

### From Learning to Launching

#### Exercise 3.1: The Iteration Method (5 minutes)

Start with a basic prompt, then refine it based on the output. This mimics real-world prompt engineering.

**Round 1:**

> "Write a proposal for [project in your industry]"

**After seeing the output, Round 2:**

> "Write a 2-page proposal for [same project]. Include budget estimates, timeline, and risk factors. Use bullet points for easy scanning. Target audience is senior management who have 2 minutes to read this."

**Key learning:** Prompt engineering is iterative. Your first prompt is rarely your best prompt.

#### Exercise 3.2: The Constraint Challenge (5 minutes)

Constraints often improve creativity and relevance.

Create a training scenario for your industry with these constraints:

> "Design a 15-minute training exercise for new employees in [your industry].  
> Constraints:  
> - No technology required  
> - Can be done remotely  
> - Costs nothing  
> - Teaches [specific skill]  
> - Includes a measurable outcome"

**Real example:** A Richmond restaurant chain used constraint-based prompting to develop their entire COVID-era training program, saving $50,000 in consulting fees.

#### Exercise 3.3: The Combination Technique (5 minutes)

Combine multiple techniques for complex tasks:

> "You are a [role] in [industry].  
> I need help with [specific challenge].  
> Think step-by-step:  
> 1. What are the key issues?  
> 2. What solutions have worked elsewhere?  
> 3. What's unique about our situation?  
> Provide your response as:  
> - Executive Summary (2 sentences)  
> - Top 3 Recommendations (bullet points)  
> - Next Steps (numbered list)  
> Keep the total response under 300 words and focus on actionable items only."

## Part 4: Reflection & Real-World Application (5 minutes)

### Making It Stick

#### Personal Reflection Questions (answer these for yourself):

1. Which technique surprised you the most with its effectiveness?
2. How could you use CoT prompting in your daily work tomorrow?
3. What's one repetitive task in your job that could benefit from a well-crafted prompt template?

#### Create Your Power Prompt

Before you leave, create ONE prompt template you'll actually use this week:

> "You are [role].  
> I need [specific outcome].  
> Context: [relevant background].  
> Please [specific action verb] and provide [format].  
> Focus on [key priority].  
> Avoid [what to exclude]."

Save this template - you've just created your first piece of prompt engineering IP!

## Lab Wrap-Up (5 minutes)

### Key Takeaways to Remember

- ✓ **Clarity beats cleverness** - Specific prompts get specific results
- ✓ **Examples accelerate excellence** - One-shot and few-shot learning dramatically improve outputs
- ✓ **Structure saves time** - Clear format requirements reduce revision cycles
- ✓ **Thinking shows value** - CoT prompting reveals insights you might miss
- ✓ **Iteration is innovation** - Your second prompt is usually better than your first

### Your Next Steps

1. **This Week:** Use your power prompt template at least 3 times
2. **This Month:** Build a prompt library for your 5 most common tasks
3. **This Quarter:** Share a prompt engineering win with your team

### Final Thought

Remember what we learned: Prompt engineering is "part art, part science." The science you've learned today—the techniques, structures, and methods. The art comes from practice, experimentation, and understanding your unique context.

Every prompt you write is an opportunity to communicate more clearly—not just with AI, but with colleagues, clients, and yourself about what you really need.

### Bonus Challenge

Tomorrow, take your worst-performing regular prompt (something you use that gives mediocre results) and apply three techniques from today's lab. Document the before and after. You might just revolutionize a piece of your workflow.

**Remember:** The AI is your collaborative partner. If you're stuck, confused, or want to explore further, just ask it! "How can I make this prompt better?" is itself a great prompt.
