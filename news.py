import requests
from googletrans import Translator  # مكتبة للترجمة من جوجل

# رابط Webhook الخاص بك
webhook_url = "https://discord.com/api/webhooks/1360722144870273136/woduEJYO-1Bv9nH3Qgc7gPcTHtwmEK11i1XwPFMImX0KpwDa8CPc6SBzc5xaEsqTTqwe"

# رابط API للأخبار باستخدام مفتاح API الذي ذكرته، مع تصفية الأخبار الاقتصادية والاجتماعية
news_api_url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=7e15e3777ba4499e8e714456069a53a7"

# تهيئة المترجم
translator = Translator()

# الحصول على الأخبار
response = requests.get(news_api_url)
if response.status_code == 200:
    news_data = response.json()
    articles = news_data["articles"]

    # جمع الأخبار التي سيتم إرسالها
    news_message = ""
    for article in articles[:5]:  # إرسال أول 5 مقالات فقط
        title = article["title"]
        description = article["description"] if article["description"] else "لا توجد تفاصيل إضافية."
        
        # ترجمة العنوان والتفاصيل إلى العربية
        title_arabic = translator.translate(title, src='en', dest='ar').text
        description_arabic = translator.translate(description, src='en', dest='ar').text
        
        news_message += f"العنوان: {title_arabic}\nالتفاصيل: {description_arabic[:150]}...\n\n"  # تلخيص التفاصيل لأقصى حد 150 حرفاً
    
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
