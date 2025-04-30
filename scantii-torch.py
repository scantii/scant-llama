# checkpoint: meta-llama/Llama-3.2-1B-Instruct
# tune run lora_finetune_single_device --config custom_config.yaml 
# llama3_2/1B_qlora_single_device
# 
# tune cp <recipe> custom_config.yaml
# 
### tune run <recipe> --config <config> epochs=1
# 
# tune run lora_finetune_single_device --config llama3_2/1B_qlora_single_device epochs=1
# 
# 
# tune validate custom_config.yaml
# 

import torch
x = torch.rand(5, 3)
print(x)

y = torch.cuda.is_available()
print(f'cuda = {y}')