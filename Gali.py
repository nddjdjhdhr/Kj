from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext
import random

# Replace with your bot token
BOT_TOKEN = "7828550293:AAHQK64NpZdRSDhAhDdOo2ZOrWu-OKO8G1I"

# List of abusive replies
ABUSE_LIST = [
    "RANDI KE BACCHE, @{name}!",
    "BAHEN KE LAWDE, @{name}?",
    "FUCK YOU, @{name}!",
    "MADARCHOD, @{name}!",
    "@{name}, TUMARI MAA KA BHEWDE'!"
    "MADARCHOD, @{name}!",
    "TARI MAA KA BHOSDA, @{name}!",
    "TARI MAA RANDI, @{name}!",
    "TARI MAA KI CHUT, @{name}!",
    "LAWDE, @{name}!",
    "bhosdike,@{name}!",
    "MAI KAHU BURGER TARI CHUTKI BAHANI KO CHODUNGA GHAR GHAR, @{name}!",
    "TARA PHELA BAAP HU BHOSDIKE, @{name}!",
    "TARI MAA KO CHUT BAHEN KE LAWDE, @{name}!",
    "TARI MAA KA CHODA, @{name}!",
    "MAA KE LAWDE",
    "BAHENCHOOD",
    "HARAAMKHOR",
    "KUTTE KE BACCHE",
    "MKC",
    "TMKC",
    "BKL",
    "RANDI",
    "RANDI KE PILLE",
    "BHOSDIKE",
    "LAWDE KE BAAL",
    "TARI MIYAA CHOD DALUNGA",
    "SUAR KE AULAD",
    "BHADWE",
    "BETICHOD",
    "MAACHOD",
    "RANDI",
    "TARI MAA KA LUND",
    "TARI BAHEN KI CHUT",
    "TARI BAHEN KA BHOSDA",
    "YOU ARE RANDI",
    "KYA RE CHAKKA",
    "GAY SPOTTED",
    "TARA BAAP RANDI",
    "TARA BAAP HU BHOSDIKE",
    "TARI MAA BHOSDI",
    "CHAPRI",
    "TARI BAHEN KA LUND",
    "MADARCHOD",
    "TARI MAA CHOD DUNGA",
    "TARA BAAP HU MAI",
    "@{random_username} dekh ye tara baap hai Bhosdike bacche",
    "TARI MAA KA PURA BHOSDA FAAD DUNGA",
    "LAWDE KE BEEJ",
    "RANDI KE BEEJ",
    "CHUTIYE KE BACCHE",
    "4 BAAP KE AULAD",
    "@{random_username} DEKH YE HAI TARA PHELE BAAP",
    "@{random_username} DEKH YE HAI TARA DUSRA BAAP",
    "@{random_username} DEKH YE HAI TARA TESRA BAAP",
    "@{random_username} DEKH YE HAI TARA CHOTA BAAP",
    
]

async def abuse_reply(update: Update, context: CallbackContext):
    """Replies directly to the user's message with an abusive response using their username."""
    if update.message.chat.type in ["group", "supergroup"]:
        user = update.message.from_user
        user_name = user.username if user.username else user.first_name  # Use username if available, otherwise first name
        reply_text = random.choice(ABUSE_LIST).format(name=user_name)  # Insert username
        await update.message.reply_text(reply_text, reply_to_message_id=update.message.message_id)  # Reply to message

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, abuse_reply))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
