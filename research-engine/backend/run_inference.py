import time
from vllm import LLM, SamplingParams

def run_benchmark(model_name, speculative_model=None, num_speculative_tokens=5):
    """
    Runs an inference benchmark with optional speculative decoding.
    """
    print(f"\n--- Initializing {'Speculative' if speculative_model else 'Vanilla'} Inference ---")
    
    # Initialize LLM with or without speculative decoding
    # Note: For EAGLE, we specify the speculative_model path
    llm = LLM(
        model=model_name,
        speculative_model=speculative_model,
        num_speculative_tokens=num_speculative_tokens if speculative_model else None,
        use_v2_block_manager=True if speculative_model else False, # Recommended for spec-dec
        trust_remote_code=True,
        gpu_memory_utilization=0.8
    )

    sampling_params = SamplingParams(temperature=0.0, max_tokens=256)
    
    prompt = "Explain the mechanics of speculative decoding in the context of LLM optimization."
    
    # Warmup
    llm.generate([prompt], sampling_params)
    
    # Benchmark run
    start_time = time.time()
    outputs = llm.generate([prompt], sampling_params)
    end_time = time.time()
    
    duration = end_time - start_time
    total_tokens = len(outputs[0].outputs[0].token_ids)
    tps = total_tokens / duration

    print(f"Model: {model_name}")
    if speculative_model:
        print(f"Speculative Model: {speculative_model}")
    print(f"Generated {total_tokens} tokens in {duration:.2f}s ({tps:.2f} tokens/s)")
    return tps

if __name__ == "__main__":
    # Using Qwen-2.5-7B as the target model
    TARGET_MODEL = "Qwen/Qwen2.5-7B-Instruct"
    
    # EAGLE-2 weights for Qwen-2.5-7B (Commonly hosted on HF)
    # If you don't have these downloaded, vLLM will attempt to fetch them.
    SPEC_MODEL = "ybeal/Qwen2.5-7B-Instruct-EAGLE"

    # 1. Run Vanilla
    # vanilla_tps = run_benchmark(TARGET_MODEL)
    
    # 2. Run Speculative
    # spec_tps = run_benchmark(TARGET_MODEL, speculative_model=SPEC_MODEL)
    
    # print(f"\nSpeedup: {spec_tps/vanilla_tps:.2x}")
    
    print("\n[NOTE] Execution is commented out to prevent immediate GPU allocation.")
    print("To run: Install vLLM (`pip install vllm`) and uncomment lines 47-52.")
