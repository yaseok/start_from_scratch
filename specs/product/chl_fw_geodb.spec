# product apply - fw geodb
Tags: DEVICE.p_real_cent.ini, DEVICE.cpp_attacker.ini
table: data/product/hips_fw_table_nation.csv

## 기본 Setup
* HIPS:"VS_DUT01"에 국가 DB 방화벽 테스트를 위한 설정을 수행한다

## 국가 DB
* HIPS:"VS_DUT01"에 국가 DB 방화벽 테스트를 위한 정책을 설정 및 적용한다 (<user_nation>, <user_nation_ip>, <internal_ip>, <policy_enable>, <nation1>, <nation2>, <nation_direction1>, <nation_direction2>, <nation_description1>, <nation_description2>)
* HIPS:"VS_DUT01"에서 TCPDUMP명:"traffic1_dump"으로 인터페이스: "$VS_DUT01.intname"에 대해 TCPDUMP를 수행한다 (<dumpoption1>)
* "ATTACK01"에서 국가 DB 방화벽 테스트의 탐지 트래픽을 발생시킨다 (<traffic_sip1>, <traffic_sip2>, <user_tip>, <traffic_sport1>, <traffic_sport2>, <traffic_dport1>, <traffic_dport2>, <traffic_protocol1>, <traffic_protocol2>)
* "VS_DUT01"에서 "traffic1_dump" TCPDUMP를 "1"초 후 종료한다

* HIPS:"VS_DUT01"에서 국가 DB 방화벽 테스트에 대한 이벤트 로그를 확인한다 (<expect_result1>, <expect_result2>, <log_result1>, <log_result2>, <traffic_sip1>, <traffic_sip2>, <user_tip>, <nation1>, <nation2>, <user_nation>, <ndir1>, <ndir2>)
\* HIPS:"VS_DUT01"에서 TCPDUMP명:"traffic1_dump" 내용을 확인한다 (<expect_result1>, <traffic_sip1>, "$VS_DUT01.ip", "5")
\* HIPS:"VS_DUT01"에서 TCPDUMP명:"traffic1_dump" 내용을 확인한다 (<expect_result2>, <traffic_sip2>, "$VS_DUT01.ip", "5")

* "VS_DUT01"에서 "traffic1_dump" pcap파일을 제거 한다

