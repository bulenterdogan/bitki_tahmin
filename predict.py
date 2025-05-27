import torch
from torchvision import transforms
from PIL import Image
from train import BitkiModel

class_names = [
    "akar_orumcegi_temelli_hastalikli_domates",
    "bakteri_temelli_domates",
    "erken_yanikli_domates",
    "gec_yanikli_domates",
    "mozaik_viruslu_domates",
    "passalora_fulva_mantarli_domates",
    "saglikli_domates",
    "sari_yaprak_kivircikliligi_viruslu_domates",
    "septoria_yaprak_lekeli_domates"
]

def predict(image_path):
    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor()
    ])

    img = Image.open(image_path).convert("RGB")
    img = transform(img).unsqueeze(0)

    model = BitkiModel(num_classes=len(class_names))
    model.load_state_dict(torch.load("model/bitki_model.pth"))
    model.eval()

    with torch.no_grad():
        output = model(img)
        probabilities = torch.softmax(output, dim=1).squeeze()
        predicted_index = torch.argmax(probabilities).item()
        confidence = float(probabilities[predicted_index].item()) * 100

    return class_names[predicted_index], confidence

