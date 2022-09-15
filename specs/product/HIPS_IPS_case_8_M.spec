# ips 테스트(예외 IP 최대 추가상태에서 동작확인)
Tags: DEVICE.master_brk.ini, DEVICE.p_real_cent.ini, DEVICE.cpp_attacker.ini
table: data/product/ips_table_except_maxconf_tc.csv

## IPS TC 수행
* <testname>의 <status> 검증 시나리오 수행

초기상태 설정
* "VS_DUT01"에서 IPS 정책 초기화를 한다
* "VS_DUT01"에서 IPS 이벤트 로그 초기화를 한다
* "VS_DUT01"에서 내부 네트워크, 예외IP, 사용자정의 국가 최대값 설정된 AGENT 정책으로 초기화를 한다

예외 IP 설정
AGENT 정책 최대 추가된 상태에서 룰 1개 삭제 후 추가 확인
예외IP 1개 삭제 및 적용
* "VS_DUT01"에서 "policy_agent" 설정파일 "/var/policy/policy_agent.json" Agent 정책에 name:<except_name3>을 삭제. xpath는 "body.policy_hips_agent.except_ip.[*].name"이다
* "VS_DUT01"에서 "policy_agent" 정책 암호화 CLI:"../exec.sh ./encrypt enc /var/policy/policy_agent.json"를 한다
* "VS_DUT01"에서 "policy_agent" 정책 적용 CLI:"../exec.sh ./hipstest set policy agent /var/policy/policy_agent.json.enc"을 한다
* "VS_DUT01"에서 DB:"../exec.sh ./sqlite3 /usr/local/ahnlab/chipsl/db/agent_policy_curr.db 'pragma key='test'; select * from config;'" 적용결과를 확인한다

예외IP 1개 추가 및 적용
* "VS_DUT01"에서 "policy_agent" 설정파일 "/var/policy/policy_agent.json" Agent 정책에 rule:"except_ip", name:<except_name1>, ip:<except_ip1>, description<description>로 추가. xpath는 "body.policy_hips_agent.except_ip"이다
* "VS_DUT01"에서 "policy_agent" 정책 암호화 CLI:"../exec.sh ./encrypt enc /var/policy/policy_agent.json"를 한다
* "VS_DUT01"에서 "policy_agent" 정책 적용 CLI:"../exec.sh ./hipstest set policy agent /var/policy/policy_agent.json.enc"을 한다
* "VS_DUT01"에서 DB:"../exec.sh ./sqlite3 /usr/local/ahnlab/chipsl/db/agent_policy_curr.db 'pragma key='test'; select * from config;'" 적용결과를 확인한다

AGENT 정책 최대 추가된 상태에서 일부 룰 변경
* "VS_DUT01"에서 "policy_agent" 설정파일 "/var/policy/policy_agent.json" 정책 "name":<except_name2>을 ip:<except_ip2> 로 변경을 한다 xpath는 "body.policy_hips_agent.except_ip.[*].name" 이다
policy_agent.json 암호화 및 정책적용
* "VS_DUT01"에서 "policy_agent" 정책 암호화 CLI:"../exec.sh ./encrypt enc /var/policy/policy_agent.json"를 한다
* "VS_DUT01"에서 "policy_agent" 정책 적용 CLI:"../exec.sh ./hipstest set policy agent /var/policy/policy_agent.json.enc"을 한다
* "VS_DUT01"에서 DB:"../exec.sh ./sqlite3 /usr/local/ahnlab/chipsl/db/agent_policy_curr.db 'pragma key='test'; select * from config;'" 적용결과를 확인한다

기본정책 값에 IPS 사용, mode deny로 설정되어 있다.
IPS 정책 설정
* "VS_DUT01"에서 "policy_mgmt" 설정파일 "/var/policy/policy_mgmt.json" 정책 "predefined" sid:<sid>을 action:<action>, blockAction:<block_action>, severity:<severity>, direction:<direction>, period:<period>, threshold:<threshold>, blockTime:<blockTime>, raw:<raw>, recommand:<recommand>, alarm:<alarm> 로 변경을 한다 xpath는 "body.policy_hips_ips_mgmt.predefined.default.[*].sid" 이다

policy_mgmt.json 암호화 및 적용
* "VS_DUT01"에서 "policy_mgmt" 정책 암호화 CLI:"../exec.sh ./encrypt enc /var/policy/policy_mgmt.json"를 한다
* "VS_DUT01"에서 "policy_mgmt" 정책 적용 CLI:"../exec.sh ./hipstest set policy mgmt /var/policy/policy_mgmt.json.enc"을 한다
* "VS_DUT01"에서 CLI:"../exec.sh ./hipstest get policy mgmt" 적용결과를 확인한다

트래픽 테스트 및 결과확인
* "ATTACK01"에서 FPG rule 파일 설정(기본시그니처용)
예외처리 출발지 IP 트래픽
traffic_sip1: 신규추가 예외IP, traffic_sip2: 변경한 예외IP, traffic_sip4: 기존에 있던 예외IP
* "ATTACK01"에서 FPG로 탐지 트래픽을 발생 한다 조건은 sip:<traffic_sip1>, dip:"$VS_DUT01.ip", sid:<sid>이다
* "ATTACK01"에서 FPG로 탐지 트래픽을 발생 한다 조건은 sip:<traffic_sip2>, dip:"$VS_DUT01.ip", sid:<sid>이다
* "ATTACK01"에서 FPG로 탐지 트래픽을 발생 한다 조건은 sip:<traffic_sip4>, dip:"$VS_DUT01.ip", sid:<sid>이다

탐지 대상 출발지IP 트래픽
* "ATTACK01"에서 FPG로 탐지 트래픽을 발생 한다 조건은 sip:<traffic_sip3>, dip:"$VS_DUT01.ip", sid:<sid>이다
* 5초 동안 대기
* "VS_DUT01"에서 "event" 로그 처리결과를 확인 한다 예상결과가 <expect_result1>이고 로그결과는 <log_result1>이다, 추가판단조건 sip:<traffic_sip1>, dip:"$VS_DUT01.ip", attackid:<sid>, action:<action>, blockaction:<block_action>, priority<severity> json 사용
* "VS_DUT01"에서 "event" 로그 처리결과를 확인 한다 예상결과가 <expect_result2>이고 로그결과는 <log_result2>이다, 추가판단조건 sip:<traffic_sip2>, dip:"$VS_DUT01.ip", attackid:<sid>, action:<action>, blockaction:<block_action>, priority<severity> json 사용
* "VS_DUT01"에서 "event" 로그 처리결과를 확인 한다 예상결과가 <expect_result3>이고 로그결과는 <log_result3>이다, 추가판단조건 sip:<traffic_sip3>, dip:"$VS_DUT01.ip", attackid:<sid>, action:<action>, blockaction:<block_action>, priority<severity> json 사용
* "VS_DUT01"에서 "event" 로그 처리결과를 확인 한다 예상결과가 <expect_result4>이고 로그결과는 <log_result4>이다, 추가판단조건 sip:<traffic_sip4>, dip:"$VS_DUT01.ip", attackid:<sid>, action:<action>, blockaction:<block_action>, priority<severity> json 사용

detect or bypass일때 요청에 대해 응답수행 및 그에 따른 결과확인 필요
block 일때 요청에 대해 응답하지 않고 그에 따른 결과확인 필요

초기화 수행
* "VS_DUT01"에서 AGENT 정책 초기화를 한다
* "VS_DUT01"에서 IPS 정책 초기화를 한다
* "VS_DUT01"에서 IPS 이벤트 로그 초기화를 한다





