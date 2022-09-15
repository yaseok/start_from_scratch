# 방화벽 최대정책 추가상태 동작확인
Tags: DEVICE.master_brk.ini, DEVICE.p_real_cent.ini, DEVICE.cpp_attacker.ini
table: data/product/hips_fw_table_maxconf_tc.csv

## 방화벽 최대정책 추가 상태에서 동작 검증
* <testname>의 <status> 검증 시나리오 수행

초기상태 설정
* "VS_DUT01"에서 방화벽 정책 초기화를 한다
* "VS_DUT01"에서 FW 이벤트 로그 초기화를 한다

정책설정
* "VS_DUT01"에서 최대값 설정된 방화벽 정책으로 초기화를 한다
* "VS_DUT01"에서 "cd /usr/local/ahnlab/chipsl/tools/"를 실행한다
* "VS_DUT01"에서 "../exec.sh ./hipstest set module off sendlog"를 실행한다

방화벽 정책 최대 추가된 상태에서 신규룰 추가 제한 확인
* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 방화벽 정책에 rule:<rule_name1>, action:<action>, enable:<rule_enable>, direction:<rule_direction>, seq_id:<seq_id1>, protocol:<protocol>, sip:<sip1>, dip:<dip>, sport:<sport>, dport:<dport>, description:<description1>로 추가. xpath는 "body.policy_hips_firewall.rule"이다
* "VS_DUT01"에서 "policy_fw" 정책 암호화 CLI:"../exec.sh ./encrypt enc /var/policy/policy_fw.json"를 한다
* "VS_DUT01"에서 "policy_fw" 정책 적용 CLI:"../exec.sh ./hipstest set policy fw /var/policy/policy_fw.json.enc"을 한다_예상결과 실패
* "VS_DUT01"에서 DB:"../exec.sh ./sqlite3 /usr/local/ahnlab/chipsl/db/fw_policy_curr.db 'pragma key='test'; select * from config;'" 적용결과를 확인한다

방화벽 정책 최대 추가된 상태에서 룰 1개 삭제 후 추가 확인
* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 방화벽 정책에 rule:<rule_name1>을 삭제. xpath는 "body.policy_hips_firewall.rule.[*].rule_name"이다
* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 방화벽 정책에 rule:<rule_name3>을 삭제. xpath는 "body.policy_hips_firewall.rule.[*].rule_name"이다
* "VS_DUT01"에서 "policy_fw" 정책 암호화 CLI:"../exec.sh ./encrypt enc /var/policy/policy_fw.json"를 한다
* "VS_DUT01"에서 "policy_fw" 정책 적용 CLI:"../exec.sh ./hipstest set policy fw /var/policy/policy_fw.json.enc"을 한다
* "VS_DUT01"에서 DB:"../exec.sh ./sqlite3 /usr/local/ahnlab/chipsl/db/fw_policy_curr.db 'pragma key='test'; select * from config;'" 적용결과를 확인한다

* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 방화벽 정책에 rule:<rule_name1>, action:<action>, enable:<rule_enable>, direction:<rule_direction>, seq_id:<seq_id1>, protocol:<protocol>, sip:<sip1>, dip:<dip>, sport:<sport>, dport:<dport>, description:<description1>로 추가. xpath는 "body.policy_hips_firewall.rule"이다
* "VS_DUT01"에서 "policy_fw" 정책 암호화 CLI:"../exec.sh ./encrypt enc /var/policy/policy_fw.json"를 한다
* "VS_DUT01"에서 "policy_fw" 정책 적용 CLI:"../exec.sh ./hipstest set policy fw /var/policy/policy_fw.json.enc"을 한다
* "VS_DUT01"에서 DB:"../exec.sh ./sqlite3 /usr/local/ahnlab/chipsl/db/fw_policy_curr.db 'pragma key='test'; select * from config;'" 적용결과를 확인한다

방화벽 정책 최대 추가된 상태에서 일부 룰 변경
* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 정책 rule:<rule_name2>을 action:<action>, enable:<rule_enable>, direction:<rule_direction>, seq_id:<seq_id2>, protocol:<protocol>, sip:<sip2>, dip:<dip>, sport:<sport>, dport:<dport>, description:<description2> 로 변경을 한다 xpath는 "body.policy_hips_firewall.rule.[*].rule_name" 이다
* "VS_DUT01"에서 "policy_fw" 정책 암호화 CLI:"../exec.sh ./encrypt enc /var/policy/policy_fw.json"를 한다
* "VS_DUT01"에서 "policy_fw" 정책 적용 CLI:"../exec.sh ./hipstest set policy fw /var/policy/policy_fw.json.enc"을 한다
* "VS_DUT01"에서 DB:"../exec.sh ./sqlite3 /usr/local/ahnlab/chipsl/db/fw_policy_curr.db 'pragma key='test'; select * from config;'" 적용결과를 확인한다

* 5초 동안 대기

트래픽 테스트 및 결과확인
* "ATTACK01"에서 hping으로 탐지 트래픽을 발생 한다 조건은 sip:<traffic_sip1>, dip:"$VS_DUT01.ip", sport:<traffic_sport>, dport:<traffic_dport>, protocol:<traffic_protocol1> 이다
* "ATTACK01"에서 hping으로 탐지 트래픽을 발생 한다 조건은 sip:<traffic_sip2>, dip:"$VS_DUT01.ip", sport:<traffic_sport>, dport:<traffic_dport>, protocol:<traffic_protocol1> 이다
* "ATTACK01"에서 hping으로 탐지 트래픽을 발생 한다 조건은 sip:<traffic_sip4>, dip:"$VS_DUT01.ip", sport:<traffic_sport>, dport:<traffic_dport>, protocol:<traffic_protocol2> 이다

* 5초 동안 대기
* "VS_DUT01"에서 "event" 로그 처리결과를 확인 한다 예상결과가 <expect_result1>이고 로그결과는 <log_result1>이다, 추가판단조건 sip:<traffic_sip1>, dip:"$VS_DUT01.ip", block_reason:"fw", rule_name:<rule_name1>, pdir:<rule_direction> json 사용
* "VS_DUT01"에서 "event" 로그 처리결과를 확인 한다 예상결과가 <expect_result2>이고 로그결과는 <log_result2>이다, 추가판단조건 sip:<traffic_sip2>, dip:"$VS_DUT01.ip", block_reason:"fw", rule_name:<rule_name2>, pdir:<rule_direction> json 사용
* "VS_DUT01"에서 "event" 로그 처리결과를 확인 한다 예상결과가 <expect_result4>이고 로그결과는 <log_result4>이다, 추가판단조건 sip:<traffic_sip4>, dip:"$VS_DUT01.ip", block_reason:"fw", rule_name:<rule_name4>, pdir:<rule_direction> json 사용

초기화 수행
* "VS_DUT01"에서 방화벽 정책 초기화를 한다
* "VS_DUT01"에서 FW 이벤트 로그 초기화를 한다


