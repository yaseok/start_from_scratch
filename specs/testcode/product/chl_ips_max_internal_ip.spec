# product apply - ips max internal IP
Tags: DEVICE.master_brk.ini, DEVICE.p_real_cent.ini, DEVICE.cpp_attacker.ini
table: data/product/ips_table_int_net_maxconf_tc.csv

## 기본 Setup
* HIPS:"VS_DUT01"에 최대값 IPS 테스트를 위한 기본 설정을 수행한다

## 내부 IP 최대 추가 상태에서의 동작 확인
* HIPS:"VS_DUT01"에 최대 내부 IP가 추가된 상태에서의 동작을 확인한다 (<intnet_name1>, <intnet_name2>, <intnet_name3>, <internal_network1>, <internal_network2>, <description>, <sid>, <action>, <block_action>, <severity>, <direction>, <period>, <threshold>, <blockTime>, <raw>, <recommand>, <alarm>)
* "ATTACK01"에서 최대값 IPS 테스트의 탐지 트래픽을 발생시킨다 (<traffic_sip1>, <traffic_sip2>, <traffic_sip3>, <traffic_sip4>, <sid>)
* HIPS:"VS_DUT01"에서 최대값 IPS 테스트에 대한 이벤트 로그를 확인한다 (<expect_result1>, <expect_result2>, <expect_result3>, <expect_result4>, <log_result1>, <log_result2>, <log_result3>, <log_result4>, <traffic_sip1>, <traffic_sip2>, <traffic_sip3>, <traffic_sip4>, <sid>, <action>, <block_action>, <severity>)





