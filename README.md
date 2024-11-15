# Responsible AI Aspect Based Sentiment Analysis 
The goal is to explore the possibility of having AI systems that can classify the sentiments of customer feedbacks along the axis of bespoke aspects.  
For an input text we want to generate target labels `{'positive', 'neutral', 'negative'}`.
## Approaches
1. API-based strong LLM with appropriate prompt engineering e.g. COT, json output, few shot prompting, output parsing etc.
2. Open-source decoder-only or encoder-decoder SLM finetuned to produce next token 
3. Open-source encoder-only SLM finetuned with classification heads
4. Open-source SLM interpretability features aligned to the same aspect directions
## Questions
* Do we want to split original input into atomic claims?