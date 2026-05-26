import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ═══════════════════════════════════════════
#   SHARSHARA HOTEL — TELEGRAM BOT
# ═══════════════════════════════════════════

TOKEN = "8600992106:AAH_QrWxo65YCZnrkFa9WAtY7GxZ6CNHdeA"
SITE_URL = "https://sharsharahotel.netlify.app"
PHONE = "+998952806633"

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO
)

# ─── MATNLAR ───────────────────────────────
TEXTS = {
    "welcome": """
🏨 *Hotel Sharshara* ga xush kelibsiz\!

🌿 _Zomin tog'lari qo'ynidagi hashamatli dam olish maskani_

Quyidagi bo'limlardan birini tanlang 👇
""",

    "rooms": """
🛏 *Xonalar ro'yxati*

Bizda 3 turdagi xona mavjud:

🔹 *Standart* — Qulay va zamonaviy
🔸 *Polluks* — Premium sharoit
👑 *Lux* — VIP hashamat

To'liq ma'lumot va videolar uchun saytimizga o'ting 👇
""",

    "included": """
✨ *To'lov ichiga kiradi:*

🌊 Sharshara bo'ylab sayohat
🍳 Ertalabki nonushta
🦁 Turli hayvonlar haykallari ziyorati

Barchasi sizning to'lovingiz ichida\! 🎁
""",

    "contact": """
📞 *Biz bilan bog'lanish:*

☎️ Telefon: `+998952806633`
📸 Instagram: @zomin\_sharshara\_hotel
✈️ Telegram: @sharsharahotel

Qo'ng'iroq qiling — sizni kutamiz\! 🤝
""",

    "about": """
🏔 *Hotel Sharshara haqida:*

📍 Joylashuv: Zomin, O'zbekiston
⭐ Daraja: 5 yulduzli mehmonxona
🌿 Tabiat qo'ynida hashamatli dam olish
🎯 Har bir mehmon uchun maxsus e'tibor

_Tabiat qo'ynida hashamat va tinchlik sizni kutmoqda\!_
""",
}

# ─── KLAVIATURALAR ─────────────────────────
def main_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🛏 Xonalar bilan tanishish", url=SITE_URL)],
        [
            InlineKeyboardButton("✨ Nimalar kiradi?", callback_data="included"),
            InlineKeyboardButton("🏔 Biz haqimizda", callback_data="about"),
        ],
        [
            InlineKeyboardButton("📞 Bog'lanish", callback_data="contact"),
            InlineKeyboardButton("🌐 Saytga o'tish", url=SITE_URL),
        ],
    ])

def back_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🛏 Xonalarni ko'rish", url=SITE_URL)],
        [InlineKeyboardButton("◀️ Bosh menyuga qaytish", callback_data="main")],
    ])

def contact_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📞 Qo'ng'iroq qilish", url=f"tel:{PHONE}")],
        [InlineKeyboardButton("🌐 Saytga o'tish", url=SITE_URL)],
        [InlineKeyboardButton("◀️ Bosh menyuga qaytish", callback_data="main")],
    ])

# ─── HANDLERLAR ────────────────────────────
async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name or "Mehmon"
    await update.message.reply_text(
        f"Assalomu alaykum, *{name}*\\!\n" + TEXTS["welcome"],
        parse_mode="MarkdownV2",
        reply_markup=main_keyboard(),
    )

async def button_handler(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "main":
        await query.edit_message_text(
            TEXTS["welcome"],
            parse_mode="MarkdownV2",
            reply_markup=main_keyboard(),
        )
    elif data == "included":
        await query.edit_message_text(
            TEXTS["included"],
            parse_mode="MarkdownV2",
            reply_markup=back_keyboard(),
        )
    elif data == "about":
        await query.edit_message_text(
            TEXTS["about"],
            parse_mode="MarkdownV2",
            reply_markup=back_keyboard(),
        )
    elif data == "contact":
        await query.edit_message_text(
            TEXTS["contact"],
            parse_mode="MarkdownV2",
            reply_markup=contact_keyboard(),
        )

# ─── ISHGA TUSHIRISH ───────────────────────
def main():
    print("🚀 Sharshara Hotel boti ishga tushmoqda...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("✅ Bot tayyor! Telegramda @sharshara_hotel_bot ga yozing.")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
