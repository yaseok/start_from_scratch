# product apply - fw geodb
Tags: DEVICE.p_real_win.ini, DEVICE.P_W_attacker.ini
table: data/product/w_hips_fw_table_nation.csv

## 정책 파일 load
* P_W_HIPS:"P_W_DUT"에 정책 파일 load 한다

## 기본 Setup
* P_W_HIPS:"P_W_DUT"에 방화벽 테스트를 위한 설정을 수행한다

## 국가 DB geodb
* "P_W_DUT"에서 "rm 'C:/Program Files/AhnLab/EPC/HIPS/LOG/ems/hipssvc.log'"를 실행한다
* "P_W_DUT"에서 "rm 'C:/Program Files/AhnLab/EPC/fw.txt'"를 실행한다
* "P_W_DUT"에서 "rm 'C:/var/fw.txt'"를 실행한다
* P_W_HIPS:"P_W_DUT"에 국가 DB 방화벽 테스트를 위한 정책을 설정 및 적용한다 (<policy_enable>, <user_nation>, <user_nation_ip>, <internal_ip>, <policy_enable>, <nation1>, <nation2>, <nation_direction1>, <nation_direction2>, <nation_description1>, <nation_description2>)
* 10초 동안 대기
* P_W_"P_W_ATTACK"에서 국가 DB 방화벽 테스트의 탐지 트래픽을 발생시킨다 (<traffic_sip1>, <traffic_sip2>, <user_tip>, <traffic_sport1>, <traffic_sport2>, <traffic_dport1>, <traffic_dport2>, <traffic_protocol1>, <traffic_protocol2>)
* "P_W_DUT"에서 "rm 'C:/Program Files/AhnLab/EPC/HIPS/LOG/ems/hipssvc.log'"를 실행한다
* 120초 동안 대기
* "P_W_DUT"에서 "cd 'C:/Program Files/AhnLab/EPC'"를 실행한다
* "P_W_DUT"에서 "./EpcLogV ./HIPS/log/ems/hipssvc.log fw.txt; sleep 3"를 실행한다
* "P_W_DUT"에서 "cp fw.txt c:/var"를 실행한다
* 3초 동안 대기
* P_W_HIPS:"P_W_DUT"에서 국가 DB 방화벽 테스트에 대한 이벤트 로그를 확인한다 (<expect_result1>, <expect_result2>, <log_result1>, <log_result2>, <traffic_sip1>, <traffic_sip2>, <user_tip>, <nation1>, <nation2>, <user_nation>, <ndir1>, <ndir2>)

\* HIPS:"VS_DUT01"에서 국가 DB 방화벽 테스트에 대한 이벤트 로그를 확인한다 (<expect_result1>, <expect_result2>, <log_result1>, <log_result2>, <traffic_sip1>, <traffic_sip2>, <user_tip>, <nation1>, <nation2>, <user_nation>, <ndir1>, <ndir2>)
\* HIPS:"VS_DUT01"에서 TCPDUMP명:"traffic1_dump" 내용을 확인한다 (<expect_result1>, <traffic_sip1>, "$VS_DUT01.ip", "5")
\* HIPS:"VS_DUT01"에서 TCPDUMP명:"traffic1_dump" 내용을 확인한다 (<expect_result2>, <traffic_sip2>, "$VS_DUT01.ip", "5")

\* "VS_DUT01"에서 "traffic1_dump" pcap파일을 제거 한다

