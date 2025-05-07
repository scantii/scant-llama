# checkpoint: meta-llama/Llama-3.2-1B-Instruct
# 
# llama3_2/1B_lora_single_device
# llama3_2/1B_qlora_single_device
# 
### tune cp <recipe> custom_type_config.yaml
# 
### tune validate <config>
#
### tune run <recipe> --config <config>
# 
#
## tune cp llama3_2/1B_lora_single_device configs/custom_lora_config.yaml
## tune cp llama3_2/1B_qlora_single_device configs/custom_qlora_config.yaml
#
# tune validate dev/configs/custom_lora_config.yaml
# tune validate dev/configs/custom_qlora_config.yaml
#
# tune run lora_finetune_single_device --config dev/configs/customloraconfig.yaml
# tune run lora_finetune_single_device --config dev/configs/customqloraconfig.yaml
# 
# 
## tune cp eleuther_evaluation configs/custom_eval_config.yaml
# tune validate dev/configs/custom_eval_config.yaml
#
# tune run eleuther_eval --config dev/configs/custom_eval_config.yaml
#
#
## tune cp generation configs/custom_generation_config.yaml
# 
# tune run generate --config dev/configs/custom_generation_config.yaml prompt.user="Tell me a joke. "
#
# nvidia-smi dmon -f gpu0.csv --format csv -o T

import torch
x = torch.rand(5, 3)
y = torch.cuda.is_available()
z = torch.cuda.is_bf16_supported()
print(x)
print(f'cuda = {y} bf16 = {z}')
