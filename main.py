import os
import json
import re
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from pyrogram.types import InputMediaPhoto

API_ID = 1234567890 #api id
API_HASH = "xxxxx" #api hash 
BOT_TOKEN = "xxxx" #bot token

ADMIN_ID = 1234567890 #admin user id

app = Client("TelegramWearBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

user_data = {} 
user_state = {}

@app.on_message(filters.command("start"))
def start(client, message):
    username = message.from_user.username

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Geyimlər 👕", callback_data="geyimler")],
        [InlineKeyboardButton("Telefon Caseləri 📱", callback_data="kabrolar")],
        [InlineKeyboardButton("Ödəniş 💳", callback_data="ödəniş"),
         InlineKeyboardButton("Çatdırılma 🛵", callback_data="çatdırılma")],
        [InlineKeyboardButton("Suallar ❓", callback_data="suallar"),
         InlineKeyboardButton("Bizi izləyin 🔍", callback_data="hesablar")],
         [InlineKeyboardButton("Sifariş üçün müraciət 💌", callback_data="sifariş_müraciət")]
    ])
    message.reply_text(
        f"Salam @{username}! 👋 Öz geyiminlə fərq yarat\n"
        f"Aşağıdakı seçimlər arasından bir əməliyyat başlatmaq üçün düymələri basın\n",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("geriyə"))
def geriye(client, callback_query):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Geyimlər 👕", callback_data="geyimler")],
        [InlineKeyboardButton("Telefon Caseləri 📱", callback_data="kabrolar")],
        [InlineKeyboardButton("Ödəniş 💳", callback_data="ödəniş"),
         InlineKeyboardButton("Çatdırılma 🛵", callback_data="çatdırılma")],
        [InlineKeyboardButton("Suallar ❓", callback_data="suallar"),
         InlineKeyboardButton("Bizi izləyin 🔍", callback_data="hesablar")],
         [InlineKeyboardButton("Sifariş üçün müraciət 💌", callback_data="sifariş_müraciət")]
    ])
    
    callback_query.message.edit_text(
        f"Aşağıdakı seçimlər arasından bir əməliyyat başlatmaq üçün düymələri basın\n",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("geyimler"))
def geyimler(client, callback_query):

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Sweatshirt ✅", callback_data="sweatshirt")],
        [InlineKeyboardButton("Hoodie ✅", callback_data="hoodie")],
        [InlineKeyboardButton("T-Shirt ✅", callback_data="tshirt")],
        [InlineKeyboardButton("Jacket ✅", callback_data="jacket")],
        [InlineKeyboardButton("Geriyə ↩️", callback_data="geriyə")]
    ])
    
    callback_query.message.edit_text(
        f"Hal-hazırda aşağıdakı geyimlərin sifarişini qəbul edirik\n",
        reply_markup=keyboard
    )



@app.on_callback_query(filters.regex("sweatshirt"))
def sweatshirt(client, callback_query):
    text = "Hal-hazırda dizayn edilib paylaşılmış sweatshirt✅\nQeyd: Geyimlərimiz Unisex-dir. Yəni ki, istənilən cins geyinə bilər🫱🏻‍🫲🏻\nSifariş etmək üçün aşağıdakı düyməni klikləyin."
    
    images_and_captions = [
        ("sweatshirt1.jpg", text),
        ("sweatshirt2.jpg", text),
        ("sweatshirt3.jpg", text)
    ]

    for image, caption in images_and_captions:
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Sifariş Et", callback_data="sifariş_müraciət")],
            [InlineKeyboardButton("Ana Menyu", callback_data="ana_ekran")]
        ])

        callback_query.message.reply_photo(photo=image, caption=caption, reply_markup=keyboard)

@app.on_callback_query(filters.regex("hoodie"))
def hoodie(client, callback_query):
    text = "Hal-hazırda dizayn edilib paylaşılmış hoodie✅\nQeyd: Geyimlərimiz Unisex-dir. Yəni ki, istənilən cins geyinə bilər🫱🏻‍🫲🏻\nSifariş etmək üçün aşağıdakı düyməni klikləyin."
    
    images_and_captions = [
        ("hoodie1.jpg", text),
        ("hoodie2.jpg", text),
        ("hoodie3.jpg", text)
    ]

    for image, caption in images_and_captions:
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Sifariş Et", callback_data="sifariş_müraciət")],
            [InlineKeyboardButton("Ana Menyu", callback_data="ana_ekran")]
        ])

        callback_query.message.reply_photo(photo=image, caption=caption, reply_markup=keyboard)


@app.on_callback_query(filters.regex("tshirt"))
def tshirt(client, callback_query):

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Sweatshirt ✅", callback_data="sweatshirt")],
        [InlineKeyboardButton("Hoodie ✅", callback_data="hoodie")],
        [InlineKeyboardButton("T-Shirt ✅", callback_data="tshirt")],
        [InlineKeyboardButton("Jacket ✅", callback_data="jacket")],
        [InlineKeyboardButton("Geriyə ↩️", callback_data="geriyə")]
    ])
    
    callback_query.message.edit_text(
        f"Hal-hazırda dizayn edilib paylaşılmış tshirt mövcud deyil✅\n",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("jacket"))
def jacket(client, callback_query):

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Sweatshirt ✅", callback_data="sweatshirt")],
        [InlineKeyboardButton("Hoodie ✅", callback_data="hoodie")],
        [InlineKeyboardButton("T-Shirt ✅", callback_data="tshirt")],
        [InlineKeyboardButton("Jacket ✅", callback_data="jacket")],
        [InlineKeyboardButton("Geriyə ↩️", callback_data="geriyə")]
    ])
    
    callback_query.message.edit_text(
        f"Hal-hazırda dizayn edilib paylaşılmış jacket mövcud deyil✅\n",
        reply_markup=keyboard
    )
@app.on_callback_query(filters.regex("kabrolar"))
def kabro(client, callback_query):
    text = "Bu kimi case'lər üçün müraciət edə bilərsiniz✅\nSifariş etmək üçün aşağıdakı düyməni klikləyin."
    
    images_and_captions = [
        ("kabro.jpg", text)
    ]

    for image, caption in images_and_captions:
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Sifariş Et", callback_data="sifariş_müraciət")],
            [InlineKeyboardButton("Ana Menyu", callback_data="ana_ekran")]
        ])

        callback_query.message.reply_photo(photo=image, caption=caption, reply_markup=keyboard)

@app.on_callback_query(filters.regex("çatdırılma"))
def hesablar(client, callback_query):

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Geriyə ↩️", callback_data="geriyə")]
    ])
    
    callback_query.message.edit_text(
        f"The Asad Wear,istənilən metroya,bölgəyə hətta başqa ölkələrə belə çatdırılma edir\n",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("hesablar"))
def hesablar(client, callback_query):

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Telegram", url="https://t.me/theasadwear")],
        [InlineKeyboardButton("WhatsApp", url="https://wa.me/994507341060")],
        [InlineKeyboardButton("İnstagram", url="https://instagram.com/theasad_wear")],
        [InlineKeyboardButton("Geriyə ↩️", callback_data="geriyə")]
    ])
    
    callback_query.message.edit_text(
        f"Bizi aşağıdakı sosial şəbəkələrdən izləyə bilərsiniz\n",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("suallar"))
def suallar(client, callback_query):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Geyimlərin istifadə qaydası zəhmət olmasa?", callback_data="sual1")],
        [InlineKeyboardButton("Geyim alanda ödənişi etsəm olar?", callback_data="sual2")],
        [InlineKeyboardButton("Çatdırılma mövcuddur?🛵", callback_data="sual3")],
        [InlineKeyboardButton("Geyimlərin tərkibi nədən ibarətdir?", callback_data="sual4")],
        [InlineKeyboardButton("Unisex nədir?", callback_data="sual5")],
        [InlineKeyboardButton("Geriyə ↩️", callback_data="geriyə")]
    ])
    
    callback_query.message.edit_text(
        "Hal-hazırda aşağıdakı suallar mövcuddur:\n",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("sual1"))
def sual1(client, callback_query):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Geriyə ↩️", callback_data="suallar")]
    ])
    
    callback_query.message.edit_text(
        "• Geyimləri 30° temperaturda yuyulmalıdır ! ✅\n\n"
        "• Geyimlərin üzərinə Ətir və Birbaşa Ütü dəyməməlidir ! ✅\n\n"
        "• Yuyub-Ütülədiyiniz zaman geyimləri tərs üzünə çevirməyiniz məsləhət görülür ! ✅",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("sual2"))
def sual2(client, callback_query):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Geriyə ↩️", callback_data="suallar")]
    ])
    
    callback_query.message.edit_text(
        "Təəsüf ki, mağaza şərtlərimizə əsasən, sifariş qəbul edildikdə müştəridən geyimin 50% alınır💸\n",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("sual3"))
def sual3(client, callback_query):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Geriyə ↩️", callback_data="suallar")]
    ])
    
    callback_query.message.edit_text(
        "BƏLİ ✅\n\n"
        "Çatdırılma istənilən metroya🚇, istənilən bölgəyə🚗, istənilən ölkəyə✈️ mövcuddur 🤝🏻😎\n",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("sual4"))
def sual4(client, callback_query):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Geriyə ↩️", callback_data="suallar")]
    ])
    
    callback_query.message.edit_text(
        "Geyimlərimiz 95% pambıq tərkiblidir. İçi mexdir, rəng və forma itməyən materialdandır.\n"
        "İstənilən yazı və şəkil forması edilir.\n",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("sual5"))
def sual5(client, callback_query):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Geriyə ↩️", callback_data="suallar")]
    ])
    
    callback_query.message.edit_text(
        "Unisex dedikdə həm qadın, həm kişi paylaşdığımız dizaynda olan geyimi geyinə bilər🫱🏻‍🫲🏻\n",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("ana_ekran"))
def anamenyu(client, callback_query):


    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Geyimlər 👕", callback_data="geyimler")],
        [InlineKeyboardButton("Telefon Caseləri 📱", callback_data="kabrolar")],
        [InlineKeyboardButton("Ödəniş 💳", callback_data="ödəniş"),
         InlineKeyboardButton("Çatdırılma 🛵", callback_data="çatdırılma")],
        [InlineKeyboardButton("Suallar ❓", callback_data="suallar"),
         InlineKeyboardButton("Bizi izləyin 🔍", callback_data="hesablar")],
         [InlineKeyboardButton("Sifariş üçün müraciət 💌", callback_data="sifariş")]
    ])
    callback_query.message.reply_text(
        f"Aşağıdakı seçimlər arasından bir əməliyyat başlatmaq üçün düymələri basın\n",
        reply_markup=keyboard
    )


@app.on_callback_query(filters.regex("sifariş_müraciət"))
def siparis_muraciet(client, callback_query):
    user_id = callback_query.from_user.id
    user_data[user_id] = {}
    user_state[user_id] = "awaiting_photo"  
    callback_query.message.reply_text("Sifariş etmək və yaxud da çap etmək istədiyiniz məhsulun şəklini göndərin.")

    app.add_handler(MessageHandler(handle_photo, filters.photo), group=1)

def handle_photo(client, message):
    user_id = message.from_user.id

    if user_state.get(user_id) == "awaiting_photo":
        user_data[user_id]['photo'] = message.photo.file_id
        user_state[user_id] = "awaiting_location"  
        message.reply_text("Sifarişi çatdırmaq üçün bizimlə konumunuzu paylaşın")
        app.add_handler(MessageHandler(handle_location, filters.location), group=2)

def handle_location(client, message):
    user_id = message.from_user.id

    if user_state.get(user_id) == "awaiting_location":
        user_data[user_id]['location'] = message.location
        user_state[user_id] = "awaiting_phone_number"  
        message.reply_text("Telefon nömrənizi +994xxxxxxxxx formatında paylaşın.")
        app.add_handler(MessageHandler(handle_phone_number, filters.text), group=3)

def handle_phone_number(client, message):
    user_id = message.from_user.id

    if user_state.get(user_id) == "awaiting_phone_number":
        phone_number = message.text


        if re.match(r"^\+994\d{9}$", phone_number):
            user_data[user_id]['phone_number'] = phone_number
            user_state[user_id] = "awaiting_name"  
            message.reply_text("Adınızı və soyadınızı daxil edin.")
            app.add_handler(MessageHandler(handle_name, filters.text), group=4)
        else:
            message.reply_text("Telefon nömrəsi formatı yanlışdır. Zəhmət olmasa +994xxxxxxxxx formatında təkrar daxil edin.")

def handle_name(client, message):
    user_id = message.from_user.id

    if user_state.get(user_id) == "awaiting_name":
        name = message.text.strip()

  
        if len(name.split()) >= 1: 
            user_data[user_id]['name'] = name
            
            username = message.from_user.username
            username_text = f"@{username}" if username else "Yoxdur"

            client.send_message(
                chat_id=ADMIN_ID,
                text=f"Yeni sifariş! 🛒\n\n"
                     f"İstifadəçi: {user_data[user_id]['name']}\n"
                     f"Telefon Nömrəsi: {user_data[user_id]['phone_number']}\n"
                     f"Konum: {user_data[user_id]['location'].latitude}, {user_data[user_id]['location'].longitude}\n"
                     f"Username: {username_text}\n"
                     f"ID: {user_id}\n"
                     f"Profil Linki: [Profilə keçid](tg://user?id={user_id})"
            )
            client.send_photo(
                chat_id=ADMIN_ID,
                photo=user_data[user_id]['photo'],
                caption="Sifariş edilən məhsul"
            )

            
            message.reply_text("Sifarişiniz qəbul edildi, ən qısa müddətdə ödəniş haqqında məlumatlandırılacaqsınız.")
            user_state[user_id] = None  
        else:
            message.reply_text("Ad və soyad boş ola bilməz. Zəhmət olmasa düzgün ad və soyad daxil edin.")

app.run()