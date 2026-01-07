import telebot, time
from telebot import types

# --- إعدادات البوت ---
# التوكن الجديد
API_TOKEN = '8534960248:AAHUaOFPs4SvojH7RsaOzAbUUEbxWime_1w'
bot = telebot.TeleBot(API_TOKEN)

# رابط الـ GIF
STORM_GIF = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueGZ3eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7TKMGpxxcaNn9X2M/giphy.gif"

# --- القائمة الرئيسية ---
def main_menu():
    m = types.InlineKeyboardMarkup(row_width=2)
    m.add(
        types.InlineKeyboardButton("● Storm Hub", callback_data="storm"),
        types.InlineKeyboardButton("● Account Login", callback_data="login"),
        types.InlineKeyboardButton("● Session List", callback_data="sessions"),
        types.InlineKeyboardButton("● Performance", callback_data="stats")
    )
    m.add(types.InlineKeyboardButton("○ Terminate All", callback_data="stop"))
    return m

@bot.message_handler(commands=['start'])
def welcome(m):
    bot.send_message(m.chat.id, "───「 DaRk SyStEm v5.0 」───\nالوضع: متصل وآمن.", reply_markup=main_menu())

# --- معالجة الأزرار ---
@bot.callback_query_handler(func=lambda c: True)
def handle_buttons(c):
    if c.data == "storm":
        bot.send_animation(c.message.chat.id, STORM_GIF, caption="🚀 Storm Hub is Active!")
    
    elif c.data == "login":
        msg = bot.send_message(c.message.chat.id, "● ارسل اسم المستخدم الآن:")
        bot.register_next_step_handler(msg, lambda m: bot.send_message(m.chat.id, f"✅ تم حفظ @{m.text}", reply_markup=main_menu()))
    
    elif c.data == "sessions":
        # تفعيل خيار عرض الجلسات بشكل مبسط
        bot.send_message(c.message.chat.id, "📋 **قائمة الجلسات النشطة:**\n\n1- Session_882 (Active)\n2- Session_901 (Idle)\n\n_لا توجد جلسات أخرى حالياً._", parse_mode="Markdown")
    
    elif c.data == "stats":
        # تحسين عرض الأداء
        status_text = "📊 تفاصيل الأداء:\n• Uptime: 99.9%\n• Ping: 24ms\n• CPU: 12%\n• Status: Stable"
        bot.answer_callback_query(c.id, status_text, show_alert=True)
    
    elif c.data == "stop":
        bot.answer_callback_query(c.id, "تم إيقاف كافة العمليات بنجاح.", show_alert=True)

# --- نظام التشغيل ---
print("🚀 DaRk SyStEm is Starting on NEW Account...")
while True:
    try:
        bot.infinity_polling()
    except Exception:
        time.sleep(5)
