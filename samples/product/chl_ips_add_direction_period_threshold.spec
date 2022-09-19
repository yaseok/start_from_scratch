# product apply - ips additional direction, period, threshold
Tags: DEVICE.p_real_cent.ini, DEVICE.cpp_attacker.ini
table: data/product/ips_table_predefined_add_3.csv

## 기본 Setup
* HIPS:"VS_DUT01"에 IPS 테스트를 위한 기본 설정을 수행한다


정책 설정
* HIPS:"VS_DUT01"에 IPS additional 탐지방향 및 공격 인정 테스트를 위한 정책을 설정 및 적용한다 (<internal_network_ip>, <sid>, <action>, <block_action>, <severity>, <direction>, <period>, <threshold>, <blockTime>, <raw>, <recommand>, <alarm>)
* HIPS:"VS_DUT01"에서 TCPDUMP명:"traffic1_dump"으로 인터페이스: "$VS_DUT01.intname"에 대해 TCPDUMP를 수행한다 (<dumpoption1>)
* "ATTACK01"에서 IPS additional 탐지방향 및 공격 인정 테스트의 탐지 트래픽을 발생시킨다 (<traffic_sip>, <sid>, <traffic_count>, <traffic_delaytime>)
* "VS_DUT01"에서 "traffic1_dump" TCPDUMP를 "1"초 후 종료한다
* HIPS:"VS_DUT01"에서 IPS 테스트에 대한 이벤트 로그를 확인한다2 (<expect_result>, <log_result>, <traffic_sip>, <sid>, <action>, <block_action>, <severity>, <ndir>)

\* HIPS:"VS_DUT01"에서 TCPDUMP명:"traffic1_dump" 내용을 확인한다_IPS (<expect_result>, <traffic_sip>, "$VS_DUT01.ip", <threshold>)
* "VS_DUT01"에서 "traffic1_dump" pcap파일을 제거 한다


