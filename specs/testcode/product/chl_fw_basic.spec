# product apply - fw basic
Tags: DEVICE.p_real_cent.ini, DEVICE.cpp_attacker.ini
table: data/product/hips_fw_table_full.csv

## 기본 Setup
* HIPS:"VS_DUT01"에 기본 방화벽 테스트를 위한 설정을 수행한다

## 사용여부, 방향, seq id, 프로토콜 조합, 처리방법
* HIPS:"VS_DUT01"에 기본 방화벽 테스트를 위한 정책을 설정 및 적용한다 (<policy_enable>, <rule_name1>, <rule_name2>, <action1>, <action2>, <rule_enable1>, <rule_enable2>, <rule_direction1>, <rule_direction2>, <seq_id1>, <seq_id2>, <protocol1>, <protocol2>, <sip1>, <sip2>, <dip1>, <dip2>, <sport1>, <sport2>, <dport1>, <dport2>, <description1>, <description2>)
* "ATTACK01"에서 기본 방화벽 테스트의 탐지 트래픽을 발생시킨다 (<traffic_sip1>, <traffic_sip2>, <traffic_sport1>, <traffic_sport2>, <traffic_dport1>, <traffic_dport2>, <traffic_protocol1>, <traffic_protocol2>)
* HIPS:"VS_DUT01"에서 기본 방화벽 테스트에 대한 이벤트 로그를 확인한다 (<expect_result1>, <expect_result2>, <log_result1>, <log_result2>, <traffic_sip1>, <traffic_sip2>, <rule_name1>, <rule_name2>, <rule_direction1>, <rule_direction2>)
