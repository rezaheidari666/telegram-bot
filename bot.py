import telebot

# 🔹 جای 'YOUR_BOT_TOKEN' توکن رباتت رو بذار
TOKEN = "7660711019:AAFskdOrUtdF-I7xFJdnOno7hzKGgK0B1Xs"
bot = telebot.TeleBot(TOKEN)

# 🔹 این تابع وقتی پیامی دریافت شد، اجرا میشه
@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    response ="سلام !چطوري؟ من فعلا نيستم بعدا بهت پيام ميدم."
    bot.send_message(message.chat.id, response)

# 🔹 اجرای ربات
print("ربات در حال اجراست...")
bot.infinity_polling()
