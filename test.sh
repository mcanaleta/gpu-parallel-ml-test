#! /bin/bash

curl -X POST http://localhost:8080/generate \
    -H "Content-Type: application/json" \
    -d '{"prompt": "A futuristic cityscape at sunset"}'
