# product apply - fw max rule
Tags: DEVICE.p_real_win.ini, DEVICE.P_W_attacker.ini
table: data/product/w_hips_fw_table_max_rule.csv

## 정책 파일 load
* P_W_HIPS:"P_W_DUT"에 최대 rule 정책 파일 load 한다

## 기본 Setup
* P_W_HIPS:"P_W_DUT"에 최대 rule 테스트를 위한 설정을 수행한다

## 기존 이벤트 로그 삭제
* "P_W_DUT"에서 "rm 'C:/Program Files/AhnLab/EPC/HIPS/LOG/ems/hipssvc.log'"를 실행한다
* "P_W_DUT"에서 "rm 'C:/Program Files/AhnLab/EPC/fw.txt'"를 실행한다
* "P_W_DUT"에서 "rm 'C:/var/fw.txt'"를 실행한다

## 트래픽 인가 및 로그 확인 -이벤트 로그 rule_name=rule103, src_ip=51.0.100.1 발생시 최대 룰 정상 판단.
* P_W_"P_W_ATTACK"에서 최대 정책 방화벽 테스트의 탐지 트래픽을 발생시킨다 (<traffic_sip1>, <traffic_sip2>, <traffic_sip4>, <traffic_sport>, <traffic_dport>, <traffic_protocol1>, <traffic_protocol2>)
* 90초 동안 대기
* "P_W_DUT"에서 "cd 'C:/Program Files/AhnLab/EPC'"를 실행한다
* "P_W_DUT"에서 "./EpcLogV ./HIPS/log/ems/hipssvc.log fw.txt; sleep 3"를 실행한다
* "P_W_DUT"에서 "cp fw.txt c:/var"를 실행한다
* P_W_HIPS:"p_w_DUT"에서 최대 정책 방화벽 수정 및 삭제 테스트에 대한 이벤트 로그를 확인한다 (<expect_result1>, <expect_result2>, <expect_result4>, <log_result1>, <log_result2>, <log_result4>, <traffic_sip1>, <traffic_sip2>, <traffic_sip4>, <rule_name1>, <rule_name2>, <rule_name3>, <rule_direction>)



