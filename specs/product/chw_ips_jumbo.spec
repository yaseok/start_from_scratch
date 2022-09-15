# product apply - JUMBO
Tags: DEVICE.p_real_win.ini, DEVICE.P_W_attacker.ini
table: data/product/w_ips_table_predefined6.csv

## 정책 파일 load
* P_W_HIPS:"P_W_DUT"에 정책 파일 load 한다

## 기본 Setup
* P_W_HIPS:"P_W_DUT"에 IPS 테스트를 위한 설정을 수행한다

## jumbo 정책 설정, 패킷 인가, 로그 확인 
* "P_W_DUT"에서 "rm 'C:/Program Files/AhnLab/EPC/HIPS/LOG/ems/hipssvc.log'"를 실행한다
* "P_W_DUT"에서 "rm 'C:/Program Files/AhnLab/EPC/log.txt'"를 실행한다
* "P_W_DUT"에서 "rm 'C:/var/log.txt'"를 실행한다
* P_W_HIPS:"P_W_DUT"에 JUMBO 테스트를 위한 정책을 설정 및 적용한다 (<sid>, <action>, <block_action>, <severity>, <direction>, <period>, <threshold>, <blockTime>, <raw>, <recommand>, <alarm>)
* 60초 동안 대기
* "P_W_DUT"에서 "rm 'C:/Program Files/AhnLab/EPC/HIPS/LOG/ems/hipssvc.log'"를 실행한다
* P_W_HIPS:"P_W_DUT"에 JUMBO 테스트를 위한 탐지 트래픽을 인가한다.
* 120초 동안 대기
* "P_W_DUT"에서 "cd 'C:/Program Files/AhnLab/EPC'"를 실행한다
* "P_W_DUT"에서 "./EpcLogV ./HIPS/log/ems/hipssvc.log log.txt; sleep 3"를 실행한다
* "P_W_DUT"에서 "cp log.txt c:/var"를 실행한다
* P_W_HIPS:"P_W_DUT"에서 JUMBO 테스트에 대한 이벤트 로그를 확인한다 (<expect_result>, <log_result>, <traffic_sip>, <sid>, <action>, <block_action>, <detect_bytes>, <ndir>)

