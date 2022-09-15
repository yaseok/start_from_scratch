# product apply - ips max exception IP
Tags: DEVICE.p_real_cent.ini, DEVICE.cpp_attacker.ini
table: data/product/ips_table_except_maxconf_tc.csv

## 기본 Setup
* HIPS:"VS_DUT01"에 최대값 IPS 테스트를 위한 기본 설정을 수행한다

## 예외 IP 최대 추가 상태에서의 동작 확인
* HIPS:"VS_DUT01"에 최대 예외 IP가 추가된 상태에서의 동작을 확인한다 (<except_name1>, <except_name2>, <except_name3>, <except_ip1>, <except_ip2>, <description>, <sid>, <action>, <block_action>, <severity>, <direction>, <period>, <threshold>, <blockTime>, <raw>, <recommand>, <alarm>)
* HIPS:"VS_DUT01"에서 TCPDUMP명:"traffic1_dump"으로 인터페이스: "$VS_DUT01.intname"에 대해 TCPDUMP를 수행한다 (<dumpoption1>)
* "ATTACK01"에서 최대값 IPS 테스트의 탐지 트래픽을 발생시킨다 (<traffic_sip1>, <traffic_sip2>, <traffic_sip3>, <traffic_sip4>, <sid>)
* "VS_DUT01"에서 "traffic1_dump" TCPDUMP를 "1"초 후 종료한다
* HIPS:"VS_DUT01"에서 최대값 IPS 테스트에 대한 이벤트 로그를 확인한다 (<expect_result1>, <expect_result2>, <expect_result3>, <expect_result4>, <log_result1>, <log_result2>, <log_result3>, <log_result4>, <traffic_sip1>, <traffic_sip2>, <traffic_sip3>, <traffic_sip4>, <sid>, <action>, <block_action>, <severity>)
\* HIPS:"VS_DUT01"에서 TCPDUMP명:"traffic1_dump" 내용을 확인한다_IPS (<expect_result1>, <traffic_sip1>, "$VS_DUT01.ip", <threshold>)
\* HIPS:"VS_DUT01"에서 TCPDUMP명:"traffic1_dump" 내용을 확인한다_IPS (<expect_result2>, <traffic_sip2>, "$VS_DUT01.ip", <threshold>)
\* HIPS:"VS_DUT01"에서 TCPDUMP명:"traffic1_dump" 내용을 확인한다_IPS (<expect_result3>, <traffic_sip3>, "$VS_DUT01.ip", <threshold>)
\* HIPS:"VS_DUT01"에서 TCPDUMP명:"traffic1_dump" 내용을 확인한다_IPS (<expect_result4>, <traffic_sip4>, "$VS_DUT01.ip", <threshold>)
* "VS_DUT01"에서 "traffic1_dump" pcap파일을 제거 한다