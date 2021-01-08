from auto_heating.models import motor
from auto_heating.models import notify


def switch_on():
    servomotor = motor.Servomotor()
    servomotor.move()

    line_notify = notify.LineNotify()
    line_notify.send_message('暖房をつけました。')
