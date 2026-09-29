def get_advice(disease):
    tavsiyeler = {
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        #                DOMATES 🍅
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        "healthy_tomato": (
            "🎉 Harika haber! Bu domates yaprağı sağlıklı görünüyor.\n\n"
            "🛡️ Sağlığı Korumak İçin Öneriler:\n"
            "• Haftada en az 1-2 kez yaprakları kontrol edin; erken teşhis en önemli savunmadır.\n"
            "• Alt yaprakları budayarak hava sirkülasyonunu artırın.\n"
            "• Damla sulama tercih edin; yaprakları ıslatmaktan kaçının.\n"
            "• 2-3 haftada bir bakır bazlı koruyucu ilaçlama yapın.\n"
            "• Bitkiler arası mesafeyi en az 50 cm tutun.\n"
            "• Toprak pH'ını 6.0-6.8 arasında tutmaya özen gösterin."
        ),

        "passalora_fulva_mantarli_domates": (
            "⚠️ Hastalık: Passalora Fulva Mantarı (Cladosporium fulvum)\n\n"
            "🔍 Belirtiler:\n"
            "• Yaprakların üst yüzeyinde soluk sarı-yeşil lekeler oluşur.\n"
            "• Alt yüzeyde kadifemsi, zeytin yeşili veya kahverengi mantar sporları görülür.\n"
            "• İlerleyen dönemde yapraklar kıvrılır, sararır ve dökülür.\n"
            "• Ağır enfeksiyonlarda meyve verimi ciddi şekilde düşer.\n\n"
            "💊 Tedavi:\n"
            "• Enfekte yaprakları hemen koparıp bitkiden uzağa atın (kompost yapmayın).\n"
            "• Bakır oksiklorür (%50 WP) — 50 g / 10 L su ile 7-10 gün arayla püskürtün.\n"
            "• Alternatif olarak azoxystrobin veya difenoconazole içeren fungisitler kullanılabilir.\n\n"
            "🛡️ Önleme:\n"
            "• Sera ortamında nem oranını %85'in altında tutun ve havalandırma sağlayın.\n"
            "• Bitkiler arası mesafeyi artırarak hava sirkülasyonunu iyileştirin.\n"
            "• Dayanıklı domates çeşitleri (Cf genli çeşitler) tercih edin.\n"
            "• 2-3 yıllık ekim nöbeti uygulayın."
        ),

        "tomato_bacterial_disease": (
            "⚠️ Hastalık: Bakteriyel Benek / Bakteriyel Yanıklık\n\n"
            "🔍 Belirtiler:\n"
            "• Yapraklarda küçük, koyu kahverengi veya siyah su emilmiş lekeler oluşur.\n"
            "• Lekeler etrafında sarımsı bir hale (halo) görülebilir.\n"
            "• Gövde ve meyve saplarında da koyu lekeler oluşabilir.\n"
            "• Meyveler üzerinde kabarcıklı, mantar benzeri lekeler gelişebilir.\n\n"
            "💊 Tedavi:\n"
            "• Bakır hidroksit veya bakır sülfat bazlı preparatlar erken dönemde etkilidir.\n"
            "• Streptomisin sülfat (%15) — 1 g / 1 L su ile 5-7 gün arayla uygulayın.\n"
            "• Enfekte yaprak, dal ve meyveleri hemen koparıp uzaklaştırın.\n\n"
            "🛡️ Önleme:\n"
            "• Temiz ve sertifikalı tohum kullanın; tohumu ekmeden önce sıcak su ile dezenfekte edin (50°C, 25 dk).\n"
            "• Üstten sulama yapmayın, damla sulama kullanın.\n"
            "• Islak yapraklara dokunmayın; hastalık mekanik olarak yayılır.\n"
            "• 3 yıllık ekim nöbeti uygulayın; aynı yere ard arda domates dikmeyin."
        ),

        "tomato_early_blight": (
            "⚠️ Hastalık: Erken Yanıklık (Alternaria solani)\n\n"
            "🔍 Belirtiler:\n"
            "• Yapraklarda iç içe geçmiş halkalar şeklinde kahverengi lekeler (hedef tahtası görünümü) oluşur.\n"
            "• Alt yapraklardan başlayarak yukarıya doğru ilerler.\n"
            "• Yapraklar sararır ve erken dökülür; meyve güneş yanığına açık kalır.\n"
            "• Gövdede de koyu, çökmüş lekeler oluşabilir.\n\n"
            "💊 Tedavi:\n"
            "• Mancozeb (%80 WP) — 25-30 g / 10 L su ile 7-10 gün arayla püskürtün.\n"
            "• Bordo bulamacı (%1) ile önleyici uygulama yapın.\n"
            "• Chlorothalonil veya azoxystrobin içeren fungisitler alternatif olarak kullanılabilir.\n"
            "• Hastalıklı yaprakları hemen uzaklaştırın.\n\n"
            "🛡️ Önleme:\n"
            "• Sulamayı sabah erken saatlerde, sadece kök bölgesine yapın.\n"
            "• Alt yaprakları budayarak hava dolaşımını artırın.\n"
            "• Ekim nöbeti uygulayın; domates ailesinden olmayan bitkilerle dönüşümlü ekin.\n"
            "• Malçlama yaparak topraktan sıçrama yoluyla bulaşmayı önleyin."
        ),

        "tomato_late_blight": (
            "🚨 Hastalık: Geç Yanıklık (Phytophthora infestans)\n\n"
            "🔍 Belirtiler:\n"
            "• Yapraklarda büyük, gri-yeşil, su emilmiş lekeler oluşur.\n"
            "• Nemli havalarda yaprak altlarında beyaz pamuksu mantar sporları görülür.\n"
            "• Gövdede koyu kahverengi-siyah lekeler oluşur.\n"
            "• Meyvelerde sert, kahverengi çürüme başlar.\n"
            "• Çok hızlı yayılır; birkaç gün içinde tüm tarlayı sarabilir!\n\n"
            "💊 Tedavi (ACİL):\n"
            "• Metalaxyl + Mancozeb (Ridomil Gold MZ) — 25 g / 10 L su ile hemen uygulayın.\n"
            "• Bakır bazlı fungisitler (bordo bulamacı %1) ile 5-7 gün arayla tekrarlayın.\n"
            "• Yağmurdan sonra uygulamayı mutlaka tekrarlayın.\n"
            "• Enfekte bitkileri hemen sökün ve yakın (kompost yapmayın!).\n\n"
            "🛡️ Önleme:\n"
            "• Serin (15-22°C) ve nemli havalarda özellikle dikkatli olun.\n"
            "• Üstten sulama kesinlikle yapmayın.\n"
            "• Havalandırmayı artırın, bitkiler arası mesafeyi geniş tutun.\n"
            "• Dayanıklı çeşitler tercih edin.\n"
            "• Patatesten uzak ekin — aynı patojen her iki bitkiyi de etkiler."
        ),

        "tomato_leaf_mold_fungal": (
            "⚠️ Hastalık: Yaprak Küfü Mantarı (Fulvia fulva)\n\n"
            "🔍 Belirtiler:\n"
            "• Yaprakların üst yüzeyinde açık yeşil veya sarımsı lekeler oluşur.\n"
            "• Alt yüzeyde zeytin yeşili ile kahverengi arasında kadifemsi küf tabakası oluşur.\n"
            "• Enfekte yapraklar kıvrılır, sararır ve sonunda dökülür.\n"
            "• Yüksek nem ortamlarında (sera) çok hızlı yayılır.\n\n"
            "💊 Tedavi:\n"
            "• Bakır oksiklorür (%50 WP) — 50 g / 10 L su ile 7-10 gün arayla uygulayın.\n"
            "• Bakır sülfat (bordo bulamacı %1) alternatif olarak kullanılabilir.\n"
            "• Difenoconazole veya myclobutanil içeren fungisitler de etkilidir.\n"
            "• Püskürtmeleri sabah erken veya akşam saatlerinde yapın.\n\n"
            "🛡️ Önleme:\n"
            "• Sera ortamında nemi %80'in altında tutun.\n"
            "• Havalandırma pencerelerini açık tutun veya fan kullanın.\n"
            "• Bitkiler arası mesafeyi artırın.\n"
            "• Dayanıklı çeşitler tercih edin.\n"
            "• Hastalıklı bitki kalıntılarını sezon sonunda temizleyin."
        ),

        "tomato_mosaic_virus": (
            "🚨 Hastalık: Domates Mozaik Virüsü (ToMV)\n\n"
            "🔍 Belirtiler:\n"
            "• Yapraklarda açık ve koyu yeşil mozaik deseni oluşur.\n"
            "• Yapraklar deformasyona uğrar, kıvrılır veya buruşur.\n"
            "• Bitkinin büyümesi yavaşlar, bodurlaşma görülebilir.\n"
            "• Meyvelerde iç kahverengileşme ve olgunlaşmama görülebilir.\n\n"
            "💊 Tedavi:\n"
            "• ⚠️ Virüs hastalıklarının kimyasal tedavisi YOKTUR.\n"
            "• Enfekte bitkiler derhal sökülmeli ve yakılmalıdır (kompost yapmayın).\n"
            "• Enfekte bitkiye dokunan aletler %10 çamaşır suyu çözeltisiyle dezenfekte edilmeli.\n"
            "• Tütün kullanıcıları bitkiye dokunmadan önce ellerini yıkamalıdır.\n\n"
            "🛡️ Önleme:\n"
            "• Virüse dayanıklı domates çeşitleri (Tm-2, Tm-2² genli) seçin.\n"
            "• Sertifikalı ve virüssüz tohum kullanın.\n"
            "• Vektör böceklerle (yaprak biti, beyaz sinek) mücadele edin.\n"
            "• Sarı yapışkan tuzaklar kullanın.\n"
            "• Aletlerinizi her bitkiden sonra dezenfekte edin."
        ),

        "tomato_septoria_leaf_spot": (
            "⚠️ Hastalık: Septoria Yaprak Lekesi (Septoria lycopersici)\n\n"
            "🔍 Belirtiler:\n"
            "• Yapraklarda çok sayıda küçük (2-3 mm), yuvarlak, koyu kenarları olan gri-beyaz lekeler oluşur.\n"
            "• Lekelerin ortasında küçük siyah noktalar (piknidyumlar) görülebilir.\n"
            "• Alt yapraklardan başlar, yukarı doğru ilerler.\n"
            "• Ağır enfeksiyonlarda yapraklar tamamen sararıp dökülür.\n\n"
            "💊 Tedavi:\n"
            "• Mancozeb (%80 WP) — 25-30 g / 10 L su ile 7 gün arayla uygulayın.\n"
            "• Bordo bulamacı (%1) veya bakır sülfat ile önleyici uygulama yapın.\n"
            "• Chlorothalonil bazlı fungisitler alternatif olarak kullanılabilir.\n"
            "• İlaçlama sonrası yağmur yağarsa uygulamayı tekrarlayın.\n\n"
            "🛡️ Önleme:\n"
            "• Enfekte yaprakları hemen koparıp uzaklaştırın.\n"
            "• Malçlama yaparak topraktan sıçrama bulaşmasını engelleyin.\n"
            "• Ekim nöbeti uygulayın (en az 2 yıl).\n"
            "• Alt yaprakları budayarak hava sirkülasyonunu artırın.\n"
            "• Sulamayı kök bölgesine ve sabah erken saatlerde yapın."
        ),

        "tomato_spider_mite_disease": (
            "⚠️ Hastalık: Kırmızı Örümcek Akarı (Tetranychus urticae)\n\n"
            "🔍 Belirtiler:\n"
            "• Yapraklarda küçük, sarı-beyaz benekler (noktacıklar) oluşur.\n"
            "• Yaprakların alt yüzeyinde ince örümcek ağları görülür.\n"
            "• İlerleyen dönemde yapraklar bronzlaşır, kurur ve dökülür.\n"
            "• Sıcak ve kuru havada (30°C+) çok hızlı çoğalır.\n\n"
            "💊 Tedavi:\n"
            "• İlk aşamada yaprakları güçlü su jeti ile yıkayın (alt yüzeyler dahil).\n"
            "• Sabunlu su (1 L suya 5-10 ml sıvı sabun) ile yaprak altlarını püskürtün.\n"
            "• Abamectin veya spiromesifen içeren akarisitler kullanılabilir.\n"
            "• Organik seçenek: Neem yağı (azadirachtin) — 3-5 ml / 1 L su.\n"
            "• Diyatomlu toprak (diatomite) organik alternatif olarak etkilidir.\n\n"
            "🛡️ Önleme:\n"
            "• Ortam nemini artırın (akarlar kuruyu sever).\n"
            "• Doğal düşmanları (Phytoseiulus persimilis gibi yırtıcı akarlar) destekleyin.\n"
            "• Bitkiler arası yabani ot kontrolü yapın.\n"
            "• Sera ortamında sıcaklığı 30°C altında tutmaya çalışın.\n"
            "• Aşırı azotlu gübrelemeden kaçının (akar çoğalmasını artırır)."
        ),

        "tomato_yellow_leaf_curl_virus": (
            "🚨 Hastalık: Domates Sarı Yaprak Kıvırcıklık Virüsü (TYLCV)\n\n"
            "🔍 Belirtiler:\n"
            "• Yapraklar yukarıya doğru kıvrılır ve kenarları sarıya döner.\n"
            "• Bitkide ciddi bodurlaşma görülür.\n"
            "• Çiçek dökümü artar, meyve verimi çok düşer.\n"
            "• Beyaz sinek (Bemisia tabaci) ile taşınır.\n\n"
            "💊 Tedavi:\n"
            "• ⚠️ Virüs hastalıklarının kimyasal tedavisi YOKTUR.\n"
            "• Enfekte bitkileri hemen sökün ve yakın.\n"
            "• Beyaz sinek kontrolü birincil hedeftir:\n"
            "  — Imidacloprid veya thiamethoxam içeren insektisitler uygulanabilir.\n"
            "  — Sarı yapışkan tuzaklar asın (bitki başına 1-2 tuzak).\n\n"
            "🛡️ Önleme:\n"
            "• TYLCV'ye dayanıklı domates çeşitleri (Ty genli) seçin.\n"
            "• Sera girişlerinde böcek tülü (50 mesh) kullanın.\n"
            "• Sarı yapışkan tuzaklar ile beyaz sinek popülasyonunu izleyin.\n"
            "• Doğal düşmanları (Encarsia formosa gibi parazitoidler) destekleyin.\n"
            "• Enfekte bitki kalıntılarını sezon sonunda mutlaka temizleyin."
        ),

        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        #                PATATES 🥔
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        "Potato___healthy": (
            "🎉 Harika haber! Bu patates yaprağı sağlıklı görünüyor.\n\n"
            "🛡️ Sağlığı Korumak İçin Öneriler:\n"
            "• Düzenli yaprak kontrolü yapın; erken teşhis en iyi savunmadır.\n"
            "• Ekim nöbeti uygulayın — aynı tarlaya arka arkaya patates ekmeyin (en az 3 yıl).\n"
            "• Sertifikalı ve hastalıksız tohumluk patates kullanın.\n"
            "• Dengeli gübreleme yapın; aşırı azot yaprak hastalıklarına zemin hazırlar.\n"
            "• Damla sulama tercih edin; yaprakları ıslatmaktan kaçının.\n"
            "• Hasat sırasında yumruları çizmemeye dikkat edin; çizikler depo çürüğüne yol açar."
        ),

        "Potato___Early_blight": (
            "⚠️ Hastalık: Patates Erken Yanıklığı (Alternaria solani)\n\n"
            "🔍 Belirtiler:\n"
            "• Yapraklarda iç içe halkalar şeklinde kahverengi lekeler (hedef tahtası deseni) oluşur.\n"
            "• Alt (yaşlı) yapraklardan başlayarak yukarı doğru ilerler.\n"
            "• Lekelerin etrafında sarı bir hale oluşabilir.\n"
            "• Gövde ve yumrularda da koyu, çökmüş lekeler görülebilir.\n"
            "• Stres altındaki (kuraklık, beslenme eksikliği) bitkiler daha duyarlıdır.\n\n"
            "💊 Tedavi:\n"
            "• Mancozeb (%80 WP) — 25-30 g / 10 L su ile 7-10 gün arayla uygulayın.\n"
            "• Bordo bulamacı (%1) erken dönemde koruyucu olarak etkilidir.\n"
            "• Azoxystrobin veya difenoconazole içeren fungisitler alternatif olarak kullanılabilir.\n"
            "• Hastalıklı yaprakları hemen koparıp bitkiden uzağa atın.\n\n"
            "🛡️ Önleme:\n"
            "• Ekim nöbeti uygulayın; domates ve patlıcan ile rotasyondan kaçının (aynı patojen).\n"
            "• Sertifikalı tohumluk patates kullanın.\n"
            "• Dengeli gübreleme yapın; özellikle potasyum eksikliğinden kaçının.\n"
            "• Malçlama yaparak topraktan sıçrama bulaşmasını önleyin.\n"
            "• Alt yaprakları budayarak hava sirkülasyonunu artırın."
        ),

        "Potato___Late_blight": (
            "🚨 Hastalık: Patates Geç Yanıklığı (Phytophthora infestans)\n\n"
            "🔍 Belirtiler:\n"
            "• Yapraklarda büyük, düzensiz, su emilmiş gri-yeşil lekeler oluşur.\n"
            "• Nemli havalarda yaprak altında beyaz pamuksu mantar sporları görülür.\n"
            "• Gövdede koyu kahverengi-siyah lekeler oluşur.\n"
            "• Yumrularda kahverengi-kızıl renkte sert çürüme başlar.\n"
            "• Çok hızlı yayılır — birkaç gün içinde tüm tarlayı sarabilir!\n\n"
            "💊 Tedavi (ACİL):\n"
            "• Metalaxyl + Mancozeb (Ridomil Gold MZ) — 25 g / 10 L su ile hemen uygulayın.\n"
            "• Bakır bazlı fungisitler (bordo bulamacı %1) ile 5-7 gün arayla tekrarlayın.\n"
            "• Cymoxanil + Mancozeb alternatif olarak kullanılabilir.\n"
            "• Yağmurdan sonra uygulamayı mutlaka tekrarlayın.\n"
            "• Enfekte bitkileri hemen sökün ve yakın (kompost yapmayın!).\n\n"
            "🛡️ Önleme:\n"
            "• Serin (15-22°C) ve nemli havalarda özellikle dikkatli olun.\n"
            "• Üstten sulama kesinlikle yapmayın.\n"
            "• Dayanıklı patates çeşitleri tercih edin.\n"
            "• Domateslerden uzak ekin — aynı patojen her iki bitkiyi de etkiler.\n"
            "• Hasattan 2-3 hafta önce sapları biçerek yumruların enfeksiyondan korunmasını sağlayın.\n"
            "• Hasat edilen yumruları serin, kuru ve karanlık ortamda depolayın."
        ),

        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        #                BİBER 🫑
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        "Pepper__bell___healthy": (
            "🎉 Harika haber! Bu biber yaprağı sağlıklı görünüyor.\n\n"
            "🛡️ Sağlığı Korumak İçin Öneriler:\n"
            "• Düzenli yaprak kontrolü yapın; hastalık ve zararlıları erken tespit edin.\n"
            "• Damla sulama kullanın; yaprakları ıslatmaktan kaçının.\n"
            "• Dengeli gübreleme yapın; aşırı azot yaprak hastalıklarına zemin hazırlar.\n"
            "• Bitkiler arası mesafeyi 40-50 cm tutarak hava sirkülasyonunu sağlayın.\n"
            "• Ekim nöbeti uygulayın — aynı tarlaya arka arkaya biber ekmeyin.\n"
            "• Zararlılara karşı periyodik sarı yapışkan tuzak kontrolü yapın."
        ),

        "Pepper__bell___Bacterial_spot": (
            "⚠️ Hastalık: Biber Bakteriyel Leke (Xanthomonas euvesicatoria)\n\n"
            "🔍 Belirtiler:\n"
            "• Yapraklarda küçük, koyu yeşil veya kahverengi, su emilmiş lekeler oluşur.\n"
            "• Lekeler zamanla büyür, kahverengileşir ve ortası kuruyarak delinebilir.\n"
            "• Yaprak dökümü hızlanır, bitki zayıflar.\n"
            "• Meyvelerde kabarcıklı, kahverengi kabuklu lekeler oluşur.\n"
            "• Gövde ve yaprak saplarında da koyu lekeler görülebilir.\n"
            "• Sıcak (25-30°C) ve nemli havalarda hızla yayılır.\n\n"
            "💊 Tedavi:\n"
            "• Bakır hidroksit (%77 WP) — 30-40 g / 10 L su ile 7 gün arayla uygulayın.\n"
            "• Bordo bulamacı (%1) ile önleyici uygulama yapın.\n"
            "• Bakır + mancozeb kombinasyonu daha etkili olabilir.\n"
            "• Streptomisin sülfat (%15) — 1 g / 1 L su ile ciddi durumlarda uygulanabilir.\n"
            "• Enfekte yaprak ve meyveleri hemen koparıp uzaklaştırın.\n\n"
            "🛡️ Önleme:\n"
            "• Temiz ve sertifikalı tohum kullanın.\n"
            "• Tohumu ekmeden önce sıcak su ile dezenfekte edin (50°C, 25 dk).\n"
            "• Üstten sulama yapmayın, damla sulama tercih edin.\n"
            "• Islak yapraklara dokunmayın; hastalık mekanik olarak yayılır.\n"
            "• Ekim nöbeti uygulayın (en az 2-3 yıl).\n"
            "• Dayanıklı biber çeşitleri tercih edin.\n"
            "• Sezon sonunda bitki kalıntılarını mutlaka temizleyin."
        ),
    }
    return tavsiyeler.get(disease, "Henüz bu hastalık için detaylı tavsiye bulunmamaktadır.")
