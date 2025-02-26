#!/bin/bash

# Fetch Railway CLI documentation
response=$(curl -s -X POST http://localhost:8000/sse \
  -H "Content-Type: application/json" \
  -d '{"tool":"fetch_railway_docs","arguments":{"url":"https://docs.railway.app/guides/cli"}}')

# Pretty print the response
echo "$response" | jq '.' 