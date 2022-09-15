# product apply - fw max user geodb rule
Tags: DEVICE.p_real_win.ini, DEVICE.P_W_attacker.ini
table: data/product/w_hips_fw_table_nation_maxconf_rule.csv

## 정책 파일 load
* P_W_HIPS:"P_W_DUT"에 최대 user geo rule 정책 파일 load 한다

## 기본 Setup
* P_W_HIPS:"P_W_DUT"에 최대 user geo rule 테스트를 위한 설정을 수행한다

## 방화벽 테스트케이스(사용자 정의 국가 최대치 추가 상태에서 추가/수정/삭제 시 동작확인) - max_user_geodb
* "P_W_DUT"에서 "rm 'C:/Program Files/AhnLab/EPC/HIPS/LOG/ems/hipssvc.log'"를 실행한다
* "P_W_DUT"에서 "rm 'C:/Program Files/AhnLab/EPC/fw.txt'"를 실행한다
* "P_W_DUT"에서 "rm 'C:/var/fw.txt'"를 실행한다
사용자정의 국가를 방화벽 룰에 추가: nation1: 신규추가 국가, nation2: 변경한 국가, nation3: 기존에 있던 사용자 정의 국가
* "P_W_DUT"에서 "policy_fw" 설정파일 "c:/var/policy/data/firewall.txt" 방화벽 정책에 nation:<user_nation1>, direction:<nation_direction>, description:<nation_description1>로 추가. xpath는 "body.policy_hips_firewall.block_nation"이다
* "P_W_DUT"에서 "policy_fw" 설정파일 "c:/var/policy/data/firewall.txt" 방화벽 정책에 nation:<user_nation2>, direction:<nation_direction>, description:<nation_description2>로 추가. xpath는 "body.policy_hips_firewall.block_nation"이다
* "P_W_DUT"에서 "policy_fw" 설정파일 "c:/var/policy/data/firewall.txt" 방화벽 정책에 nation:<user_nation4>, direction:<nation_direction>, description:<nation_description4>로 추가. xpath는 "body.policy_hips_firewall.block_nation"이다
방화벽 정책을 적용시키기 위해 policy_fw.json 암호화 및 정책적용
* "P_W_DUT"에서 "cd c:/var/policy"를 실행한다
* P_W_"P_W_DUT"에서 "firewall" 정책 암호화 CLI:"./hipstest file plyenc ./data/firewall.txt ./work/firewall.txt"를 한다
* P_W_"P_W_DUT"에서 "firewall" 정책 적용 CLI:"./hipstest set policy fw ./work/firewall.txt"을 한다
* 60초 동안 대기
* P_W_"P_W_ATTACK"에서 최대 사용자 정의 국가 방화벽 테스트의 탐지 트래픽을 발생시킨다 (<traffic_sip1>, <traffic_sip2>, <traffic_sip4>, <traffic_sport>, <traffic_dport>, <traffic_protocol>)
* 90초 동안 대기
* "P_W_DUT"에서 "cd 'C:/Program Files/AhnLab/EPC'"를 실행한다
* "P_W_DUT"에서 "./EpcLogV ./HIPS/log/ems/hipssvc.log fw.txt; sleep 3"를 실행한다
* "P_W_DUT"에서 "cp fw.txt c:/var"를 실행한다
* P_W_HIPS:"P_W_DUT"에서 최대 사용자 정의 국가 방화벽 테스트 RULE에 대한 이벤트 로그를 확인한다 (<expect_result1>, <expect_result2>, <expect_result4>, <log_result1>, <log_result2>, <log_result4>, <traffic_sip1>, <traffic_sip2>, <traffic_sip4>, <user_nation1>, <user_nation2>, <user_nation4>, <ndir>)
