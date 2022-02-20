from rest_framework import status

STATUS_SUCCESS = 200
STATUS_INVALID_PARAM = 4000

STATUS_USER_PERMISSION_ERROR = 4200
STATUS_USER_DOES_NOT_EXISTS = 4201
STATUS_USER_EMAIL_ALREADY_EXISTS = 4202
STATUS_USER_PASSWORD_NOT_MATCHED = 4203

MSG_RSP_SUCCESS = '성공'
MSG_RSP_PERMISSION_ERROR = '유저 접근 권한이 없습니다.'

code_to_alert = {
    STATUS_SUCCESS: MSG_RSP_SUCCESS,
    STATUS_USER_PERMISSION_ERROR: MSG_RSP_SUCCESS,
}


def code_to_message(code):
    return code_to_alert.get(code)
