# product apply - fw max ip
Tags: DEVICE.p_real_win.ini, DEVICE.P_W_attacker.ini
table: data/product/w_hips_fw_table_maxconf_add_modi_del.csv


## 정책 파일 load
* P_W_HIPS:"P_W_DUT"에 정책 파일 load 한다

## 기본 Setup
* P_W_HIPS:"P_W_DUT"에 방화벽 테스트를 위한 설정을 수행한다

## 최대 정책이 추가된 상태에서의 정상 동작 여부 및 탐지 확인 -FW max ip
* "P_W_DUT"에서 "rm 'C:/Program Files/AhnLab/EPC/HIPS/LOG/ems/hipssvc.log'"를 실행한다
* "P_W_DUT"에서 "rm 'C:/Program Files/AhnLab/EPC/fw.txt'"를 실행한다
* "P_W_DUT"에서 "rm 'C:/var/fw.txt'"를 실행한다
* P_W_HIPS:"P_W_DUT"에 방화벽 최대 정책이 추가된 상태에서의 동작을 확인한다 (<rule_name1>, <rule_name2>, <rule_name3>, <rule_name4>, <action>, <rule_enable>, <rule_direction>, <seq_id1>, <seq_id2>, <seq_id3>, <seq_id4>, <protocol>, <sip1>, <sip2>, <sip3>, <sip4>, <dip>, <sport>, <dport>, <description1>, <description2>)

## 방화벽 최대 ip 삭제
* "P_W_DUT"에서 "policy_fw" 설정파일 "c:/var/policy/data/firewall.txt" 방화벽 정책에 rule:<rule_name1>을 삭제. xpath는 "body.policy_hips_firewall.rule.[*].rule_name"이다
* "P_W_DUT"에서 "policy_fw" 설정파일 "c:/var/policy/data/firewall.txt" 방화벽 정책에 rule:<rule_name2>을 삭제. xpath는 "body.policy_hips_firewall.rule.[*].rule_name"이다
* W_HIPS:"P_W_DUT"에 기본 방화벽 테스트를 위한 설정을 수행한다

## 방화벽 최대 ip 수정
* "P_W_DUT"에서 "policy_fw" 설정파일 "c:/var/policy/data/firewall.txt" 정책 rule:<rule_name3>을 action:<action>, enable:<rule_enable>, direction:<rule_direction>, seq_id:<seq_id2>, protocol:<protocol>, sip:<sip1>, dip:<dip>, sport:<sport>, dport:<dport>, description:<description2> 로 변경을 한다 xpath는 "body.policy_hips_firewall.rule.[*].rule_name" 이다
* W_HIPS:"P_W_DUT"에 기본 방화벽 테스트를 위한 설정을 수행한다

## 트래픽 인가 및 로그 확인 -이벤트 로그 rule_name=rule103, src_ip=51.0.100.1 발생시 룰 수정,삭제 정상 판단.
* P_W_"P_W_ATTACK"에서 최대 정책 방화벽 테스트의 탐지 트래픽을 발생시킨다 (<traffic_sip1>, <traffic_sip2>, <traffic_sip4>, <traffic_sport>, <traffic_dport>, <traffic_protocol1>, <traffic_protocol2>)
* 90초 동안 대기
* "P_W_DUT"에서 "cd 'C:/Program Files/AhnLab/EPC'"를 실행한다
* "P_W_DUT"에서 "./EpcLogV ./HIPS/log/ems/hipssvc.log fw.txt; sleep 3"를 실행한다
* "P_W_DUT"에서 "cp fw.txt c:/var"를 실행한다
* P_W_HIPS:"p_w_DUT"에서 최대 정책 방화벽 수정 및 삭제 테스트에 대한 이벤트 로그를 확인한다 (<expect_result1>, <expect_result2>, <expect_result4>, <log_result1>, <log_result2>, <log_result4>, <traffic_sip1>, <traffic_sip2>, <traffic_sip4>, <rule_name1>, <rule_name2>, <rule_name3>, <rule_direction>)



