# Openai Finetuning
intended to assist in finetuning GPT models [https://platform.openai.com/finetune]

#### why finetune? :(assume everything i say to be wrong) 
You have two way to manipulate/enhance LLMs; that being RAG and finetuning. Both may reduce hallucination risk, but finetuning is better for behavior, style, tone, abilities whereas RAG is employing abilities to verify or inform models. 

## How to use 
### install dependencies and set api key
```
chmod +x build.sh
./build.sh
```
### want to try on a dataset now?
```
 git clone https://huggingface.co/datasets/karan4d/machiavellian_synthetic_textbooks
```
### upload your file
```
{intrpreter} main.py {file}
```

- file = jsonl
- interpreter = your python
