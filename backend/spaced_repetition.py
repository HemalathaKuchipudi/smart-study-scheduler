from datetime import timedelta

def calculate_next_review_date(date_studied, review_number=1):
    days_gap = [1, 3, 7, 14, 30, 60]
    interval = days_gap[min(review_number - 1, len(days_gap) - 1)]
    return date_studied + timedelta(days=interval)
