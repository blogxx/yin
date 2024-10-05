from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Token bot Anda
BOT_TOKEN = '7898032099:AAHwzMeTRyA_T0v27PZTj03yEbzh25cV9EM'

# Fungsi untuk menangani command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Selamat datang! Gunakan /artikel untuk mendapatkan artikel.")

# Fungsi untuk menangani command /artikel
async def artikel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pesan_html = """
    <b>Judul Artikel</b>
    <i>Ini adalah isi artikel yang diformat dengan HTML.</i>
    Anda bisa menambahkan <u>teks underline</u> atau bahkan <a href='https://example.com'>tautan</a>.
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text=pesan_html, parse_mode='HTML')

# Fungsi utama untuk menjalankan bot
def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('artikel', artikel))

    application.run_polling()

if __name__ == '__main__':
    main()