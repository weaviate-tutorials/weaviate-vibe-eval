# Weaviate Benchmark Docker Image

This document describes how to build, update, and use the Docker image for benchmarking.

## Building the Image

To build the prebuilt Docker image:

```bash
cd weaviate_vibe_eval/docker
chmod +x build_image.sh
./build_image.sh
```

This creates two tags:
- `weaviate-vibe-benchmark:latest` - Always points to the most recent build
- `weaviate-vibe-benchmark:YYYYMMDD` - Date-stamped version for reproducibility

## Updating the Image

1. Modify the `Dockerfile` to add/change packages or configuration
2. Re-run the build script
3. Update your tests to ensure the new image works as expected

## Common Package List

The prebuilt image includes these frequently used packages:
- weaviate-client
- python-dotenv
- requests
- pytest
