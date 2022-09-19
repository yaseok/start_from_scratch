# product apply - fw basic
Tags: DEVICE.p_real_win.ini, DEVICE.P_W_attacker.ini
table: data/product/hips_fw_table_full.csv

## 정책 파일 load
* P_W_HIPS:"P_W_DUT"에 정책 파일 load 한다

## 기본 Setup 1
* P_W_HIPS:"P_W_DUT"에 방화벽 테스트를 위한 설정을 수행한다

## 기본 방화벽 fw_basic
* "P_W_DUT"에서 "rm 'C:/Program Files/AhnLab/EPC/HIPS/LOG/ems/hipssvc.log'"를 실행한다
* "P_W_DUT"에서 "rm 'C:/Program Files/AhnLab/EPC/fw.txt'"를 실행한다
* "P_W_DUT"에서 "rm 'C:/var/fw.txt'"를 실행한다
* W_HIPS:"P_W_DUT"에 기본 방화벽 테스트를 위한 정책을 설정 및 적용한다 (<policy_enable>, <rule_name1>, <rule_name2>, <action1>, <action2>, <rule_enable1>, <rule_enable2>, <rule_direction1>, <rule_direction2>, <seq_id1>, <seq_id2>, <protocol1>, <protocol2>, <sip1>, <sip2>, <dip1>, <dip2>, <sport1>, <sport2>, <dport1>, <dport2>, <description1>, <description2>)
* P_W_"P_W_ATTACK"에서 기본 방화벽 테스트의 탐지 트래픽을 발생시킨다 (<traffic_sip1>, <traffic_sip2>, <traffic_sport1>, <traffic_sport2>, <traffic_dport1>, <traffic_dport2>, <traffic_protocol1>, <traffic_protocol2>)
* 90초 동안 대기
* "P_W_DUT"에서 "cd 'C:/Program Files/AhnLab/EPC'"를 실행한다
* "P_W_DUT"에서 "./EpcLogV ./HIPS/log/ems/hipssvc.log fw.txt; sleep 3"를 실행한다
* "P_W_DUT"에서 "cp fw.txt c:/var"를 실행한다
* 3초 동안 대기
* P_W_HIPS:"P_W_DUT"에서 기본 방화벽 테스트에 대한 이벤트 로그를 확인한다 (<expect_result1>, <expect_result2>, <log_result1>, <log_result2>, <traffic_sip1>, <traffic_sip2>, <rule_name1>, <rule_name2>, <rule_direction1>, <rule_direction2>)
