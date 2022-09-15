# fw block_nation

Tags: DEVICE.real_win.ini, DEVICE.nsew_attacker.ini
table: data/engine/w_table_config_fw_block_nation.csv

## NSEW 설치
* W_HIPS:"W_DUT"에 NSEW를 설치한다.

## 기본 Setup
* W_HIPS:"W_DUT"에 방화벽 차단 국가 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다

## block_nation

* W_HIPS:"W_DUT"에 국가 DB 방화벽 테스트를 위한 정책을 설정 및 적용한다 (<policy_enable>, <nation1>, <nation_direction1>)
* W_HIPS:"W_DUT"에 방화벽 테스트를 위한 설정 파일을 적용한다
* W_HIPS:"W_DUT"에서 로그 초기화
* "W_DUT"에서 "cd /windows/system32"를 실행한다
* "W_DUT"에서 "./ping 1.0.1.1 -n 2"를 실행한다
* "ATTACK"에서 "$W_DUT.ip"로 Signature가 "GET /TEST.html"이고 출발지 IP가 1.0.1.1 인 패킷을 전송함
* W_HIPS:"W_DUT"에서 엔진의 이벤트 로그를 확인한다 (<logcheck>, <log_key_1>, <log_keytype_1>, <log_value_1>, <log_key_2>, <log_keytype_2>, <log_value_2>, <log_key_3>, <log_keytype_3>, <log_value_3>)