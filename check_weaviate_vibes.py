# run_benchmarks.py
from weaviate_vibe_eval.models.model import ModelNames
from weaviate_vibe_eval.benchmarks.benchmark_runner import BenchmarkRunner

# Only run with specific models
custom_benchmark = BenchmarkRunner(
    output_dir="results/custom",
    models=[
        ModelNames.CLAUDE_3_7_SONNET_20250219,
        ModelNames.CLAUDE_3_5_SONNET_20241022,
        ModelNames.CLAUDE_3_5_HAIKU_20241022,
        # ModelNames.COHERE_COMMAND_A_03_2025,
        # ModelNames.COHERE_COMMAND_R_PLUS_08_2024,
        ModelNames.GEMINI_2_5_PRO_EXP_03_25,
        ModelNames.GEMINI_2_0_FLASH_LITE,
        # ModelNames.OPENAI_GPT4O_20241120,
        # ModelNames.OPENAI_GPT4_TURBO,
        # Add any other models you want to test
    ],
    tasks=[
        "connect",
        "create_collection",
        "create_collection_more_examples",
    ],
    use_judge=True,
    verbose=True,
)

custom_results = custom_benchmark.run_benchmarks()
