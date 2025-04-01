# run_benchmarks.py
from weaviate_vibe_eval.models.model import ModelNames
from weaviate_vibe_eval.benchmarks.benchmark_runner import BenchmarkRunner

# Only run with specific models
custom_benchmark = BenchmarkRunner(
    output_dir="results/custom",
    models=[
        ModelNames.CLAUDE_3_7_SONNET_20250219,
        ModelNames.GEMINI_2_5_PRO_EXP_03_25
        # Add any other models you want to test
    ],
    tasks=["zero_shot_connect"],
    use_judge=True,
    verbose=True,
)

custom_results = custom_benchmark.run_benchmarks()
