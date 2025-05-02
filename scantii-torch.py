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
y = torch.cuda.is_available()
z = torch.cuda.is_bf16_supported()
print(x)
print(f'cuda = {y} bf16 = {z}')

# llama3_2/1B_qlora_single_device

# tune cp llama3_2/1B_lora_single_device custom_lora_config.yaml