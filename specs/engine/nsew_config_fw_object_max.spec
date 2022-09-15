# 방화벽 정책 - 객체별 최대 개수 적용 케이스
Tags: DEVICE.real_win.ini, DEVICE.nsew_attacker.ini
table: data/engine/w_table_config_fw_object_max.csv

## NSEW 설치
* W_HIPS:"W_DUT"에 NSEW를 설치한다.

## 기본 Setup
* W_HIPS:"W_DUT"에 방화벽 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다

## 방화벽 정책 객체 유형별 최대 개수 적용 케이스
최대 개수: 객체당 255개
sip/dip/sport/dport = 255/1/1/1
sip/dip/sport/dport = 1/1/1/1
sip/dip/sport/dport = 1/255/1/1
sip/dip/sport/dport = 1/1/1/1
sip/dip/sport/dport = 1/1/1/255
sip/dip/sport/dport = 1/1/1/1
sip/dip/sport/dport = 1/1/255/1
sip/dip/sport/dport = 1/1/1/1
sip/dip/sport/dport = 255/1/1/1 (하위 4가지 케이스는 NSEL-1725 해결되면 추가 필요함. 현재 미반영)
sip/dip/sport/dport = 255/255/1/1 
sip/dip/sport/dport = 255/255/255/1 
sip/dip/sport/dport = 255/255/255/255 

* W_HIPS:"W_DUT"에서 엔진의 설정을 변경하고 적용한다 (String Type, <menu>, <xpath>, <path_local>, <path_remote_1>, <path_remote_2>, <value>)
* "W_DUT"에서 "cat /tmp/policy_hips_firewall.json"를 실행한다
* W_HIPS:"W_DUT"에서 엔진의 설정을 확인한다 (Object Type, <anse_cmd>, <result_path>, <result_value>)
* "ATTACK"에서 "$W_DUT.ip"로 Signature가 "GET /TEST.html"이고 TCP 목적지 포트가 "80"인 패킷을 전송한다
* W_HIPS:"W_DUT"에서 엔진의 이벤트 로그를 확인한다 (<logcheck>, <log_key_1>, <log_keytype_1>, <log_value_1>, <log_key_2>, <log_keytype_2>, <log_value_2>, <log_key_3>, <log_keytype_3>, <log_value_3>)