#!/bin/bash
echo "Please enter your OpenAI key: "
read openai_key
export OPENAI_API_KEY=$openai_key
source ~/.bashrc
echo "Installing Python packages from requirements.txt..."
pip install -r requirements.txt
echo """

~/uploadfilestoopenai$ 

git clone https://huggingface.co/datasets/karan4d/machiavellian_synthetic_textbooks
python main.py machiavellian_synthetic_textbooks/machiavellian_books.json

"""  