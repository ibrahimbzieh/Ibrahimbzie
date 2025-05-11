import requests
import json

# رابط Webhook الخاص بك
webhook_url = "https://discord.com/api/webhooks/1360722144870273136/woduEJYO-1Bv9nH3Qgc7gPcTHtwmEK11i1XwPFMImX0KpwDa8CPc6SBzc5xaEsqTTqwe"

# رابط API للأخبار باستخدام مفتاح API الذي ذكرته
news_api_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=7e15e3777ba4499e8e714456069a53a7"

# الحصول على الأخبار
response = requests.get(news_api_url)
if response.status_code == 200:
    news_data = response.json()
    articles = news_data["articles"]

    # جمع الأخبار التي سيتم إرسالها
    news_message = ""
    for article in articles[:5]:  # يمكن تحديد عدد المقالات
        title = article["title"]
        url = article["url"]
        news_message += f"{title}\n{url}\n\n"
    
    # إرسال الأخبار إلى ديسكورد عبر Webhook
    data = {
        "content": f"أخبار اليوم:\n{news_message}"
    }
    discord_response = requests.post(webhook_url, json=data)

    if discord_response.status_code == 204:
        print("تم إرسال الأخبار بنجاح!")
    else:
        print(f"فشل في إرسال الأخبار. كود الحالة: {discord_response.status_code}")
else:
    print(f"فشل في الحصول على الأخبار. كود الحالة: {response.status_code}")
