# product apply - fw max user geodb
Tags: DEVICE.master_brk.ini, DEVICE.p_real_cent.ini, DEVICE.cpp_attacker.ini
table: data/product/hips_fw_table_nation_maxconf_tc.csv

## 기본 Setup
* HIPS:"VS_DUT01"에 최대 사용자 정의 국가 방화벽 테스트를 위한 설정을 수행한다

## 방화벽 테스트케이스(사용자 정의 국가 최대치 추가 상태에서 추가/수정/삭제 시 동작확인)
* HIPS:"VS_DUT01"에 최대 사용자 정의 국가가 추가된 상태에서의 동작을 확인한다 (<user_nation1>, <user_nation2>, <user_nation3>, <user_nation4>, <user_nation_ip1>, <user_nation_ip2>, <nation_direction>, <nation_description1>, <nation_description2>, <nation_description4>, <policy_enable>)
* "ATTACK01"에서 최대 사용자 정의 국가 방화벽 테스트의 탐지 트래픽을 발생시킨다 (<traffic_sip1>, <traffic_sip2>, <traffic_sip4>, <traffic_sport>, <traffic_dport>, <traffic_protocol>)
* HIPS:"VS_DUT01"에서 최대 사용자 정의 국가 방화벽 테스트에 대한 이벤트 로그를 확인한다 (<expect_result1>, <expect_result2>, <expect_result4>, <log_result1>, <log_result2>, <log_result4>, <traffic_sip1>, <traffic_sip2>, <traffic_sip4>, <user_nation1>, <user_nation2>, <user_nation4>, <ndir>)

