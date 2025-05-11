import requests

# رابط الويب هوك الجديد
webhook_url = "https://discord.com/api/webhooks/1360722144870273136/woduEJYO-1Bv9nH3Qgc7gPcTHtwmEK11i1XwPFMImX0KpwDa8CPc6SBzc5xaEsqTTqwe"
# بيانات الرسالة التي تريد إرسالها
data = {
    "content": "هذه رسالة من السكربت! 🚨"
}

# إرسال البيانات إلى الويب هوك
response = requests.post(webhook_url, json=data)

# التحقق من الرد
if response.status_code == 204:
    print("تم إرسال الرسالة بنجاح!")
else:
    print(f"فشل في إرسال الرسالة. كود الحالة: {response.status_code}")
