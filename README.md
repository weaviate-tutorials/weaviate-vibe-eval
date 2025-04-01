# Weaviate Vibe Check

Evaluate LLMs on their ability to generate correct Weaviate code in zero-shot and few-shot scenarios.

## Supported Models

- API-based: OpenAI, Anthropic, Claude, Gemini
- Local: Ollama-based models (planned)

## Benchmark Tasks

- Connect to Weaviate Cloud
- Create and manage collections
- CRUD operations + batch import
- Querying (semantic, filters, hybrid)
- RAG patterns
- Error handling

## Setup

```bash
# Clone repository
git clone https://github.com/your-username/weaviate-vibe-eval.git
cd weaviate-vibe-eval

# Set up environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -e .

# Set environment variables
# Create a .env file with your API keys:
# ANTHROPIC_API_KEY=your_key
# COHERE_API_KEY=your_key
# GEMINI_API_KEY=your_key
# OPENAI_API_KEY=your_key
# WCD_TEST_URL=your_weaviate_cloud_url
# WCD_TEST_KEY=your_weaviate_api_key
```

## Usage

```bash
# Run all benchmarks
python check_weaviate_vibes.py

# Run specific tests
# (See documentation for additional options)
```

## Project Structure

```
weaviate_vibe_eval/       # Main package
  ├── benchmarks/         # Benchmark definitions and runner
  ├── models/             # LLM provider implementations
  └── utils/              # Shared utilities (Docker, code execution)
tests/                    # Test suite
docker/                   # Docker environment for safe code execution
results/                  # Benchmark results output
```

## License
MIT License
