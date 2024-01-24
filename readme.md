# oai finetuning
intended to assist in finetuning GPT models [https://platform.openai.com/finetune]

#### why finetune?
You have two way to manipulate/enhance LLMs; that being RAG (Retrieval Augmented Generation) and finetuning. Both may reduce hallucination risk, but finetuning is better for behavior, style, tone, abilities whereas RAG is employing abilities to verify or inform models. you can also finetune to RAG more efficiently.

today's models are as bad as we allow them to be, if you finetune for a task and it performs better than gpt4 then congrats that's SOTA (state of the art).

## How to use 
### install dependencies and set api key
```
cd openai_finetuning_framework
chmod +x build.sh
./build.sh
```
### want to try on a dataset now?
```
 git clone https://huggingface.co/datasets/karan4d/machiavellian_synthetic_textbooks
 python main.py openai_finetuning_framework/machiavellian_synthetic_textbooks/machiavellian_books.jsonl
```
### upload your file
```
{intrpreter} main.py {file}
```

- file = jsonl
- interpreter = your python
### uninstall 
```
sudo rm -rf openai_finetuning_framework

```
