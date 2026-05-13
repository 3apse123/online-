import telebot

# تۆکنەکەی خۆت لێرە جێگیر کراوە
TOKEN = '8940054373:AAEs7ysVW_vSwGeBxAJlvHkeoHBk8n3xAvQ'
bot = telebot.TeleBot(TOKEN)

# بەشی بەخێرهاتنی ئەندامی نوێ
@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    for member in message.new_chat_members:
        user_name = member.first_name
        welcome_text = f"بەخێربێیت {user_name} بۆ ناو قووڵایی Deadly Ocian! 🌊💀"
        bot.send_message(message.chat.id, welcome_text)

print("Cranium is running...")
bot.infinity_polling()
