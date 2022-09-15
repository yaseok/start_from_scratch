# product apply - fw max user geodb ip
Tags: DEVICE.p_real_win.ini, DEVICE.P_W_attacker.ini
table: data/product/w_hips_fw_table_nation_maxconf_tc.csv

## 정책 파일 load
* P_W_HIPS:"P_W_DUT"에 정책 파일 load 한다

## 기본 Setup
* P_W_HIPS:"P_W_DUT"에 방화벽 테스트를 위한 설정을 수행한다

## 방화벽 테스트케이스(사용자 정의 국가 최대치 추가 상태에서 추가/수정/삭제 시 동작확인) - max_user_geodb
* "P_W_DUT"에서 "rm 'C:/Program Files/AhnLab/EPC/HIPS/LOG/ems/hipssvc.log'"를 실행한다
* "P_W_DUT"에서 "rm 'C:/Program Files/AhnLab/EPC/fw.txt'"를 실행한다
* "P_W_DUT"에서 "rm 'C:/var/fw.txt'"를 실행한다
* P_W_HIPS:"P_W_DUT"에 최대 사용자 정의 국가가 추가된 상태에서의 동작을 확인한다 (<user_nation1>, <user_nation2>, <user_nation3>, <user_nation4>, <user_nation_ip1>, <user_nation_ip2>, <nation_direction>, <nation_description1>, <nation_description2>, <nation_description4>, <policy_enable>)
* P_W_"P_W_ATTACK"에서 최대 사용자 정의 국가 방화벽 테스트의 탐지 트래픽을 발생시킨다 (<traffic_sip1>, <traffic_sip2>, <traffic_sip4>, <traffic_sport>, <traffic_dport>, <traffic_protocol>)
* 90초 동안 대기
* "P_W_DUT"에서 "cd 'C:/Program Files/AhnLab/EPC'"를 실행한다
* "P_W_DUT"에서 "./EpcLogV ./HIPS/log/ems/hipssvc.log fw.txt; sleep 3"를 실행한다
* "P_W_DUT"에서 "cp fw.txt c:/var"를 실행한다
* P_W_HIPS:"P_W_DUT"에서 최대 사용자 정의 국가 방화벽 테스트에 대한 이벤트 로그를 확인한다 (<expect_result1>, <expect_result2>, <expect_result4>, <log_result1>, <log_result2>, <log_result4>, <traffic_sip1>, <traffic_sip2>, <traffic_sip4>, <user_nation1>, <user_nation2>, <user_nation4>, <ndir>)
