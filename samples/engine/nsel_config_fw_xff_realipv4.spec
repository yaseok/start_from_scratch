# engine apply - xff real ipv4

Tags: DEVICE.real_cent.ini, DEVICE.nsel_attacker.ini
table: data/engine/table_config_fw_xff_real_ipv4.csv

## 기본 Setup
* HIPS:"VS_DUT01"에 FW XFF Real IPv4 차단 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다

## XFF Real IPv4 (방화벽, 국가기반)
* "ATTACK01"에서 "$VS_DUT01.ip"로 XFF Real IP 패킷을 전송한다 (<realip>)
* HIPS:"VS_DUT01"에서 XFF Real IP 로그를 확인한다 (<logcheck>, <log_key_1>, <log_keytype_1>, <log_value_1>, <log_key_2>, <log_keytype_2>, <log_value_2>, <log_key_3>, <log_keytype_3>, <log_value_3>)