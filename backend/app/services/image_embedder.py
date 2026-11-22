from PIL import Image
from transformers import CLIPProcessor, CLIPModel


MODEL_NAME = "openai/clip-vit-base-patch32"


class ImageEmbedder:
    def __init__(self):
        self.processor = CLIPProcessor.from_pretrained(MODEL_NAME)
        self.model = CLIPModel.from_pretrained(MODEL_NAME)

    def embed_image(self, image_path: str) -> list[float]:
        image = Image.open(image_path).convert("RGB")

        inputs = self.processor(
            images=image,
            return_tensors="pt"
        )

        output = self.model.get_image_features(**inputs)

        embedding = (
            output.pooler_output
            if hasattr(output, "pooler_output")
            else output
        )

        return embedding[0].detach().cpu().tolist()