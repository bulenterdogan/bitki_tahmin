import React, { useState } from 'react';
import { 
  StyleSheet, Text, View, TouchableOpacity, Image, 
  ScrollView, ActivityIndicator, Alert, SafeAreaView, Platform 
} from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import axios from 'axios';

// BİLGİSAYARININ IP ADRESİNİ BURAYA YAZ (Örn: 192.168.1.100)
// Localhost (127.0.0.1) telefonda çalışmaz çünkü telefon kendi içindeki 127.0.0.1'e bakar!
const API_URL = 'http://192.168.1.44:5000/api/predict';

const PLANTS = [
  { key: 'domates', name: 'Domates', icon: '🍅' },
  { key: 'patates', name: 'Patates', icon: '🥔' },
  { key: 'biber', name: 'Biber', icon: '🫑' }
];

export default function App() {
  const [selectedPlant, setSelectedPlant] = useState(null);
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  // Galeriden seç
  const pickImage = async () => {
    if (!selectedPlant) {
      Alert.alert('Hata', 'Lütfen önce bir bitki seçin!');
      return;
    }

    const { status } = await ImagePicker.requestMediaLibraryPermissionsAsync();
    if (status !== 'granted') {
      Alert.alert('İzin Gerekli', 'Galerinize erişim izni vermelisiniz.');
      return;
    }

    let result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      allowsEditing: true,
      aspect: [1, 1],
      quality: 0.8,
    });

    if (!result.canceled) {
      setImage(result.assets[0]);
      setResult(null);
    }
  };

  // Kamerayı aç
  const takePhoto = async () => {
    if (!selectedPlant) {
      Alert.alert('Hata', 'Lütfen önce bir bitki seçin!');
      return;
    }

    const { status } = await ImagePicker.requestCameraPermissionsAsync();
    if (status !== 'granted') {
      Alert.alert('İzin Gerekli', 'Kamera erişim izni vermelisiniz.');
      return;
    }

    let result = await ImagePicker.launchCameraAsync({
      allowsEditing: true,
      aspect: [1, 1],
      quality: 0.8,
    });

    if (!result.canceled) {
      setImage(result.assets[0]);
      setResult(null);
    }
  };

  // API'ye gönder
  const analyzeImage = async () => {
    if (!image || !selectedPlant) return;
    
    if (API_URL.includes('192.168.1.X')) {
      Alert.alert('IP Ayarı Gerekli', "Lütfen App.js dosyasındaki API_URL kısmına bilgisayarınızın yerel IP adresini (IPv4) yazın.");
      return;
    }

    setLoading(true);
    setResult(null);

    const formData = new FormData();
    formData.append('plant', selectedPlant);
    
    // Resmi formData'ya uygun formata çevir
    const localUri = image.uri;
    const filename = localUri.split('/').pop();
    const match = /\.(\w+)$/.exec(filename);
    const type = match ? `image/${match[1]}` : `image`;

    formData.append('image', { uri: localUri, name: filename, type });

    try {
      const response = await axios.post(API_URL, formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
        timeout: 10000,
      });

      setResult(response.data);
    } catch (error) {
      console.error(error);
      Alert.alert('Bağlantı Hatası', 'Sunucuya bağlanılamadı. Bilgisayardaki app.py çalışıyor mu ve IP adresi doğru mu?');
    } finally {
      setLoading(false);
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContainer}>
        
        <Text style={styles.title}>🌿 VizyPlant</Text>
        <Text style={styles.subtitle}>Yapay Zeka ile Bitki Sağlığı Analizi</Text>

        {/* Bitki Seçim Kartları */}
        <View style={styles.plantSelector}>
          {PLANTS.map((plant) => (
            <TouchableOpacity 
              key={plant.key}
              style={[
                styles.plantCard, 
                selectedPlant === plant.key && styles.plantCardSelected
              ]}
              onPress={() => setSelectedPlant(plant.key)}
            >
              <Text style={styles.plantIcon}>{plant.icon}</Text>
              <Text style={[
                styles.plantName,
                selectedPlant === plant.key && styles.plantNameSelected
              ]}>{plant.name}</Text>
            </TouchableOpacity>
          ))}
        </View>

        {/* Uyarı Kutusu */}
        <View style={styles.warningBox}>
          <Text style={styles.warningTitle}>⚠️ Önemli Uyarı</Text>
          <Text style={styles.warningText}>
            Yukarıdan analiz etmek istediğiniz bitkiyi doğru seçtiğinizden emin olun.
          </Text>
        </View>

        {/* Seçilen Resmi Göster */}
        {image && (
          <Image source={{ uri: image.uri }} style={styles.imagePreview} />
        )}

        {/* Butonlar */}
        <View style={styles.buttonContainer}>
          <TouchableOpacity style={[styles.button, styles.btnGallery]} onPress={pickImage}>
            <Text style={styles.buttonText}>📁 Galeriden Seç</Text>
          </TouchableOpacity>
          
          <TouchableOpacity style={[styles.button, styles.btnCamera]} onPress={takePhoto}>
            <Text style={styles.buttonText}>📷 Kamerayı Aç</Text>
          </TouchableOpacity>
        </View>

        {image && (
          <TouchableOpacity 
            style={[styles.button, styles.btnAnalyze]} 
            onPress={analyzeImage}
            disabled={loading}
          >
            {loading ? (
              <ActivityIndicator color="#fff" />
            ) : (
              <Text style={styles.buttonText}>🔍 Analiz Et</Text>
            )}
          </TouchableOpacity>
        )}

        {/* Sonuç Kartı */}
        {result && (
          <View style={styles.resultCard}>
            <Text style={styles.resultHeader}>🌿 Bitki: {result.bitki_adi}</Text>
            <Text style={styles.resultHeader}>🔬 Tahmin: {result.tahmin}</Text>
            <Text style={styles.resultConfidence}>📈 Güven Skoru: %{result.guven_skoru.toFixed(2)}</Text>
            <View style={styles.divider} />
            <Text style={styles.resultAdvice}>{result.tavsiye}</Text>
          </View>
        )}

      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f7fa',
    paddingTop: Platform.OS === 'android' ? 40 : 0,
  },
  scrollContainer: {
    padding: 20,
    alignItems: 'center',
    paddingBottom: 50,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#2e7d32',
    marginTop: 10,
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
    marginBottom: 25,
  },
  plantSelector: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    width: '100%',
    marginBottom: 15,
  },
  plantCard: {
    backgroundColor: '#fff',
    padding: 15,
    borderRadius: 15,
    alignItems: 'center',
    width: '30%',
    borderWidth: 2,
    borderColor: '#eee',
    elevation: 3,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowRadius: 5,
  },
  plantCardSelected: {
    borderColor: '#4caf50',
    backgroundColor: '#e8f5e9',
  },
  plantIcon: {
    fontSize: 32,
    marginBottom: 5,
  },
  plantName: {
    fontWeight: '600',
    color: '#333',
  },
  plantNameSelected: {
    color: '#2e7d32',
  },
  warningBox: {
    backgroundColor: '#fff3cd',
    borderLeftWidth: 5,
    borderLeftColor: '#f5c6cb',
    padding: 12,
    borderRadius: 8,
    width: '100%',
    marginBottom: 20,
  },
  warningTitle: {
    fontWeight: 'bold',
    color: '#856404',
    marginBottom: 4,
  },
  warningText: {
    color: '#856404',
    fontSize: 13,
  },
  imagePreview: {
    width: 250,
    height: 250,
    borderRadius: 15,
    marginBottom: 20,
  },
  buttonContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    width: '100%',
    marginBottom: 15,
  },
  button: {
    padding: 15,
    borderRadius: 10,
    alignItems: 'center',
    justifyContent: 'center',
  },
  btnGallery: {
    backgroundColor: '#1976d2',
    width: '48%',
  },
  btnCamera: {
    backgroundColor: '#ef6c00',
    width: '48%',
  },
  btnAnalyze: {
    backgroundColor: '#388e3c',
    width: '100%',
    padding: 18,
    marginBottom: 20,
  },
  buttonText: {
    color: '#fff',
    fontWeight: 'bold',
    fontSize: 16,
  },
  resultCard: {
    backgroundColor: '#fff',
    padding: 20,
    borderRadius: 15,
    width: '100%',
    borderWidth: 1,
    borderColor: '#c8e6c9',
    elevation: 4,
  },
  resultHeader: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#1b5e20',
    marginBottom: 5,
  },
  resultConfidence: {
    fontSize: 15,
    color: '#555',
    marginBottom: 10,
  },
  divider: {
    height: 1,
    backgroundColor: '#e0e0e0',
    marginVertical: 10,
  },
  resultAdvice: {
    fontSize: 15,
    color: '#333',
    lineHeight: 22,
  },
});
