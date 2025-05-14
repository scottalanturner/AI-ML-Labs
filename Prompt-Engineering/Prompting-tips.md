
# Prompting Tips

|  | Theme                    | Tip                                                   | Explanation                                                                 |
|------------|--------------------------|-------------------------------------------------------|-----------------------------------------------------------------------------|
| 1          | Evaluation               | Test LLM understanding with examples                  | Input training examples to check if the LLM produces expected outputs; refine or break tasks if poor. |
| 2          | Versioning               | Version prompts like code using git                   | Track performance changes with tools like git, anticipating MLflow or Weights & Biases for experiments. |
| 3          | Optimization             | Use Chain-of-Thought (COT) for step-by-step reasoning | Improves accuracy on complex tasks but increases latency and cost; use judiciously in production. |
| 4          | Optimization             | Generate multiple outputs for self-consistency        | Use majority vote or let LLM pick best response to improve reliability, especially for ambiguous tasks. |
| 6          | Compatibility            | Unit-test prompts for backward/forward compatibility  | Ensure prompts work with model updates by testing with evaluation examples, address centralized knowledge gaps. |
| 7          | Basics                   | Define good and bad responses for evaluation          | Set clear guidelines, combining automation and manual review to assess prompt effectiveness. |
| 8          | Approach                 | Start with prompting, then add data, escalate to complex methods if needed | Focus on solving the problem, not chasing latest tech; non-AI solutions may suffice. |
| 9          | Production Readiness     | Implement input/output guardrails                     | Prevent model jailbreaking and ensure output quality, crucial for enterprise reliability. |
| 11         | Cost and Latency Management | Optimize prompts for cost and latency                 | Break large prompts into smaller ones to balance performance and efficiency in production. |
| 12         | Contextual Enhancement   | Leverage RAG for relevant context                     | Use Retrieval-Augmented Generation to improve accuracy with domain-specific data, ideal for enterprises. |
| 14         | Continuous Improvement   | Monitor and gather feedback for iterative prompt enhancement | Implement mechanisms to track performance and user feedback, ensuring prompts evolve with needs. |
| 15         | Problem-Centric Design   | Prioritize problem-solving over technology            | Focus on business outcomes; sometimes simpler prompting or non-AI solutions are more effective. |
