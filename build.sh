#!/bin/bash
echo "Please enter your OpenAPI key: "
read openapi_key
export OPENAI_API_KEY=$api_key

echo "Installing Python packages from requirements.txt..."
pip install -r requirements.txt

