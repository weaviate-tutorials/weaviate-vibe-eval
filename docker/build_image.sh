#!/bin/bash

# Define variables
IMAGE_NAME="weaviate-vibe-benchmark"
TAG="latest"

# Build the Docker image
echo "Building Docker image: ${IMAGE_NAME}:${TAG}"
docker build -t ${IMAGE_NAME}:${TAG} .

# Tag with date for versioning
DATE_TAG=$(date "+%Y%m%d")
docker tag ${IMAGE_NAME}:${TAG} ${IMAGE_NAME}:${DATE_TAG}

echo "Image built successfully:"
echo "  - ${IMAGE_NAME}:${TAG}"
echo "  - ${IMAGE_NAME}:${DATE_TAG}"
