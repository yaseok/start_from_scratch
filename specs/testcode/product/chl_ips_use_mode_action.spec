# product apply - ips use, mode, action
Tags: DEVICE.p_real_cent.ini, DEVICE.cpp_attacker.ini
table: data/product/ips_table_predefined4.csv

## IPS TC 수행
* HIPS:"VS_DUT01"에 IPS 테스트를 위한 기본 설정을 수행한다

## 사용여부, 모드변환, 대응방법 테스트
* HIPS:"VS_DUT01"에 IPS 사용여부 및 모드, 대응방법 테스트를 위한 정책을 설정 및 적용한다 (<engine_mode>, <policy_enable>, <ips_mode>, <sid>, <action>, <block_action>, <severity>, <direction>, <period>, <threshold>, <blockTime>, <raw>, <recommand>, <alarm>)
* "ATTACK01"에서 IPS 사용여부 및 모드, 대응방법 테스트의 탐지 트래픽을 발생시킨다 (<traffic_sip>, <sid>)
* HIPS:"VS_DUT01"에서 IPS 테스트에 대한 이벤트 로그를 확인한다1 (<expect_result>, <log_result>, <traffic_sip>, <sid>, <action>, <block_action>, <severity>)





