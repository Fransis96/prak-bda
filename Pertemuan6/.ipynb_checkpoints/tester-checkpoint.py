from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ContextTypes

token = "YOUR_BOT_TOKEN"

# Fungsi untuk membuat inline keyboard
def build_menu():
    keyboard = [
        [InlineKeyboardButton("Mulai Sesi", callback_data='start')],
        [InlineKeyboardButton("Bantuan", callback_data='help')],
        [InlineKeyboardButton("Akun GitHub", callback_data='github')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Fungsi untuk respon /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Saya bot Telegram!", reply_markup=build_menu())

# Fungsi untuk respon /help
async def bantuan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    menu_bantuan = """
    Menu yang tersedia:
    - /start : Memulai sesi
    - /help  : Bantuan
    - /github : Akun github
    """
    await update.message.reply_text(menu_bantuan, reply_markup=build_menu())

# Fungsi untuk respon /github
async def github(update: Update, context: ContextTypes.DEFAULT_TYPE):
    github_acc = "[Kunjungi akun GitHub saya](https://github.com/Fransis96)"
    await update.message.reply_text(github_acc, parse_mode="Markdown", reply_markup=build_menu())

# Fungsi untuk menangani tombol yang dipilih pengguna
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Menyelesaikan callback yang ada
    if query.data == 'start':
        await query.edit_message_text(text="Halo! Saya bot Telegram. Pilih menu di bawah.")
    elif query.data == 'help':
        await query.edit_message_text(text="Menu yang tersedia:\n/start - Memulai sesi\n/help - Bantuan\n/github - Akun GitHub")
    elif query.data == 'github':
        await query.edit_message_text(text="Kunjungi akun GitHub saya: [github.com/Fransis96](https://github.com/Fransis96)", parse_mode="Markdown")

# Fungsi untuk menangani perintah tidak valid
async def handle_invalid_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Perintah tidak valid! Silakan pilih dari menu di bawah.", reply_markup=build_menu())

# Main
app = Application.builder().token(token).build()

# Menambahkan handler untuk setiap perintah
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", bantuan))
app.add_handler(CommandHandler("github", github))

# Handler untuk tombol
app.add_handler(CallbackQueryHandler(button))

# Handler untuk perintah tidak valid
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_invalid_command))

app.run_polling()
