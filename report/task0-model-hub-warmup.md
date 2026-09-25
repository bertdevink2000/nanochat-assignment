# Task 0: Model Hub warm-up

| Model ID | Training tokens or steps | Architecture | Trainable parameters | Training data | Sources |
| --- | ---: | --- | ---: | --- | --- |
| `allenai/OLMo-1B` | 3 trillion tokens | 16 layers; hidden size 2,048; 16 attention heads | approximately 1.2B | Dolma v1.5: a mixture of web content, academic publications, code, books, and encyclopedic material | [model card](https://huggingface.co/allenai/OLMo-1B), [config.json](https://huggingface.co/allenai/OLMo-1B/blob/main/config.json), [Dolma dataset card](https://huggingface.co/datasets/allenai/dolma) |
| `HuggingFaceTB/SmolLM2-360M` | 4 trillion tokens | 32 layers; hidden size 960; 15 query-attention heads and 5 key/value heads | approximately 362M | FineWeb-Edu, DCLM, The Stack, and additional filtered datasets curated by Hugging Face | [model card](https://huggingface.co/HuggingFaceTB/SmolLM2-360M), [config.json](https://huggingface.co/HuggingFaceTB/SmolLM2-360M/blob/main/config.json), [technical report](https://arxiv.org/abs/2502.02737) |
| `Qwen/Qwen2.5-0.5B` | 18 trillion tokens reported for the Qwen2.5 series; a separate 0.5B count is not published | 24 layers; hidden size 896; grouped-query attention with 14 query heads and 2 key/value heads | 0.49B total (0.36B excluding embeddings) | A filtered, multilingual mixture emphasizing knowledge, mathematics, and code, including synthetic data; the exact source-corpus list is not disclosed | [model card](https://huggingface.co/Qwen/Qwen2.5-0.5B), [config.json](https://huggingface.co/Qwen/Qwen2.5-0.5B/blob/main/config.json), [technical report](https://arxiv.org/abs/2412.15115) |

## Source notes

- Model cards provide the training-token totals and summarized model details.
- `config.json` provides the layer count, hidden dimension, and attention-head configuration.
- Dataset cards and technical reports provide the training-data descriptions. Qwen's report describes data categories and curation methods but does not publish a complete list of source corpora.
