# product apply - ips max internal RULE
Tags: DEVICE.p_real_win.ini, DEVICE.P_W_attacker.ini
table: data/product/w_ips_table_int_net_maxconf_rule.csv

## 정책 파일 load
* P_W_HIPS:"P_W_DUT"에 최대 rule 정책 파일 load 한다

## 기본 Setup
* P_W_HIPS:"P_W_DUT"에 최대 rule 테스트를 위한 설정을 수행한다

## 내부 IP 최대 추가 상태에서의 동작 확인 - max_internal_ip
* "P_W_DUT"에서 "rm 'C:/Program Files/AhnLab/EPC/HIPS/LOG/ems/hipssvc.log'"를 실행한다
* "P_W_DUT"에서 "rm 'C:/Program Files/AhnLab/EPC/log.txt'"를 실행한다
* "P_W_DUT"에서 "rm 'C:/var/log.txt'"를 실행한다

## 트래픽 인가 및 로그 확인- src_ip=70.0.0.1 로그 발생 시 정상 판단.
* "P_W_DUT"에서 "rm 'C:/Program Files/AhnLab/EPC/HIPS/LOG/ems/hipssvc.log'"를 실행한다
* P_W_"P_W_ATTACK"에서 최대값 IPS internal 테스트의 탐지 트래픽을 발생시킨다 (<traffic_sip1>, <traffic_sip2>, <traffic_sip3>, <traffic_sip4>, <sid>)
* 120초 동안 대기
* "P_W_DUT"에서 "cd 'C:/Program Files/AhnLab/EPC'"를 실행한다
* "P_W_DUT"에서 "./EpcLogV ./HIPS/log/ems/hipssvc.log log.txt; sleep 3"를 실행한다
* "P_W_DUT"에서 "cp log.txt c:/var"를 실행한다
* P_W_HIPS:"P_W_DUT"에서 최대값 IPS internal 테스트에 대한 이벤트 로그를 확인한다 (<expect_result1>, <expect_result2>, <expect_result3>, <expect_result4>, <log_result1>, <log_result2>, <log_result3>, <log_result4>, <traffic_sip1>, <traffic_sip2>, <traffic_sip3>, <traffic_sip4>, <sid>, <action>, <block_action>, <severity>)




