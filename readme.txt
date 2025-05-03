Torchtune Project

*MODEL* PROEJECT DIRECTORY

scantii-torch/
├── configs/
│   ├── model_config.yaml
│   ├── optimizer_config.yaml
│   ├── trainer_config.yaml
│   ├── dataloader_config.yaml
│   └── tokenizer_config.yaml
│
├── data/
│   ├── raw/         # Raw dataset files
│   ├── processed/   # Tokenized datasets
│   └── README.md    # Notes about dataset
│
├── src/
│   ├── model.py     # Custom model if needed
│   ├── dataset.py   # Custom dataset loaders/preprocessing
│   ├── train.py     # Main training script
│   ├── evaluate.py  # Evaluation/metrics script
│   ├── utils.py     # Helper functions
│   └── callbacks.py # (Optional) Custom callbacks
│
├── outputs/
│   ├── checkpoints/
│   ├── logs/
│   └── metrics/
│
├── README.md        # Explain the project, instructions
├── requirements.txt # Python dependencies
└── run.sh           # Shell script to launch training easily


Huggingface models available:

#llama
    llama3.2 3B
    llama3.2 1B

#gemma
    all

---------------------------------
Notes

custom_config.yaml
    this is the generated config file used for qlora

max_seq_len = null was causing severe slowdown at 288 its during lora
    set to 512