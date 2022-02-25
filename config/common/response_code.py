STATUS_SUCCESS = 200  # 성공

MSG_RSP_SUCCESS = 'success'
MSG_RSP_PERMISSION_ERROR = '유저 접근 권한이 없습니다.'
MSG_RSP_USER_DOES_NOT_EXISTS = '존재하지 않는 유저입니다.'
MSG_RSP_USER_EMAIL_ALREADY_EXISTS = '동일한 이메일이 존재합니다.'
MSG_RSP_USER_NOT_MATCHED = '아이디 혹은 비밀번호를 확인해주세요.'

MSG_RSP_PURCHASE_DOES_NOT_EXISTS = "존재하지 않는 구매 상품입니다."
MSG_RSP_CATEGORY_DOES_NOT_EXISTS = '존재하지 않는 카테고리입니다.'
MSG_RSP_PRODUCT_DOES_NOT_EXISTS = '존재하지 않는 상품입니다.'
MSG_RSP_PRODUCT_PRICE_IS_NOT_POSITIVE_NUM = '제품 가격이 0보다 작습니다.'

code_to_alert = {
    STATUS_SUCCESS: MSG_RSP_SUCCESS,
}


def code_to_message(code):
    return code_to_alert.get(code)
