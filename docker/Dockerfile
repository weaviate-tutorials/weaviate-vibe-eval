FROM python:3.9-slim

WORKDIR /code

# Install common Python packages used in benchmarks
RUN pip install --no-cache-dir \
    "weaviate-client>=4.16.7" \
    python-dotenv \
    requests \
    pytest
    # Add more packages as needed based on your benchmark requirements

# Set up a non-root user for added security
RUN useradd -m -u 1000 benchmark
# Create directory with appropriate permissions
RUN mkdir -p /code && chown -R benchmark:benchmark /code

USER benchmark

# Set Python to not buffer output for better logging
ENV PYTHONUNBUFFERED=1
