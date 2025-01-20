# Preamble context
PREAMBLE = (
    "Woolworths (also referred to as Woolies in a short and colloquial form) is one of the largest supermarket chains in Australia and New Zealand. "
    "Woolworths primarily sells common household grocery-related products ranging from fruit, vegetables, meat, dairy products, condiments, pet food and more.\n" 
    "Woolworths has a loyalty (or rewards) program that gives its members extra benefits including targeted personalised offers. "
    "Customers need to sign up to join the program, at which point they'll be given a rewards card. "
    "In order to enjoy more benefits from this program, members need to continue to scan their rewards / loyalty cards when making purchases. "
    "Typical scan of rewards card would register transaction details such as the item purchased, purchase date time and purchase price against their unique personal identifier. "
    "Customer would also get 1 reward point for each dollar they spend in the transactions that are scanned. "
    "The main value proposition comes in the form of points where every 2000 points is equivalent to $10 off the customer's next shop. "
    "From time to time, members can also enjoy other benefits such as additional points for redeeming targeted offers on a certain range of products and free samples of products."
)

# Multi-headings
MULTIHEAD_INSTRUCTION = """\
You are good at reading, understanding and rephrasing customer survey data without changing the underlying content. \
You will be presented with lines of comments from a rewards customer. The comment will always start with the a survey heading followed by the comment body will respond to. \
Your task is to combine the survey heading and the comment body into more coherent and natural sounding sentences. \
You MUST avoid adding extra emotions to the original comment or infer anything not in the comment. \
You will fix any spelling or punctuation mistakes. You take the perspective of the customer. \
You will output in the format of a JSON list with:
- Each newline of the input as a separate list element
- An empty string '' if there are no, "no" or "None" comments for that survey heading. Do NOT put extra words.

### Comment
{comment}
"""

# Single-heading
SINGLEHEAD_INSTRUCTION = """\
You are good at reading, understanding and rephrasing customer survey data without changing the underlying meaning. \
You will be presented with a comment from a rewards customer in response to a survey heading". \
Your task is to combine the survey heading and the comment body into a more coherent and natural sounding passage. \
You MUST avoid adding extra emotions to the original comment or infer anything not mentioned in the comment. \
You will fix any spelling or punctuation mistakes. You take the perspective of the customer. 

### Survey Heading
{survey_heading}

### Comment
{comment}
"""

# Fixing Instruction on the concantenated comments from multiple survey headings
CONCAT_INSTRUCTION = """\
You are good at reading chunks of texts and making sense of the overall theme. \
You will be presented with a comment from a rewards customer. The comment can be disjoint at various locations and possibly repeated in certain ways. \
Your task is to make sense of it and respond with a fluent version of the comment, which sounds more like natural language sentences. \
You MUST avoid adding extra emotions to the original comment or infer anything not in the comment. You take the perspective of the customer. 

### Comment
{comment}
"""

# Generic ABSA Template
ABSA_TEMPLATE = """\
You are an expert at judging sentiments of specific aspects within comments.
For the comment below, please give the polarity of the speaker's sentiment in terms of the aspect as either "positive", "negative" or "neutral".
Please output "neutral" if the aspect is irrelevant to the comment or you are unsure about the sentiment.

<comment>
{comment}
</comment>\

<aspect>
{aspect}
</aspect>

Repeat the comment and aspect first then think step-by-step through the comment to give the reasoning before arriving at an answer for the sentiment. 
You must output in JSON format like the example below: 
{{
    "comment": "The movie has a great ending."
    "aspect": "Transparency"
    "reason": "The customer does not mention anything about that aspect."
    "sentiment": "neutral"
}}
"""