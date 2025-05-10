import requests
import time
from datetime import datetime

# عنوان webhook الخاص بـ Discord
WEBHOOK_URL = 'https://discord.com/api/webhooks/1360722108329623664/rQ22UOkzguqDlNSXZ0nJ2mAnyKGGnCPLsj8hlgDSxWbo_wg2_xnQRzJuLm95WfeQ_eGX'

# رابط للحصول على الأخبار (أدخل مفتاح API الخاص بك هنا)
NEWS_API_URL = "https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_NEWS_API_KEY"

# جلب الأخبار من واجهة API
def fetch_news():
    response = requests.get(NEWS_API_URL)
    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        return articles
    else:
        return None

# إرسال الأخبار إلى Discord عبر Webhook
def send_to_discord(news):
    for article in news:
        title = article['title']
        description = article['description']
        url = article['url']
        message = {
            "content": f"**{title}**\n{description}\n[Read more]({url})"
        }
        response = requests.post(WEBHOOK_URL, json=message)
        if response.status_code == 204:
            print(f"Message sent: {title}")
        else:
            print(f"Failed to send message for {title}")

# دالة لتحديد الإشعارات في أوقات محددة (مثلاً 7 صباحًا و 9 مساءً)
def send_at_specific_times():
    while True:
        current_time = datetime.now().strftime("%H:%M")  # الوقت الحالي
        if current_time == "07:00" or current_time == "21:00":
            news = fetch_news()
            if news:
                send_to_discord(news)
            time.sleep(60)  # الانتظار 60 ثانية بين كل تحقق
        time.sleep(30)  # تحقق كل 30 ثانية

# بدء تشغيل السكربت
send_at_specific_times()
