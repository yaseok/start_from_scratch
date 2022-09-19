# 사용자정의 시그니처(처리방법, 차단시간, 위험도)
Tags: DEVICE.p_real_cent.ini, DEVICE.cpp_attacker.ini
table: data/product/user_signature_1.csv
## IPS TC 수행
* <testname>의 <status> 검증 시나리오 수행

* "VS_DUT01"에서 alias를 설정한다
* "VS_DUT01"에서 제품이 설치된 버전을 확인한다
* "VS_DUT01"에서 제품이 설치된 디렉토리를 확인한다
* "VS_DUT01"에서 제품 툴이 설치된 디렉토리를 확인한다
* "VS_DUT01"에서 데몬 구동상태를 확인한다
* "VS_DUT01"에서 IPS 정책 초기화를 한다
* "VS_DUT01"에서 "event" 로그 초기화를 한다

정책 설정

기본정책 값에 IPS 사용, mode deny로 설정되어 있다.
IPS 정책 설정
* "VS_DUT01"에서 "policy_mgmt" 설정파일 "/var/policy/policy_mgmt.json" 정책 "predefined" sid:<sid>을 action:<action>, blockAction:<block_action>, severity:<severity>, direction:<direction>, period:<period>, threshold:<threshold>, blockTime:<blockTime>, raw:<raw>, alarm:<alarm> 로 변경을 한다 xpath는 "body.policy_hips_ips_mgmt.additional.user.[*].sid" 이다
암호화 및 적용
* "VS_DUT01"에서 "policy_mgmt" 정책 암호화 CLI:"encrypt enc /var/policy/policy_mgmt.json"를 한다
* "VS_DUT01"에서 "policy_mgmt" 정책 적용 CLI:"hipstest set policy mgmt /var/policy/policy_mgmt.json.enc"을 한다
* "VS_DUT01"에서 CLI:"hipstest get policy mgmt" 적용결과를 확인한다

트래픽 테스트 및 결과확인
* "ATTACK01"에서 FPG rule 파일 설정(사용자정의시그니처용)
* "ATTACK01"에서 FPG로 탐지 트래픽을 발생 한다 조건은 sip:<traffic_sip>, dip:"$VS_DUT01.ip", sid:<sid>이다
* "ATTACK01"에서 hping으로 탐지 트래픽을 발생 한다 조건은 sip:<traffic_sip>, dip:"$VS_DUT01.ip", sport:"1024", dport:<traffic_dport>, protocol:<traffic_protocol> 이다
* 5초 동안 대기
* "VS_DUT01"에서 "event" 로그 처리결과를 확인 한다 예상결과가 <expect_result>이고 로그결과는 <log_result>이다, 추가판단조건 sip:<traffic_sip>, dip:"$VS_DUT01.ip", attackid:<sid>, action:<action>, blockaction:<block_action>, priority<severity> json 사용
"VS_DUT01"에서 "event" 로그 처리결과를 확인 한다 예상결과가 <expect_result>이고 로그결과는 <log_result>이다, 추가판단조건 sip:<traffic_sip>, dip:"$VS_DUT01.ip", attackid:<sid>, action:<action>, blockaction:<block_action>

black list 등록에 따른 5tuple 트래픽 차단 확인

초기화 수행
"VS_DUT01"에서 IPS 정책 초기화를 한다





