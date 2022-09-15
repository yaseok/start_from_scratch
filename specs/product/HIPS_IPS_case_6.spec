# ips 테스트(사용여부,모드변환,대응방법)
Tags: DEVICE.p_real_cent.ini, DEVICE.cpp_attacker.ini
table: data/product/ips_table_predefined4.csv
## IPS TC 수행
* 엔진 모드 <engine_mode> 일 때 <testname>의 <status> 검증 시나리오 수행

초기상태 설정
* "VS_DUT01"에서 AGENT 정책 초기화를 한다
* "VS_DUT01"에서 IPS 정책 초기화를 한다
* "VS_DUT01"에서 IPS 이벤트 로그 초기화를 한다

동작 모드 및 정책 설정

IPS 동작 모드 설정
* "VS_DUT01"에서 "policy_agent" 설정파일 "/var/policy/policy_agent.json" 정책 "engine":"mode"의 string type 설정 "mode"을 <engine_mode>로 변경을 한다 xpath는 "body.policy_hips_agent.engine.mode" 이다

IPS 정책 설정
* "VS_DUT01"에서 "policy_mgmt" 설정파일 "/var/policy/policy_mgmt.json" boolean type 설정 "사용여부"을 <policy_enable>로 한다 xpath는 "body.policy_hips_ips_mgmt.enable" 이다
* "VS_DUT01"에서 "policy_mgmt" 설정파일 "/var/policy/policy_mgmt.json" string type 설정 "mode"을 <ips_mode>로 한다 xpath는 "body.policy_hips_ips_mgmt.mode" 이다
* "VS_DUT01"에서 "policy_mgmt" 설정파일 "/var/policy/policy_mgmt.json" 정책 "predefined" sid:<sid>을 action:<action>, blockAction:<block_action>, severity:<severity>, direction:<direction>, period:<period>, threshold:<threshold>, blockTime:<blockTime>, raw:<raw>, recommand:<recommand>, alarm:<alarm> 로 변경을 한다 xpath는 "body.policy_hips_ips_mgmt.predefined.default.[*].sid" 이다

policy_mgmt.json 암호화 및 적용
* "VS_DUT01"에서 "policy_mgmt" 정책 암호화 CLI:"../exec.sh ./encrypt enc /var/policy/policy_mgmt.json"를 한다
* "VS_DUT01"에서 "policy_mgmt" 정책 적용 CLI:"../exec.sh ./hipstest set policy mgmt /var/policy/policy_mgmt.json.enc"을 한다
* "VS_DUT01"에서 CLI:"../exec.sh ./hipstest get policy mgmt" 적용결과를 확인한다

policy_agent.json 암호화 및 정책적용
* "VS_DUT01"에서 "policy_agent" 정책 암호화 CLI:"../exec.sh ./encrypt enc /var/policy/policy_agent.json"를 한다
* "VS_DUT01"에서 "policy_agent" 정책 적용 CLI:"../exec.sh ./hipstest set policy agent /var/policy/policy_agent.json.enc"을 한다

트래픽 테스트 및 결과확인
* "ATTACK01"에서 FPG rule 파일 설정(기본시그니처용)
* "ATTACK01"에서 FPG로 탐지 트래픽을 발생 한다 조건은 sip:<traffic_sip>, dip:"$VS_DUT01.ip", sid:<sid>이다
* 5초 동안 대기
* "VS_DUT01"에서 "event" 로그 처리결과를 확인 한다 예상결과가 <expect_result>이고 로그결과는 <log_result>이다, 추가판단조건 sip:<traffic_sip>, dip:"$VS_DUT01.ip", attackid:<sid>, action:<expect_result>, blockaction:<block_action>, priority<severity> json 사용
"VS_DUT01"에서 "event" 로그 처리결과를 확인 한다 예상결과가 <expect_result>이고 로그결과는 <log_result>이다, 추가판단조건 sip:<traffic_sip>, dip:"$VS_DUT01.ip", attackid:<sid>, action:<expect_result>, blockaction:<block_action>

detect or bypass일때 요청에 대해 응답수행 및 그에 따른 결과확인 필요
block 일때 요청에 대해 응답하지 않고 그에 따른 결과확인 필요

초기화 수행
* "VS_DUT01"에서 AGENT 정책 초기화를 한다
* "VS_DUT01"에서 IPS 정책 초기화를 한다
* "VS_DUT01"에서 IPS 이벤트 로그 초기화를 한다





