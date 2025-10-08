# AI/ML Midterm Exam Study Guide

## 1. Fundamental Concepts and Definitions

### Core Machine Learning Terms
- **Algorithm**: A step-by-step procedure for solving problems or making calculations
- **Model**: A mathematical representation of patterns learned from data
- **Features**: Individual measurable properties of the phenomena you're analyzing (the "input variables")
- **Training**: The process by which algorithms learn patterns from historical data
- **Inference**: Using a trained model to make predictions on new, previously unseen data
- **Overfitting**: When a model performs well on training data but poorly on new data (memorizing vs. learning)
- **Underfitting**: When a model fails to capture underlying patterns in data
- **Generalization**: A model's ability to perform well on new, unseen data

### AI vs. Machine Learning vs. Deep Learning
- **Artificial Intelligence**: Any technique that enables computers to mimic human behavior
- **Machine Learning**: A subset of AI that uses statistical methods to enable machines to improve with experience
- **Deep Learning**: A subset of ML that uses neural networks with multiple layers
- **Key Difference**: ML learns from data to create rules, while traditional programming uses predefined rules
- **Evolution**: AI → ML → Deep Learning (each is a subset of the previous)

## 2. Foundation Models and Large Language Models

### Foundation Models
- **Examples**: GPT, Claude, Gemini, Grok, BERT, T5
- **Training Data**: Large amounts of diverse text and data from the internet
- **GPT Definition**: Generative Pre-trained Transformer
- **Characteristics**: Pre-trained on massive datasets, can be fine-tuned for specific tasks

### LLM Capabilities and Applications
- **Primary Uses**: Text generation, question answering, natural language processing, code generation, translation
- **How They Work**: Using statistical patterns learned from training data to predict likely next words
- **Context Window**: The amount of text a model can "remember" in a single conversation

### Limitations and Challenges
- **Technical Limitations**: Limited context window, knowledge cutoff dates, computational requirements
- **Quality Issues**: Hallucinations (generating plausible but incorrect information)
- **Bias Sources**: Training data that reflects existing societal and cultural biases
- **Cost Factors**: Computational resources, API token usage, energy consumption
- **Interpretability**: Difficulty understanding why models make specific decisions

## 3. Prompt Engineering and AI Interaction

### What is Prompt Engineering?
- **Definition**: Crafting effective inputs to optimize AI model outputs and behavior
- **Importance**: Better prompts lead to more useful and accurate responses
- **Components**: Context, instructions, examples, output format specifications

### Effective Techniques
- **Clear Instructions**: Specific, unambiguous directions
- **Context Setting**: Providing relevant background information
- **Examples**: Showing desired input-output patterns
- **Step-by-Step**: Breaking complex tasks into manageable parts
- **Role Playing**: Having AI assume specific personas or expertise
- **Output Formatting**: Specifying desired structure (lists, tables, etc.)

### Advanced Concepts
- **Zero-shot Prompting**: No examples provided, just instructions
- **One-shot Prompting**: Providing one example to guide response style
- **Few-shot Prompting**: Multiple examples to establish patterns
- **Chain-of-Thought**: Encouraging step-by-step reasoning
- **Parameter Control**: Temperature, top-p, and other settings (typically not available to consumers)

## 4. Types of Machine Learning

### Supervised Learning
- **Requirements**: Labeled training data with known correct answers
- **Process**: Uses examples with "correct answers" to learn patterns
- **Data Splitting**: Training, validation, and test sets
- **Applications**: Classification and regression problems
- **Examples**: Email spam detection, medical diagnosis, price prediction

### Unsupervised Learning
- **Definition**: Finding hidden patterns in data without labeled examples
- **Applications**: Clustering, anomaly detection
- **Use Cases**: Customer segmentation, market basket analysis, data exploration
- **Challenges**: Difficult to evaluate without ground truth

### Reinforcement Learning
- **Definition**: Learning through trial and error with rewards and penalties
- **Components**: Agent, environment, actions, rewards, policy
- **Examples**: Game playing, robotics, autonomous vehicles, recommendation systems
- **Applications**: Any scenario where optimal decision-making is needed over time

## 5. Classification vs. Regression

### Classification
- **Definition**: Predicting discrete categories or classes
- **Output**: Categorical labels (spam/not spam, cat/dog/bird)
- **Types**: Binary (two classes) vs. Multi-class (multiple categories)
- **Examples**: 
  - Email spam detection
  - Image recognition
  - Sentiment analysis
  - Medical diagnosis
  - Fraud detection

### Regression
- **Definition**: Predicting continuous numerical values
- **Output**: Numbers on a continuous scale
- **Examples**:
  - House price prediction
  - Stock price forecasting
  - Temperature prediction
  - Sales revenue estimation
  - Patient vital signs

## 6. Business Applications and Implementation

### Industry Applications
- **Retail**: Product recommendations, inventory optimization, price optimization
- **Healthcare**: Medical imaging, drug discovery, patient monitoring, electronic health records
- **Finance**: Fraud detection, algorithmic trading, credit scoring, risk assessment
- **Manufacturing**: Quality control, predictive maintenance, supply chain optimization
- **Transportation**: Route optimization, autonomous vehicles, traffic management
- **Technology**: Search engines, content moderation, personalization

### Knowledge Engines and RAG
- **Scenario**: Company using internal documentation for employee assistance
- **Technology**: Knowledge engine or retrieval-augmented generation (RAG) system
- **Benefits**: Leverages existing knowledge, reduces training time, maintains accuracy
- **Components**: Document storage, search/retrieval, generation, user interface

### Implementation Considerations
- **Data Quality**: Clean, representative, sufficient data
- **Model Selection**: Choosing appropriate algorithms for the problem
- **Scalability**: Ability to handle increasing data and users
- **Maintenance**: Ongoing monitoring, updates, and retraining
- **Integration**: Connecting AI systems with existing business processes

### Business Trade-offs
- **Performance vs. Cost**: More accurate models often require more resources
- **Speed vs. Accuracy**: Faster predictions may sacrifice some precision
- **Interpretability vs. Performance**: Simpler models are easier to understand
- **Automation vs. Human Oversight**: Balancing efficiency with control

## 7. Cybersecurity and Ethical Considerations

### AI Security Risks
- **Adversarial Attacks**: Malicious inputs designed to fool AI systems
- **Data Poisoning**: Corrupting training data to influence model behavior
- **Model Theft**: Stealing or reverse-engineering AI models
- **Privacy Breaches**: Extracting sensitive information from training data
- **Automated Attacks**: Using AI to generate phishing emails, malware, or find vulnerabilities

### Ethical Challenges
- **Bias and Fairness**: Models perpetuating discrimination based on protected characteristics
- **Transparency**: "Black box" models making unexplainable decisions
- **Privacy**: Collecting and using personal data without consent
- **Accountability**: Determining responsibility when AI systems cause harm

### Responsible AI Practices
- **Diverse Teams**: Including varied perspectives in AI development
- **Bias Testing**: Evaluating models across different demographic groups
- **Explainable AI**: Developing models that can explain their decisions
- **Human Oversight**: Maintaining human control in critical decisions
- **Regular Auditing**: Continuously monitoring AI systems for problems