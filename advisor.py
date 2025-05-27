def get_advice(disease):
    tavsiyeler = {
        "akar_orumcegi_temelli_hastalikli_domates": (
            "Kırmızı örümcekler, yaprakların alt yüzeyinde beslenerek sararma ve dökülmelere neden olur. "
            "Mücadele için yaprak başına 3 ergin örümcek görüldüğünde uygun akarisitlerle ilaçlama yapılmalıdır. "
            "Ayrıca, seralarda nem kontrolü ve yaprakların alt yüzeylerinin düzenli kontrolü önemlidir."
        ),
        "bakteri_temelli_domates": (
            "Bakteriyel hastalıklar, tohumla taşınabilir ve bitkinin her yerine yayılabilir. "
            "Temiz tohum kullanımı, seraların havalandırılması ve hasta bitkilerin imhası önerilir. "
            "Kimyasal mücadele genellikle etkili değildir, bu nedenle kültürel önlemler ön planda tutulmalıdır."
        ),
        "erken_yanikli_domates": (
            "Erken yanıklık, alt yapraklarda koyu lekelerle başlar ve yaprak dökülmesine neden olur. "
            "Toprakta patojen birikimini önlemek için mahsulleri yıllık olarak değiştirin. "
            "Sulama esnasında yaprakları kuru tutmaya dikkat edin ve enfekte olmuş kısımları ayırarak yok edin."
        ),
        "gec_yanikli_domates": (
            "Geç yanıklık, yapraklarda hızla genişleyen kahverengi lekelerle kendini gösterir. "
            "Bitkiler arasında yeterli mesafe bırakarak iyi hava sirkülasyonu sağlayın. "
            "Üstten sulamadan kaçının ve enfekte olmuş bitkileri derhal çıkarıp yok edin."
        ),
        "mozaik_viruslu_domates": (
            "Mozaik virüsü, yapraklarda mozaik desenli lekelerle belirti verir. "
            "Etkilenen bitkiler çıkarılmalı ve yok edilmelidir. "
            "Dikimden önce tohumlar %1'lik potasyum permanganat çözeltisiyle dezenfekte edilmelidir."
        ),
        "passalora_fulva_mantarli_domates": (
            "Cladosporium (Passalora fulva) hastalığı, yapraklarda sarı lekeler ve alt yüzeyde kahverengi sporlarla kendini gösterir. "
            "Seralarda nem kontrolü ve iyi havalandırma sağlanmalıdır. "
            "Bakır içeren fungisitlerle ilaçlama yapılabilir."
        ),
        "saglikli_domates": (
            "Bitkiniz sağlıklı görünüyor. "
            "Düzenli sulama, dengeli gübreleme ve hastalık belirtilerine karşı düzenli kontrol ile sağlıklı kalmasını sağlayabilirsiniz."
        ),
        "sari_yaprak_kivircikliligi_viruslu_domates": (
            "Sarı yaprak kıvırcıklığı virüsü, yapraklarda sararma ve kıvrılma ile belirti verir. "
            "Beyaz sinekler bu virüsün taşıyıcısıdır. "
            "Beyaz sineklerle mücadele edilmeli ve enfekte bitkiler imha edilmelidir."
        ),
        "septoria_yaprak_lekeli_domates": (
            "Septoria yaprak lekesi, yapraklarda küçük kahverengi lekelerle başlar ve yaprak dökülmesine neden olur. "
            "Temiz tohum kullanımı, ekim nöbeti ve hasta bitkilerin imhası önerilir. "
            "Bakır içeren fungisitlerle ilaçlama yapılabilir."
        )
    }
    return tavsiyeler.get(disease, "Bu hastalık için henüz öneri bulunmamaktadır.")
