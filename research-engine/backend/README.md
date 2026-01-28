# Speculative Decoding Benchmark: Qwen-2.5-7B with EAGLE

This project implements a high-performance inference pipeline using speculative decoding (EAGLE-2) for the Qwen-2.5 model series.

## Setup

1. **Environment**: Recommended Python 3.10+
2. **Key Dependencies**:
   - `vllm`: The primary engine for high-throughput inference.
   - `torch`, `transformers`: Standard backend.

## Execution
Run `python run_inference.py` to benchmark the speedup.
