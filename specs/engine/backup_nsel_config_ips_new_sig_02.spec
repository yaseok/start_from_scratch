# engine apply - ips new signature test 2

Tags: DEVICE.real_cent.ini, DEVICE.nsel_attacker.ini
table: data/engine/l_table_config_ips_new_sig_02.csv

## 기본 Setup
* HIPS:"VS_DUT01"에 IPS 신규 시그니처 옵션 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다

## 신규 IPS Sinature 동작 확인 2
* HIPS:"VS_DUT01"에서 엔진의 설정을 변경하고 적용한다_신규 시그니처 옵션 (<path_remote_2>)
* P_L_"ATTACK01"에서 IPS 신규 시그니처 옵션 테스트의 탐지 트래픽을 발생시킨다 (<traffic_protocol1>)
* HIPS:"VS_DUT01"에서 엔진의 시그니처 옵션 이벤트 로그를 확인한다2 (<logcheck>, <log_key_1>, <log_keytype_1>, <log_value_1>, <log_key_2>, <log_keytype_2>, <log_value_2>, <log_key_3>, <log_keytype_3>, <log_value_3>)
