# fw 5tuple

Tags: DEVICE.real_win.ini, DEVICE.nsew_attacker.ini
table: data/engine/w_table_config_fw_5tuple.csv

## NSEW 설치
* W_HIPS:"W_DUT"에 NSEW를 설치한다.

## 기본 Setup
* W_HIPS:"W_DUT"에 방화벽 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다

## fw 5tuple

* "W_DUT"에서 "policy_hips_firewall" 설정파일 "/tmp/policy_hips_firewall.json" 정책 rule:<rule_name1>을 action:<action1>, enable:<rule_enable1>, direction:<rule_direction1>, seq_id:<seq_id1>, protocol:<protocol1>, sip:<sip1>, dip:<dip1>, sport:<sport1>, dport:<dport1>, description:<description1> 로 변경을 한다 xpath는 "policy_hips_firewall.rule.[*].rule_name" 이다
* W_HIPS:"W_DUT"에 방화벽 테스트를 위한 설정 파일을 적용한다.
* W_HIPS:"W_DUT"에서 로그 초기화
* "ATTACK"에서 "$W_DUT.ip"로 Signature가 "GET /TEST.html"이고 TCP 출발지 포트 1000 및 목적지 포트가 "80"인 패킷을 전송함
* W_HIPS:"W_DUT"에서 엔진의 이벤트 로그를 확인한다 (<logcheck>, <log_key_1>, <log_keytype_1>, <log_value_1>, <log_key_2>, <log_keytype_2>, <log_value_2>, <log_key_3>, <log_keytype_3>, <log_value_3>)