# 방화벽 테스트케이스(사용자 정의 국가 최대치 추가 상태에서 추가/수정/삭제 시 동작확인)
Tags: DEVICE.master_brk.ini, DEVICE.vs_ubuntu_brk.ini, DEVICE.trafficgen_brk.ini
table: data/product/hips_fw_table_nation_maxconf_tc.csv

## 방화벽 TC 수행

* <testname>의 <status> 검증 시나리오 수행

초기상태 체크
* "VS_DUT01"에서 alias를 설정한다
* "VS_DUT01"에서 제품이 설치된 버전을 확인한다
* "VS_DUT01"에서 제품이 설치된 디렉토리를 확인한다
* "VS_DUT01"에서 제품 툴이 설치된 디렉토리를 확인한다
* "VS_DUT01"에서 데몬 구동상태를 확인한다
* "VS_DUT01"에서 내부 네트워크, 예외IP, 사용자정의 국가 최대값 설정된 AGENT 정책으로 초기화를 한다
* "VS_DUT01"에서 방화벽 정책 초기화를 한다
* "VS_DUT01"에서 "event" 로그 초기화를 한다

정책설정
AGENT 정책에 사용자정의 국가 최대 설정 상태에서 신규 사용자정의 국가 추가 시 동작 확인
* "VS_DUT01"에서 "policy_agent" 설정파일 "/var/policy/policy_agent.json" Agent 정책에 rule:"user_nation", code:<user_nation1>, ip:<user_nation_ip1>로 추가. xpath는 "body.policy_hips_agent.user_nation"이다
* "VS_DUT01"에서 "policy_agent" 정책 암호화 CLI:"encrypt enc /var/policy/policy_agent.json"를 한다
* "VS_DUT01"에서 "policy_agent" 정책 적용 CLI:"hipstest set policy agent /var/policy/policy_agent.json.enc"을 한다_예상결과 실패
* "VS_DUT01"에서 DB:"sqlite3 /usr/local/ahnlab/chipsl/db/agent_policy_curr.db 'pragma key='test'; select * from config;'" 적용결과를 확인한다

AGENT 정책 최대 추가된 상태에서 룰 1개 삭제 후 추가 확인
* "VS_DUT01"에서 "policy_agent" 설정파일 "/var/policy/policy_agent.json" Agent 정책에 name:<user_nation1>을 삭제. xpath는 "body.policy_hips_agent.user_nation.[*].code"이다
* "VS_DUT01"에서 "policy_agent" 설정파일 "/var/policy/policy_agent.json" Agent 정책에 name:<user_nation3>을 삭제. xpath는 "body.policy_hips_agent.user_nation.[*].code"이다
* "VS_DUT01"에서 "policy_agent" 정책 암호화 CLI:"encrypt enc /var/policy/policy_agent.json"를 한다
* "VS_DUT01"에서 "policy_agent" 정책 적용 CLI:"hipstest set policy agent /var/policy/policy_agent.json.enc"을 한다
* "VS_DUT01"에서 DB:"sqlite3 /usr/local/ahnlab/chipsl/db/agent_policy_curr.db 'pragma key='test'; select * from config;'" 적용결과를 확인한다

* "VS_DUT01"에서 "policy_agent" 설정파일 "/var/policy/policy_agent.json" Agent 정책에 rule:"user_nation", code:<user_nation1>, ip:<user_nation_ip1>로 추가. xpath는 "body.policy_hips_agent.user_nation"이다
* "VS_DUT01"에서 "policy_agent" 정책 암호화 CLI:"encrypt enc /var/policy/policy_agent.json"를 한다
* "VS_DUT01"에서 "policy_agent" 정책 적용 CLI:"hipstest set policy agent /var/policy/policy_agent.json.enc"을 한다
* "VS_DUT01"에서 DB:"sqlite3 /usr/local/ahnlab/chipsl/db/agent_policy_curr.db 'pragma key='test'; select * from config;'" 적용결과를 확인한다

AGENT 정책 최대 추가된 상태에서 일부 룰 변경
* "VS_DUT01"에서 "policy_agent" 설정파일 "/var/policy/policy_agent.json" 정책 "code":<user_nation2>을 ip:<user_nation_ip2> 로 변경을 한다 xpath는 "body.policy_hips_agent.user_nation.[*].code" 이다
* "VS_DUT01"에서 "policy_agent" 정책 암호화 CLI:"encrypt enc /var/policy/policy_agent.json"를 한다
* "VS_DUT01"에서 "policy_agent" 정책 적용 CLI:"hipstest set policy fw /var/policy/policy_agent.json.enc"을 한다
* "VS_DUT01"에서 DB:"sqlite3 /usr/local/ahnlab/chipsl/db/agent_policy_curr.db 'pragma key='test'; select * from config;'" 적용결과를 확인한다

방화벽 정책 활성화
* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 사용여부를 <policy_enable>로 한다 xpath는 "body.policy_hips_firewall.enable" 이다

사용자정의 국가를 방화벽 룰에 추가: nation1: 신규추가 국가, nation2: 변경한 국가, nation3: 기존에 있던 사용자 정의 국가
* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 방화벽 정책에 nation:<user_nation1>, direction:<nation_direction>, description:<nation_description1>로 추가. xpath는 "body.policy_hips_firewall.block_nation"이다
* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 방화벽 정책에 nation:<user_nation2>, direction:<nation_direction>, description:<nation_description2>로 추가. xpath는 "body.policy_hips_firewall.block_nation"이다
* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 방화벽 정책에 nation:<user_nation4>, direction:<nation_direction>, description:<nation_description4>로 추가. xpath는 "body.policy_hips_firewall.block_nation"이다

방화벽 정책을 적용시키기 위해 policy_fw.json 암호화 및 정책적용
* "VS_DUT01"에서 "policy_fw" 정책 암호화 CLI:"encrypt enc /var/policy/policy_fw.json"를 한다
* "VS_DUT01"에서 "policy_fw" 정책 적용 CLI:"hipstest set policy fw /var/policy/policy_fw.json.enc"을 한다
* "VS_DUT01"에서 DB:"sqlite3 /usr/local/ahnlab/chipsl/db/fw_policy_curr.db 'pragma key='test'; select * from config;'" 적용결과를 확인한다

트래픽 테스트 및 결과확인

* "Trafficgen02"에서 hping으로 탐지 트래픽을 발생 한다 조건은 sip:<traffic_sip1>, dip:<traffic_dip>, sport:<traffic_sport>, dport:<traffic_dport>, protocol:<traffic_protocol> 이다
* "Trafficgen02"에서 hping으로 탐지 트래픽을 발생 한다 조건은 sip:<traffic_sip2>, dip:<traffic_dip>, sport:<traffic_sport>, dport:<traffic_dport>, protocol:<traffic_protocol> 이다
* "Trafficgen02"에서 hping으로 탐지 트래픽을 발생 한다 조건은 sip:<traffic_sip4>, dip:<traffic_dip>, sport:<traffic_sport>, dport:<traffic_dport>, protocol:<traffic_protocol> 이다
* 5초 동안 대기
* "VS_DUT01"에서 "event" 로그 처리결과를 확인 한다 예상결과가 <expect_result1>이고 로그결과는 <log_result1>이다, 추가판단조건 sip:<traffic_sip1>, dip:<traffic_dip>, block_reason:"sn", rule_name:"nation", block_nation:<user_nation1>, ndir:<ndir> json 사용
* "VS_DUT01"에서 "event" 로그 처리결과를 확인 한다 예상결과가 <expect_result2>이고 로그결과는 <log_result2>이다, 추가판단조건 sip:<traffic_sip2>, dip:<traffic_dip>, block_reason:"sn", rule_name:"nation", block_nation:<user_nation2>, ndir:<ndir> json 사용
* "VS_DUT01"에서 "event" 로그 처리결과를 확인 한다 예상결과가 <expect_result4>이고 로그결과는 <log_result4>이다, 추가판단조건 sip:<traffic_sip4>, dip:<traffic_dip>, block_reason:"sn", rule_name:"nation", block_nation:<user_nation4>, ndir:<ndir> json 사용


초기화 수행
"VS_DUT01"에서 alias를 설정한다
"VS_DUT01"에서 방화벽 정책 초기화를 한다
"VS_DUT01"에서 "event" 로그 초기화를 한다
"VS_DUT01"에서 "operating" 로그 초기화를 한다


