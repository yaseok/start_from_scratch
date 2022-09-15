# ips url obfuscation

Tags: DEVICE.real_win.ini, DEVICE.nsew_attacker.ini
table: data/engine/table_config_ips_url_obf.csv

## NSEW 설치
* W_HIPS:"W_DUT"에 NSEW를 설치한다.

## 기본 Setup
* W_HIPS:"W_DUT"에 IPS 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다

## URL obfuscation
* W_HIPS:"W_DUT"에서 엔진의 설정을 변경하고 적용한다 (Boolean Type, <menu>, <xpath>, <path_local>, <path_remote_1>, <path_remote_2>, <value>)
* "ATTACK"에서 "$W_DUT.ip"로 wget "T%21E%40S%23T%24"를 실행한다
* W_HIPS:"W_DUT"에서 엔진의 이벤트 로그를 확인한다 (<logcheck>, <log_key_1>, <log_keytype_1>, <log_value_1>, <log_key_2>, <log_keytype_2>, <log_value_2>, <log_key_3>, <log_keytype_3>, <log_value_3>)

/ 참고로 이 케이스는 같은 hips_dut 에서 정상 동작하다말다 하는데 원인 파악이 덜 되었음