from odoo import fields, models

class inheritsaleorder(models.Model):
    _inherit = "sale.order"

    proje_adi = fields.Char()
    satis_siprais_basligi = fields.Char(string="Satış Siparişi Başlığı", default="Bina Kontrol Sistemi KNX")

    kapsam = fields.Text(string="KAPSAM", default="Teklifimizde bulunan Bina Otomasyon Sistemi ürünlerinin temini ve müşteriye teslimi dahildir.Teklifimizde bulunması durumunda devreye alma hizmeti de dahil olacaktır. Devreye alma hizmeti; Şantiye hizmetleri __ adam/gün olarak belirlenmiştir. Şantiyenin hazır olmaması nedeniyle bu sürenin aşması durumunda ek ücret talep edilecektir.")

    dahil1 = fields.Text(default="Teklif kapsamında belirtilen malzemelerin tarafınıza teslimi temini")
    dahil2 = fields.Text(default="Kataloglar ve işletme/montaj talimatları")
    dahil3 = fields.Text(default="Süpervizörlük  ( max. 1 adam/gün pano firması, 1 adam/gün şantiyeniz)")
    dahil4 = fields.Text(default="Devreye Alma Hizmetleri")
    dahil5 = fields.Text(default="İşletme Personeli Eğitimi")
    dahil6 = fields.Text(default="Nakliye")

    haric1  = fields.Text(default="Kısa devre ve gerilim düşümü hesapları")
    haric2  = fields.Text(default="İstenebilecek tip testleri ")
    haric3  = fields.Text(default="Şantiye içindeki yatay ve dikey taşımalar")
    haric4  = fields.Text(default="Saha montajı")
    haric5  = fields.Text(default="Kablo Çekimi")
    haric6  = fields.Text(default="Kablo Uç Bağlantıları")
    haric7  = fields.Text(default="Mekanik Ekipman ve Bağlantıları, Mekanik Ekipman Manuel Çalıştırma Testleri")
    haric8  = fields.Text(default="Panolar ve Montajları")
    haric9  = fields.Text(default="Fan Coil Çoklama Kartları & Pencere Kontakları ")
    haric10  = fields.Text(default="Süpervizör ve Devreye Alma Personeli Konaklama Masrafları")
    haric11  = fields.Text(default="Süpervizör ve Devreye Alma Personeli İaşe Masrafları")

    opsiyon = fields.Text(default="Teklifimiz teklif tarihinden itibaren 30 GÜN süre ile geçerlidir. ")
    teslim_yeri = fields.Text(default="Teklif edilen malzemeler, müşterinin belirttiği adrese gönderilecektir.")
    teslim_suresi = fields.Text(default="Teslim süresi yazılı siparişin verilmesinden itibaren 2-4 haftadır.")
    fatura = fields.Text(default="Faturalar, KDV hariç, EURO olarak düzenlenecektir.")
    avans_ve_sartlar = fields.Text(default="Toplam tutarın %30’u avans olarak siparişin / sözleşmenin imzalanmasını müteakip 3 iş günü içerisinde, bakiye tutar ise ilgili faturanın tanzim tarihinden itibaren 30 gün içerisinde banka hesaplarına ödenecektir. Avans ve diğer ödemeler Euro olarak yapılacak olup, cari hesaplarımıza da Euro olarak kaydedilecektir. Fatura ve ödeme kayıtları, muhasebe defterlerine TCMB Döviz Satış Kuru üzerinden işlenecek ve oluşacak kur farkları, kur farkı faturası ile denkleştirilecektir. Kur farkı faturalarında KDV iç yüzde ile hesaplanır")
    garanti = fields.Text(default="Teslim edeceğimiz malzemeler, teslimat tarihimizi müteakip 24 ay süreyle tüm malzeme ve imalat hatalarına karşı garantimiz altındadır. Tarafımızdan kaynaklanmayan ve Firmamızın teklif kapsamı dışında olup tarafınızca yaptırılacak (nakliye, saha montajı, devreye alma ve işletme vb.) çalışmalar sırasında yapılabilecek hatalar ile Firmamızca özellikleri belirlenen malzemelerin, belirlenen bu özelliklere uygun kullanılmamasından dolayı ortaya çıkacak arızalar garanti kapsamımız dışındadır.")

    force_major = fields.Text(default="Tüm malzeme teslimatlarımız esnasında beynelminel force majeur halleri geçerli olacaktır.")
    vergi_mevzuat = fields.Text(default="Teklifimiz halihazırda geçerli Türk Vergi, Resim, Harç mevzuatına göre hazırlanmış olup ilgili mevzuatta vukuu muhtemel değişiklikler ile yeni ihdas halleri, teklif tarihimizden itibaren fiyatlarımıza aynı oranda dahil edilecektir. Siparişe dönüşen tekliflerde Damga vergisi müşteriye aittir.")
    mukavele = fields.Text(default="Teklifimiz hazırlanırken, indirekt maliyet unsurları ile fiyatlarımızı yükseltmemek amacı ile mukavele ve teminat mektubu masrafları nazarı dikkate alınmamış ve fiyatlarımıza dahil edilmemiştir. ")
    dolayli_zarar = fields.Text(default="MES MÜHENDİSLİK teklif edilen malzemeleri usulüne uygun kullanamamaktan doğan zararlardan, üretim ve kar kaybından, sözleşmenin taraflarca iptal edilmesinden doğabilecek diğer finansal kayıplardan ve dolaylı zararlardan sorumlu olmayacaktır. ")
    sorumluluk = fields.Text(default="İşbu Sözleşme kapsamında MES MÜHENDİSLİK sadece bu sözleşme’den doğan ve açıkça üstlendiği zararlardan dolayı veya kanun gereğince mesul tutulduğu hallerden –örneğin kasıt ve ağır ihmal gibi- sorumludur. MES MÜHENDİSLİK hiçbir halde mahrum kalınan kâr dahil (gelir kaybı, yatırım fırsatları) İŞVEREN’in dolaylı zararlarından ötürü sorumlu olmayacaktır.İş bu Sözleşmeden doğan toplam sorumluluğu hiçbir şart ve halde teklif tutarının %20’sini geçmeyecektir.")
    ihtilaflar = fields.Text(default="Taraflar arasındaki ihtilaf halinde Konya Mahkemeleri ve İcra Daireleri yetkili olacak ve Türk Kanunları uygulanacaktır. ")















