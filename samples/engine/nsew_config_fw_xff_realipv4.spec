# fw xff real ipv4

Tags: DEVICE.real_win.ini, DEVICE.nsew_attacker.ini
table: data/engine/table_config_fw_xff_real_ipv4.csv

## NSEW 설치
* W_HIPS:"W_DUT"에 NSEW를 설치한다.

## 기본 Setup
* W_HIPS:"W_DUT"에 XFF Real IPv4 차단 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다

## XFF Real IPv4 (방화벽, 국가기반)
* "ATTACK"에서 "$W_DUT.ip"로 XFF Real IP 패킷을 전송한다 (<realip>)
* W_HIPS:"W_DUT"에서 XFF Real IP 로그를 확인한다 (<logcheck>, <log_key_1>, <log_keytype_1>, <log_value_1>, <log_key_2>, <log_keytype_2>, <log_value_2>, <log_key_3>, <log_keytype_3>, <log_value_3>)
* "W_DUT"에서 "C:/tmp/./anse_ctl engine chcb json"를 실행한다
* "W_DUT"에서 "del c:/tmp/engine_event.json"를 실행한다
* "W_DUT"에서 "./anse_ctl engine chcb json c:/tmp/engine_event.json"를 실행한다