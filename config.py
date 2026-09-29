"""
Bitki konfigürasyonları.
Yeni bitki eklemek için buraya yeni bir anahtar eklemeniz,
data/ altına veri klasörünü koymanız ve advisor.py'ye tavsiye yazmanız yeterlidir.
"""

PLANTS = {
    "domates": {
        "name": "Domates",
        "icon": "🍅",
        "data_path": "data/domates",
        "model_path": "model/domates_model.pth",
    },
    "patates": {
        "name": "Patates",
        "icon": "🥔",
        "data_path": "data/patates",
        "model_path": "model/patates_model.pth",
    },
    "biber": {
        "name": "Biber",
        "icon": "🫑",
        "data_path": "data/biber",
        "model_path": "model/biber_model.pth",
    },
}
