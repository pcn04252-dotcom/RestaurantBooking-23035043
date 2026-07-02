from communication import SmsSender
from communication import MailSender
from booking_scheduler import BookingScheduler

class TestableSmsSender(SmsSender):
    def __init__(self):
        super().__init__()
        self._send_called = False

    def send(self, schedule):
        print("테스트용 SmsSender에서 send 메서드 실행됨")
        self._send_called = True

    @property
    def send_called(self):
        return self._send_called

class TestableMailSender(MailSender):
    def __init__(self):
        self._send_mail_count = 0

    def send_mail(self, schedule):
        self._send_mail_count += 1

    @property
    def send_mail_count(self):
        return self._send_mail_count

class TestableBookingScheduler(BookingScheduler):
    def __init__(self, capacity_per_hour):
        super().__init__(capacity_per_hour)
        self._is_sunday = False

    def set_sunday(self):
        self._is_sunday = True

    def is_sunday(self):
        return self._is_sunday