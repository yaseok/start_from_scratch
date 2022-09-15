# product apply - fw max rule
Tags: DEVICE.p_real_cent.ini, DEVICE.cpp_attacker.ini
table: data/product/hips_fw_table_maxconf_tc.csv

## 기본 Setup
* HIPS:"VS_DUT01"에 최대 정책 방화벽 테스트를 위한 설정을 수행한다

## 최대 정책이 추가된 상태에서의 정상 동작 여부 및 탐지 확인
* HIPS:"VS_DUT01"에 최대 정책이 추가된 상태에서의 동작을 확인한다 (<rule_name1>, <rule_name2>, <rule_name3>, <action>, <rule_enable>, <rule_direction>, <seq_id1>, <seq_id2>, <protocol>, <sip1>, <sip2>, <dip>, <sport>, <dport>, <description1>, <description2>)
* HIPS:"VS_DUT01"에서 TCPDUMP명:"traffic1_dump"으로 인터페이스: "$VS_DUT01.intname"에 대해 TCPDUMP를 수행한다 (<dumpoption1>)
* "ATTACK01"에서 최대 정책 방화벽 테스트의 탐지 트래픽을 발생시킨다 (<traffic_sip1>, <traffic_sip2>, <traffic_sip4>, <traffic_sport>, <traffic_dport>, <traffic_protocol1>, <traffic_protocol2>)
* "VS_DUT01"에서 "traffic1_dump" TCPDUMP를 "1"초 후 종료한다

* HIPS:"VS_DUT01"에서 최대 정책 방화벽 테스트에 대한 이벤트 로그를 확인한다 (<expect_result1>, <expect_result2>, <expect_result4>, <log_result1>, <log_result2>, <log_result4>, <traffic_sip1>, <traffic_sip2>, <traffic_sip4>, <rule_name1>, <rule_name2>, <rule_name4>, <rule_direction>)
\* HIPS:"VS_DUT01"에서 TCPDUMP명:"traffic1_dump" 내용을 확인한다 (<expect_result1>, <traffic_sip1>, "$VS_DUT01.ip", "5")
\* HIPS:"VS_DUT01"에서 TCPDUMP명:"traffic1_dump" 내용을 확인한다 (<expect_result2>, <traffic_sip2>, "$VS_DUT01.ip", "5")
\* HIPS:"VS_DUT01"에서 TCPDUMP명:"traffic1_dump" 내용을 확인한다 (<expect_result4>, <traffic_sip4>, "$VS_DUT01.ip", "5")
* "VS_DUT01"에서 "traffic1_dump" pcap파일을 제거 한다


