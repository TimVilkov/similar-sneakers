import os

from transformers import CLIPProcessor, CLIPModel


def download_clip(model_path):
    """Download a Hugging Face model and tokenizer to the specified directory"""
    # Check if the directory already exists
    if not os.path.exists(model_path):      
        print('model isn\'t downloaded.Start downloading!!!!')
        processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
        model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")

        processor.save_pretrained(model_path)
        model.save_pretrained(model_path)
    return True