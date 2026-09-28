def get_advice(disease):
    tavsiyeler = {
        "passalora_fulva_mantarli_domates": (
            "🔸 Passalora fulva mantarı (Cladosporium fulvum) yaprakların alt yüzeyinde sarımsı-yeşil lekeler oluşturur. "
            "Zamanla lekeler kahverengiye döner ve yaprak dökümüne neden olabilir. "
            "Sera ortamlarında havalandırmayı artırın ve nem seviyesini düşürün. "
            "Enfekte yaprakları hemen uzaklaştırın; bakır bazlı fungisitler ve bakır oksiklorür ile tedavi uygulanabilir. "
            "Dayanıklı çeşitler tercih edilmeli ve ekim nöbeti uygulanmalıdır."
        ),
        "tomato_spider_mite_disease": (
            "🔸 Kırmızı örümcek (Tetranychus spp.) genellikle sıcak ve kuru ortamları sever. "
            "Yaprakların alt kısmında oluşan örümcek ağlarını fark ettiğinizde önlem alınmalı. "
            "Bitkileri sabunlu suyla püskürtün (1 L suya birkaç damla sıvı sabun), "
            "yaprak altlarını suyla yıkayın, nem seviyesini artırın. "
            "Akarisit kimyasal kullanacaksanız, önerilen dozları aşmamak ve koruyucu ekipmanla uygulamak çok önemli. "
            "Organik seçenek olarak diyatomlu toprak (diatomite) kullanımı da etkilidir."
        ),
        "tomato_bacterial_disease": (
            "🔸 Bakteriyel enfeksiyonlarda (örneğin bakteriyel yanıklık) temiz ve sertifikalı tohum kullanımı, "
            "düzgün havalandırma ve kuru sulama çok önemlidir. "
            "Enfekte yaprak veya meyveler hemen koparılarak bitkiden uzaklaştırılmalı. "
            "Gerekirse bakteri karşıtı fitosidal ürünler önerilen dozlarda uygulanabilir."
        ),
        "tomato_early_blight": (
            "🔸 Erken yanıklıkta nem yüksekliği ve gece çiylenmesi hastalığı tetikler. "
            "Dönemsel ekim nöbeti uygulayın, sulamayı sabah erken zamanlara çekin ve sadece kök bölgesine yapın. "
            "Yaprakları sulamaktan kaçının; bu, yaprak ıslak kalma süresini artırarak patojen için ideal ortam sağlar."
        ),
        "tomato_late_blight": (
            "🔸 Geç yanıklıkta (Phytophthora infestans) nemle birlikte hızlı yayılır. "
            "Havanın sirkülasyonu sağlanmalı, üstten sulama yapılmamalı ve yapraklar kuru tutulmalı. "
            "Enfekte bitkiler varsa hemen uzaklaştırılmalı. "
            "Kimyasal yaklaşımda bakır bazlı fungisitler uygulanabilir; uygulama sonrası yağmurdan sonra tekrar edilmelidir."
        ),
        "tomato_mosaic_virus": (
            "🔸 Mozaik virüsünde semptomlar sararma ve yaprak kıvrılmalarıyla kendini gösterir. "
            "Enfekte bitkiler hemen çıkarılmalı ve yakılmalıdır. "
            "Yaprak bitleri, beyaz sinek gibi virüs taşıyıcıları için düzenli ilaçlama veya fiziksel engeller kullanılmalı. "
            "Tohumlar işlenmiş olmalı, iyi bakım ve temizlik en etkili korunma yollarıdır."
        ),
        "tomato_leaf_mold_fungal": (
            "🔸 Passalora fulva (kladosporium) mantarı koyu lekeler oluşturur. "
            "Yaprak dökümleri olabilir; enfekte yapraklar uzaklaştırılmalı. "
            "Bakır oksiklorür ve bakır sülfat içeren fungisitler önerilir. "
            "Püskürtme sabah erken ya da akşam ılık saatlerde yapılmalı."
        ),
        "healthy_tomato": (
            "🔸 Bu bitki sağlıklı görünüyor! 🎉 "
            "Düzenli kontroller yapın ve zararlılara karşı önleyici budama, yaprak kontrolü, "
            "bakır bazlı periyodik ilaçlamalar ile sağlığı koruyun."
        ),
        "tomato_yellow_leaf_curl_virus": (
            "🔸 Beyaz sinek (Bemisia tabaci) taşıyıcısı olan bu virüs, yapraklarda sararma ve kıvrılmaya neden olur. "
            "Beyaz sinekle mücadele için sarı yapışkan tuzaklar kullanılmalı. "
            "Doğal düşmanlar (parazitoitler) desteklenmeli, gerekirse insektisit uygulanmalı. "
            "Enfekte bitkiler vakit kaybetmeden kaldırılmalı."
        ),
        "tomato_septoria_leaf_spot": (
            "🔸 Septoria yaprak lekesi (Septoria lycopersici) kahverengi lekeler oluşturur, genellikle alt yapraklardan başlar. "
            "Temiz tohum, ekim nöbeti ve hastalıklı yaprakların uzaklaştırılması ilk adımlardır. "
            "Kimyasal kontrol için bakır sülfat, bordo bulamacı, mancozeb gibi fungisitler erken dönemde uygulanmalıdır. "
            "İlaçlama sonrası yağmur bekleniyorsa uygulama tekrarlanmalıdır."
        )
    }
    return tavsiyeler.get(disease, "Henüz detaylı tavsiye bulunmamaktadır.")
