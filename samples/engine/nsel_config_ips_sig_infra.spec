# engine apply - ips infra signature action, blockaction

Tags: DEVICE.real_cent.ini, DEVICE.nsel_attacker.ini
table: data/engine/table_config_ips_sig_infra.csv

## 기본 Setup
* HIPS:"VS_DUT01"에 IPS 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다

## IPS action, blockAction - String type의 설정을 변경하면서 결과를 Array key로 확인하는 케이스

* HIPS:"VS_DUT01"에서 엔진의 설정을 변경하고 적용한다 (String Type, <menu>, <xpath>, <path_local>, <path_remote_1>, <path_remote_2>, <value>)
* HIPS:"VS_DUT01"에서 엔진의 설정을 확인한다 (Array Type, <anse_cmd>, <result_path>, <result_key_1>, <result_key_2>, <result_value_1>, <result_value_2>, <result_keytype_1>, <result_keytype_2>)
* "ATTACK01"에서 "$VS_DUT01.ip"로 Signature가 "GET /TEST.html"이고 TCP 목적지 포트가 "80"인 패킷을 전송한다
* HIPS:"VS_DUT01"에서 엔진의 이벤트 로그를 확인한다 (<log_key_1>, <log_keytype_1>, <log_value_1>, <log_key_2>, <log_keytype_2>, <log_value_2>, <log_key_3>, <log_keytype_3>, <log_value_3>)