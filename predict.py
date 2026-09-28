import torch
from torchvision import transforms
from PIL import Image
from train import create_model

class_names = [
    "healthy_tomato",
    "passalora_fulva_mantarli_domates",
    "tomato_bacterial_disease",
    "tomato_early_blight",
    "tomato_late_blight",
    "tomato_leaf_mold_fungal",
    "tomato_mosaic_virus",
    "tomato_septoria_leaf_spot",
    "tomato_spider_mite_disease"
]

# Model uygulama başlatılırken bir kere yüklenir
model = create_model(num_classes=len(class_names))
model.load_state_dict(torch.load("model/plant_model.pth", map_location="cpu", weights_only=True))
model.eval()

def predict(image_path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(image)
        probabilities = torch.softmax(output, dim=1).squeeze()
        predicted_index = torch.argmax(probabilities).item()
        confidence = float(probabilities[predicted_index].item()) * 100

    return class_names[predicted_index], confidence
