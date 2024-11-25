from diffusers import StableDiffusionPipeline
import torch


def download_model():
    model_id = "runwayml/stable-diffusion-v1-5"
    StableDiffusionPipeline.from_pretrained(
        model_id, torch_dtype=torch.float16
    ).save_pretrained("./model/")


if __name__ == "__main__":
    download_model()
