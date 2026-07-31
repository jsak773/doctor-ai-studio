#!/bin/bash
echo "==================================================="
echo " Deploying Doctor AI Studio to Google Cloud Live"
echo "==================================================="
echo ""

echo "Step 1: Initializing Google Cloud Project..."
gcloud config set project doctor-ai-studio 2>/dev/null || true

echo "Step 2: Deploying to Google App Engine Live..."
gcloud app deploy app.yaml --quiet

echo ""
echo "==================================================="
echo " Successfully Deployed to Google Cloud!"
echo " Access live URL using: gcloud app browse"
echo "==================================================="
