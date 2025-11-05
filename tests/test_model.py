from app.services.recommender import recommend_action

def test_recommend_action_high_delay():
    features = {
        'delay_days': 75,
        'contact_count': 3,
        'promise_given': True,
        'promise_kept': False
    }
    result = recommend_action(features)
    assert "اجراییه" in result

def test_recommend_action_low_delay():
    features = {
        'delay_days': 5,
        'contact_count': 0,
        'promise_given': False,
        'promise_kept': False
    }
    result = recommend_action(features)
    assert "کسر اقساط" in result or "پیگیری معمول" in result

def test_recommend_action_no_delay():
    features = {
        'delay_days': 0,
        'contact_count': 0,
        'promise_given': False,
        'promise_kept': True
    }
    result = recommend_action(features)
    assert "خوش‌قول" in result