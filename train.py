import torch
from transformers import Trainer, TrainingArguments, AutoModelForCausalLM, AutoTokenizer

# Load pre-trained model and tokenizer
model_name = 'gpt2'
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Prepare training data
train_data = ["Your training data here..."] # Replace with your actual training data
train_encodings = tokenizer(train_data, truncation=True, padding=True)

class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, encodings):
        self.encodings = encodings

    def __getitem__(self, idx):
        return { 'input_ids': torch.tensor(self.encodings['input_ids'][idx]), 'attention_mask': torch.tensor(self.encodings['attention_mask'][idx]) }

    def __len__(self):
        return len(self.encodings['input_ids'])

# Create dataset
train_dataset = CustomDataset(train_encodings)

# Set up training arguments
training_args = TrainingArguments(
    output_dir='./results',          # output directory
    num_train_epochs=3,              # total number of training epochs
    per_device_train_batch_size=2,   # batch size per device during training
    save_steps=10_000,                # number of updates steps before saving
    save_total_limit=2,               # limit the total amount of checkpoints
)

# Create Trainer
trainer = Trainer(
    model=model,                        # the instantiated 🤗 Transformers model to be trained
    args=training_args,                 # training arguments, defined above
    train_dataset=train_dataset          # training dataset
)

# Start training
trainer.train()