import torch
import os

patates_path = "model/patates_model.pth"
if os.path.exists(patates_path):
    checkpoint = torch.load(patates_path, map_location="cpu", weights_only=False)
    # Revert to exact original names and order as created by ImageFolder initially
    checkpoint["class_names"] = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']
    torch.save(checkpoint, patates_path)
    print("Patates modeli eski haline getirildi.")

biber_path = "model/biber_model.pth"
if os.path.exists(biber_path):
    checkpoint = torch.load(biber_path, map_location="cpu", weights_only=False)
    # Revert to exact original names
    checkpoint["class_names"] = ['Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy']
    torch.save(checkpoint, biber_path)
    print("Biber modeli eski haline getirildi.")
