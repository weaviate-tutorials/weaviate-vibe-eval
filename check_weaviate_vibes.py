# run_benchmarks.py
from weaviate_vibe_eval.models.model import ModelNames
from weaviate_vibe_eval.benchmarks.benchmark_runner import BenchmarkRunner
from weaviate_vibe_eval.benchmarks.tasks import task_registry, TaskVariant

# Only run with specific models
custom_benchmark = BenchmarkRunner(
    output_dir="results/custom",
    models=[
        # Predicates - previous best model 2025Apr
        # ModelNames.CLAUDE_3_7_SONNET_20250219,
        # New models 202508
        # ModelNames.CLAUDE_4_SONNET_20250514,
        # ModelNames.CLAUDE_4_OPUS_20250514,
        # ModelNames.GEMINI_2_5_PRO,
        # ModelNames.GEMINI_2_5_FLASH,
        # ModelNames.GEMINI_2_5_FLASH_LITE,
        # ModelNames.OPENAI_GPT5_20250807,
        # ModelNames.OPENAI_GPT5_MINI_20250807,
        ModelNames.OPENAI_GPT5_NANO_20250807,
        # ANTHROPIC MODELS
        # ModelNames.CLAUDE_3_7_SONNET_20250219,
        # ModelNames.CLAUDE_3_5_SONNET_20241022,
        # ModelNames.CLAUDE_3_5_HAIKU_20241022,
        # # COHERE MODELS
        # ModelNames.COHERE_COMMAND_A_03_2025,
        # ModelNames.COHERE_COMMAND_R_PLUS_08_2024,
        # # GEMINI/GOOGLE MODELS
        # ModelNames.GEMINI_2_5_PRO_EXP_03_25,
        # ModelNames.GEMINI_2_0_FLASH_LITE,
        # # OPENAI MODELS
        # ModelNames.OPENAI_GPT4O_20241120,
        # ModelNames.OPENAI_GPT4O_MINI_20240718,
        # ModelNames.OPENAI_GPT4_5_PREVIEW_20250227,
        # ModelNames.OPENAI_O3_MINI_20250131,
        # ModelNames.OPENAI_CHATGPT_4O_LATEST,
        # ModelNames.OPENAI_GPT4_1_20250414,
        # ModelNames.OPENAI_GPT4_1_MINI_20250414,
        # # Add any other models you want to test
    ],
    tasks=[
        # You can use base task names, which will run all variants
        # ========================================================================================================================
        # ===== These tests check the model's ability to generate working v4 Weaviate Python client code =====
        # ========================================================================================================================
        "connect",
        "create_collection",
        "batch_import",
        "basic_semantic_search",
        "complex_hybrid_query",
        # ========================================================================================================================
        # ===== The 'made_up_syntax' task is a test of non-existing syntax, to test instruction following =====
        # ========================================================================================================================
        # "made_up_syntax",
        # "slightlyl_similar_made_up_syntax",
        # ========================================================================================================================
        # # Or you can specify specific variants using task registry
        # ========================================================================================================================
        # task_registry.get_task("create_collection").get_task_id_for_variant(TaskVariant.ZERO_SHOT),
        # task_registry.get_task("create_collection").get_task_id_for_variant(TaskVariant.SIMPLE_EXAMPLE),
        # task_registry.get_task("create_collection").get_task_id_for_variant(TaskVariant.EXTENSIVE_EXAMPLES),
    ],
    use_judge=False,
    verbose=False,
)

custom_results = custom_benchmark.run_benchmarks()
