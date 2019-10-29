
from pyfcm import FCMNotification


def send_fcm_message(api_key : str, title : str, message : str, tokens: list):
    push_service: FCMNotification = FCMNotification(api_key=api_key)
    result = push_service.notify_multiple_devices(registration_ids=tokens, message_body=message, message_title=title, data_message={'msg' : message, 'contentTitle':title})
    return result