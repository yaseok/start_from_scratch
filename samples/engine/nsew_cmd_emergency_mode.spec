# emergency_mode
Tags: DEVICE.real_win.ini, DEVICE.nsew_attacker.ini
table: data/engine/table_cmd_emergency_mode.csv

## NSEW 설치
* W_HIPS:"W_DUT"에 NSEW를 설치한다.

## 기본 Setup
* W_HIPS:"W_DUT"에 IPS 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다

## emergency mode

* W_HIPS:"W_DUT"에서 에이전트 설정을 변경하고 확인한다 (<anse_cmd_config>, <anse_cmd_result>, <result_value>)
* "ATTACK"에서 "$W_DUT.ip"로 Signature가 "GET /TEST.html"이고 TCP 목적지 포트가 "80"인 패킷을 전송한다
* W_HIPS:"W_DUT"에서 엔진의 이벤트 로그를 확인한다 (<logcheck>, <log_key_1>, <log_keytype_1>, <log_value_1>, <log_key_2>, <log_keytype_2>, <log_value_2>, <log_key_3>, <log_keytype_3>, <log_value_3>)
