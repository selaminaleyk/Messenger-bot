import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# BotFather'dan aldığın token
TOKEN = "9109429978:AAGk7dxcZQ1u9vM5JqY3Z_uQgsvLVLrW-_I"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}"

# Senin istediğin tam ve güncel metin
WELCOME_MESSAGE = (
    "🔥 81 İLDEN TÜRKİYE'NİN DÖRT BİR YANINDAN KIZLARIN VE GENCIN OLDUĞU EN BÜYÜK SOHBET GRUBUMUZ AKTİF! 🔥\n\n"
    "🚨 DİKKAT: Gruba katılım tamamen ücretsizdir ancak yoğunluk ve güvenlik nedeniyle herkesin aşağıdaki ana gruba katılması ZORUNLUDUR!\n\n"
    "👉 ANA SOHBET GRUBUMUZ: @trarayisda \n"
    "(Katılmayanların bot erişimi otomatik olarak engellenir!)\n\n"
    "🔞 Aradığınız 100 Tane Ünlü İfşa, Özel Arşivler ve VIP Medya Dosyaları Sadece Bu Botun İçinde!\n\n"
    "🎁 Arşivi ve linkleri anında açmak için:\n"
    "1️⃣ Önce yukarıdaki @trarayisda grubuna katılın.\n"
    "2️⃣ Aşağıdaki \"ARŞİVİ AÇ / BAĞLANTIYI GÖSTER\" butonuna basın!"
)

# İstediğin buton
KEYBOARD = {
    "inline_keyboard": [
        [{"text": "🔥 ARŞİVİ AÇ / BAĞLANTIYI GÖSTER", "url": "https://t.me/trarayisda"}]
    ]
}

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = request.get_json()
    
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")
        
        # Kullanıcı /start komutu gönderdiğinde bu metin patlar
        if text.startswith("/start"):
            payload = {
                "chat_id": chat_id,
                "text": WELCOME_MESSAGE,
                "reply_markup": KEYBOARD,
                "parse_mode": "Markdown"
            }
            requests.post(f"{TELEGRAM_API_URL}/sendMessage", json=payload)
            
    return jsonify({"status": "ok"}), 200

@app.route("/", methods=["GET"])
def index():
    return "Bot aktif ve 7/24 çalışıyor!", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
  
