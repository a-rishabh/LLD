from datetime import date

class Fine:
    DAILY_FINE_RATE = 1.0  # $1 per day

    def __init__(self, member_id: str, days_overdue: int):
        self.member_id = member_id
        self.issue_date = date.today()
        self.days_overdue = days_overdue
        self.amount = days_overdue * Fine.DAILY_FINE_RATE
        self.paid = False

   
