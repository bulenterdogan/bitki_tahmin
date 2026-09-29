import torch
import torch.nn as nn
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader, Subset
import matplotlib.pyplot as plt
import os
import random
import copy
import argparse
from config import PLANTS


torch.manual_seed(42)
random.seed(42)

def create_model(num_classes):
    """ResNet18 tabanlı transfer learning modeli oluşturur."""
    model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)

    # İlk katmanları dondur (önceden öğrenilmiş özellikler korunur)
    for param in model.parameters():
        param.requires_grad = False

    # Son katmanları aç (fine-tuning için)
    for param in model.layer4.parameters():
        param.requires_grad = True

    # Son sınıflandırma katmanını değiştir
    model.fc = nn.Sequential(
        nn.Dropout(0.3),
        nn.Linear(model.fc.in_features, num_classes)
    )

    return model

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bitki hastalığı modeli eğitimi")
    parser.add_argument(
        "--plant",
        required=True,
        choices=list(PLANTS.keys()),
        help=f"Eğitilecek bitki: {', '.join(PLANTS.keys())}"
    )
    parser.add_argument("--epochs", type=int, default=15, help="Epoch sayısı (varsayılan: 15)")
    args = parser.parse_args()

    plant_config = PLANTS[args.plant]
    data_path = plant_config["data_path"]
    model_path = plant_config["model_path"]
    epochs = args.epochs

    print(f"\n🌱 {plant_config['icon']} {plant_config['name']} modeli eğitiliyor...")
    print(f"   Veri yolu: {data_path}")
    print(f"   Model yolu: {model_path}\n")

    if not os.path.isdir(data_path) or len(os.listdir(data_path)) == 0:
        print(f"❌ Veri klasörü boş veya bulunamadı: {data_path}")
        print(f"   Lütfen önce PlantVillage'dan {plant_config['name']} verilerini indirip bu klasöre yerleştirin.")
        exit(1)

    # Eğitim için güçlü veri artırma
    transform_train = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomVerticalFlip(p=0.2),
        transforms.RandomRotation(15),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
        transforms.RandomAffine(degrees=0, translate=(0.1, 0.1)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    # Doğrulama için sadece resize ve normalize
    transform_val = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    # Veri setlerini yükle (aynı klasör, farklı transform)
    dataset_train = datasets.ImageFolder(data_path, transform=transform_train)
    dataset_val = datasets.ImageFolder(data_path, transform=transform_val)
    num_classes = len(dataset_train.classes)
    print(f"📋 Sınıflar ({num_classes}): {dataset_train.classes}")

    # Aynı indekslerle train/val ayır
    total = len(dataset_train)
    indices = list(range(total))
    random.shuffle(indices)
    train_size = int(0.85 * total)

    train_data = Subset(dataset_train, indices[:train_size])
    val_data = Subset(dataset_val, indices[train_size:])

    print(f"📊 Eğitim: {len(train_data)} | Doğrulama: {len(val_data)} görsel")

    train_loader = DataLoader(train_data, batch_size=32, shuffle=True)
    val_loader = DataLoader(val_data, batch_size=32, shuffle=False)

    model = create_model(num_classes)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.AdamW(filter(lambda p: p.requires_grad, model.parameters()), lr=0.001)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', patience=3, factor=0.5)

    train_accuracies = []
    val_accuracies = []
    train_losses = []
    val_losses = []

    # Early stopping ayarları
    best_val_acc = 0.0
    best_model_state = None
    patience = 5
    patience_counter = 0

    print(f"\n🚀 Eğitim başlıyor ({epochs} epoch, early stopping patience={patience})\n")

    for epoch in range(epochs):
        model.train()
        total, correct, train_loss = 0, 0, 0.0

        for images, labels in train_loader:
            outputs = model(images)
            loss = criterion(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            train_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            correct += (predicted == labels).sum().item()
            total += labels.size(0)

        train_acc = 100 * correct / total
        avg_train_loss = train_loss / len(train_loader)
        train_accuracies.append(train_acc)
        train_losses.append(avg_train_loss)

        model.eval()
        val_correct, val_total, val_loss = 0, 0, 0.0
        with torch.no_grad():
            for images, labels in val_loader:
                outputs = model(images)
                loss = criterion(outputs, labels)
                val_loss += loss.item()
                _, predicted = torch.max(outputs, 1)
                val_correct += (predicted == labels).sum().item()
                val_total += labels.size(0)

        val_acc = 100 * val_correct / val_total
        avg_val_loss = val_loss / len(val_loader)
        val_accuracies.append(val_acc)
        val_losses.append(avg_val_loss)

        scheduler.step(avg_val_loss)

        current_lr = optimizer.param_groups[0]['lr']
        print(f"Epoch {epoch+1:02}/{epochs}: "
              f"Train Acc: {train_acc:.2f}% | Val Acc: {val_acc:.2f}% | "
              f"Train Loss: {avg_train_loss:.4f} | Val Loss: {avg_val_loss:.4f} | "
              f"LR: {current_lr:.6f}")

        # Early stopping kontrolü
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            best_model_state = copy.deepcopy(model.state_dict())
            patience_counter = 0
            print(f"  ✅ En iyi model güncellendi! (Val Acc: {best_val_acc:.2f}%)")
        else:
            patience_counter += 1
            if patience_counter >= patience:
                print(f"\n⏹️ Early stopping! {patience} epoch boyunca iyileşme olmadı.")
                break

    # En iyi modeli sınıf isimleriyle birlikte kaydet
    os.makedirs("model", exist_ok=True)
    torch.save({
        "model_state_dict": best_model_state,
        "class_names": dataset_train.classes,
    }, model_path)
    print(f"\n✅ {plant_config['name']} modeli kaydedildi: {model_path} (Val Acc: {best_val_acc:.2f}%)")

    # Grafik çiz
    plt.figure(figsize=(10, 5))
    plt.suptitle(f"{plant_config['icon']} {plant_config['name']} Eğitim Sonuçları", fontsize=14)

    plt.subplot(1, 2, 1)
    plt.plot(train_accuracies, label='Train Acc')
    plt.plot(val_accuracies, label='Val Acc')
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy (%)")
    plt.title("Doğruluk Oranı")
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(train_losses, label='Train Loss')
    plt.plot(val_losses, label='Val Loss')
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Kayıp Değeri")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plot_name = f"accuracy_{args.plant}.png"
    plt.savefig(plot_name)
    plt.show()
    print(f"📊 Grafik kaydedildi: {plot_name}")
