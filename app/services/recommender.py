def recommend_action(customer_features):
    """
    پیشنهاد مسیر وصول مناسب بر اساس ویژگی‌های مشتری
    ورودی: دیکشنری شامل delay_days, contact_count, promise_given, promise_kept
    خروجی: متن پیشنهاد اقدام
    """

    delay = customer_features.get('delay_days', 0)
    contacts = customer_features.get('contact_count', 0)
    promised = customer_features.get('promise_given', False)
    kept = customer_features.get('promise_kept', False)

    if delay > 60:
        return "📌 صدور اجراییه و پیگیری حقوقی توصیه می‌شود."
    elif delay > 30:
        if not contacts:
            return "📞 تماس اولیه با مشتری و ضامن جهت یادآوری پرداخت"
        elif promised and not kept:
            return "🔔 ارسال اخطار رسمی به دلیل خلف وعده"
        else:
            return "📄 صدور نامه کسر اقساط از حقوق یا حساب"
    elif delay > 0:
        if promised and not kept:
            return "📞 تماس مجدد با مشتری جهت یادآوری قول پرداخت"
        else:
            return "📄 پیگیری معمول و صدور نامه کسر اقساط"
    else:
        return "✅ مشتری خوش‌قول است، نیازی به اقدام نیست."


# مثال تستی
if __name__ == "__main__":
    sample = {
        'delay_days': 45,
        'contact_count': 2,
        'promise_given': True,
        'promise_kept': False
    }
    print("🧠 پیشنهاد مسیر وصول:", recommend_action(sample))