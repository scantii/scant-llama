
#Dataset Call

from torchtune.datasets import alpaca_dataset
from torchtune.models.llama3 import llama3_tokenizer


tokenizer = llama3_tokenizer("/PATH/TO/TOKENIZER")
ds = alpaca_dataset(
    tokenizer= tokenizer,
    source= 'gbharti/wealth-alpaca_lora',
    train_on_input= True,
    packed= False,
    split= "train",
)