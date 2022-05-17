# Conversational-Agent

**Problem Description**

Given datasets and pretrained models, the project aims to explore the differences in performance between different models, different decoding techniques, different evaluation metrics, and by fine-tuning the pre-trained models. In addition to the MultiWOZ2.2 dataset provided, we supplemented our fine-tuning dialogue with The Schema Guided Dialogue DataSet

To carry out this problem, we used two different datasets:

MultiWOZ Data

Multi-Domain Wizard-of-Oz dataset (MultiWOZ), a fully-labeled collection of human-human written conversations spanning over multiple domains and topics. At a size of 10k dialogues, it is at least one order of magnitude larger than all previous annotated task-oriented corpora. There are 3,406 single-domain dialogues that include booking if the domain allows for that and 7,032 multi-domain dialogues consisting of at least 2 up to 5 domains. 


The Schema Guided Dialogue DataSet

The Schema-Guided Dialogue (SGD) dataset consists of over 20k annotated multi-domain, task-oriented conversations between a human and a virtual assistant. These conversations involve interactions with services and APIs spanning 20 domains, such as banks, events, media, calendar, travel, and weather. For most of these domains, the dataset contains multiple different APIs, many of which have overlapping functionalities but different interfaces, which reflects common real-world scenarios


**Changes made to codebase:**

-> Fine-tuning script modification

-> File directory structure

-> Automated evaluation loop

-> New decoding method (Top-K) and new metrics (BERTScore and ROUGE)


**The various Approaches Implemented:**

_Different Models_

-> The first approach was to compare pre-trained GPT vs. GPT2 models’ zero-shot performance as well as the fine tune performance.


_Varying Decoding Techniques_

-> Greedy Decoding
Selection of word with highest probability

-> Top-K
Redistribution of probability mass over K most likely next words. 
For this experiment : k = 5.

-> Top-P
Shortlisting smallest number of top tokens with sum of probabilities exceeding p.
For this experiment : p = 0.90.

-> Beam Search
Expanding the highest probability beam by keeping the number of beams constant in each timestep.
For this experiment : # of beams = 5.

_Varying Evaluation Metric_

-> BLEU Score
Evaluation of quality of machine translated text with natural language text.

-> BERTScore
Leverages the pre-trained contextual embeddings from BERT and matches words in candidate and reference texts by cosine similarity. 

-> ROUGE Score
Evaluation of automatic summarization and machine translation software

_Supplementing Fine-Tuning Data_

-> Original Goal: 
Fine-tune on large general purpose conversational dataset
Fine-tune again on the MultiWoz dataset

-> Completed Goal:
Combined SGD training dataset with the MultiWoz training dataset
Fine-tuned on combined (supplemented) dataset






