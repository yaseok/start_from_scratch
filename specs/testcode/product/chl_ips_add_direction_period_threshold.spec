# product apply - ips additional direction, period, threshold
Tags: DEVICE.p_real_cent.ini, DEVICE.cpp_attacker.ini
table: data/product/ips_table_predefined_add_3.csv

## 기본 Setup
* HIPS:"VS_DUT01"에 IPS 테스트를 위한 기본 설정을 수행한다


정책 설정
* HIPS:"VS_DUT01"에 IPS additional 탐지방향 및 공격 인정 테스트를 위한 정책을 설정 및 적용한다 (<internal_network_ip>, <sid>, <action>, <block_action>, <severity>, <direction>, <period>, <threshold>, <blockTime>, <raw>, <recommand>, <alarm>)
* "ATTACK01"에서 IPS additional 탐지방향 및 공격 인정 테스트의 탐지 트래픽을 발생시킨다 (<traffic_sip>, <sid>, <traffic_count>, <traffic_delaytime>)
* HIPS:"VS_DUT01"에서 IPS 테스트에 대한 이벤트 로그를 확인한다2 (<expect_result>, <log_result>, <traffic_sip>, <sid>, <action>, <block_action>, <severity>, <ndir>)



