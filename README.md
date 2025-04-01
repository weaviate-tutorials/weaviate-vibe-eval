# Weaviate Code Generation Benchmark

Evaluate LLMs on their ability to generate correct Weaviate code in zero-shot and few-shot scenarios.

## Supported Models

- API-based: OpenAI, Anthropic, Google, Cohere
- Local: Ollama-based models

## Tasks

- Connect to Weaviate
- Create a collection
- CRUD operations + batch import
- Querying (semantic, filters, hybrid)
- RAG queries
- Error handling

## Usage

```bash
# Install
pip install -r requirements.txt

# Run benchmarks
python run_benchmark.py --all
python run_benchmark.py --models <comma-separated-model-names>
python run_benchmark.py --zero-shot-only
python run_benchmark.py --few-shot-only
```

## Project Structure

```
benchmarks/     # Tasks, examples, and expected outputs
models/         # API and local model interfaces
evaluation/     # Evaluation code and metrics
config.py       # Configuration settings
run_benchmark.py # Main script
results/        # Benchmark results
```

## License
[MIT License](LICENSE)
