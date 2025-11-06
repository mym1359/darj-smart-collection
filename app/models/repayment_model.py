def predict_action(delay_days, contact_count, promise_given, promise_kept):
    """
    Predict the recommended action for debt collection based on customer behavior.

    Parameters:
    - delay_days (int): Number of days the payment is delayed
    - contact_count (int): Number of times the customer has been contacted
    - promise_given (bool): Whether the customer has promised to pay
    - promise_kept (bool): Whether the customer has kept the promise

    Returns:
    - str: Recommended action ("Call", "SMS", "Legal", "Wait")
    """

    if delay_days > 90 and not promise_kept:
        return "Legal"
    elif delay_days > 30 and contact_count >= 3 and promise_given and not promise_kept:
        return "Call"
    elif delay_days <= 30 and not promise_given:
        return "SMS"
    else:
        return "Wait"