# engine apply - custom URL

Tags: DEVICE.real_cent.ini, DEVICE.nsel_attacker.ini
table: data/engine/table_config_ips_user_url.csv

## 기본 Setup
* HIPS:"VS_DUT01"에 사용자 정의 URL 차단 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다

## 사용자 정의 URL 차단
* "VS_DUT01"에서 "hyunseok"content가 포함된 URL 패킷을 전송한다
* HIPS:"VS_DUT01"에서 엔진의 시그니처 옵션 이벤트 로그를 확인한다 (<logcheck>, <log_key_1>, <log_keytype_1>, <log_value_1>, <log_key_2>, <log_keytype_2>, <log_value_2>, <log_key_3>, <log_keytype_3>, <log_value_3>)