# product apply - ips exception IP
Tags: DEVICE.p_real_cent.ini, DEVICE.cpp_attacker.ini
table: data/product/ips_table_predefined5.csv

## 기본 Setup
* HIPS:"VS_DUT01"에 IPS 테스트를 위한 기본 설정을 수행한다

## 예외 IP
* HIPS:"VS_DUT01"에 IPS 예외 IP 테스트를 위한 정책을 설정 및 적용한다 (<except_ip>, <sid>, <action>, <block_action>, <severity>, <direction>, <period>, <threshold>, <blockTime>, <raw>, <recommand>, <alarm>)
* "ATTACK01"에서 IPS 예외 IP 테스트의 탐지 트래픽을 발생시킨다 (<traffic_sip>, <sid>)
* HIPS:"VS_DUT01"에서 IPS 테스트에 대한 이벤트 로그를 확인한다1 (<expect_result>, <log_result>, <traffic_sip>, <sid>, <action>, <block_action>, <severity>)