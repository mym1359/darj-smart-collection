def predict_action(delay_days: int, contact_count: int, promise_given: bool, promise_kept: bool) -> str:
    """
    Predict recommended action based on repayment behavior.

    Parameters:
    - delay_days: تعداد روزهای تأخیر
    - contact_count: تعداد تماس‌ها
    - promise_given: آیا مشتری قول داده؟
    - promise_kept: آیا مشتری به قولش عمل کرده؟

    Returns:
    - recommended_action: متن پیشنهادی اقدام
    """

    if delay_days > 90 and not promise_kept:
        return "ارجاع به پیگیری حقوقی"

    if promise_given and not promise_kept:
        return "تماس مجدد با تأکید بر تعهد"

    if delay_days < 30 and contact_count < 2:
        return "ادامه پیگیری تلفنی"

    if delay_days < 15 and promise_kept:
        return "مشتری خوش‌قول، نیازی به اقدام نیست"

    return "بررسی مجدد وضعیت و تصمیم‌گیری توسط کارشناس"