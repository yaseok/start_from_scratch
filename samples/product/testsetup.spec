# 테스트
Tags: DEVICE.vs_ubuntu_brk.ini, DEVICE.trafficgen_brk.ini
table: data/product/hips_test_table_.csv
## TC 수행

hips_config_init.spec을 선행하여 수행한다.
* "VS_DUT01"에서 alias를 설정한다
* "VS_DUT01"에서 내부 네트워크, 예외IP, 사용자정의 국가 최대값 설정된 AGENT 정책으로 초기화를 한다


정책설정
 "VS_DUT01"에서 "policy_agent" 설정파일 "/var/policy/policy_agent.json" Agent 정책에 rule:"user_nation", code:<user_nation_code>, ip:<user_nation_ip>로 추가. xpath는 "body.policy_hips_agent.user_nation"이다
 "VS_DUT01"에서 "policy_agent" 정책 암호화 CLI:"encrypt enc /var/policy/policy_agent.json"를 한다
 "VS_DUT01"에서 "policy_agent" 정책 적용 CLI:"hipstest set policy agent /var/policy/policy_agent.json.enc"을 한다
 "VS_DUT01"에서 DB:"sqlite3 /usr/local/ahnlab/chipsl/db/agent_policy_curr.db 'pragma key='test'; select * from config;'" 적용결과를 확인한다

* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 방화벽 정책에 rule:"rule100"을 삭제. xpath는 "body.policy_hips_firewall.rule.[*].rule_name"이다
* "VS_DUT01"에서 "policy_agent" 설정파일 "/var/policy/policy_agent.json" Agent 정책에 name:"NQ_except_100"을 삭제. xpath는 "body.policy_hips_agent.except_ip.[*].name"이다
* "VS_DUT01"에서 "policy_agent" 설정파일 "/var/policy/policy_agent.json" Agent 정책에 name:"NQ_int_Net100"을 삭제. xpath는 "body.policy_hips_agent.internal_network.[*].name"이다
* "VS_DUT01"에서 "policy_agent" 설정파일 "/var/policy/policy_agent.json" Agent 정책에 name:"NQ300"을 삭제. xpath는 "body.policy_hips_agent.user_nation.[*].code"이다
* "VS_DUT01"에서 "policy_agent" 정책 암호화 CLI:"encrypt enc /var/policy/policy_agent.json"를 한다
* "VS_DUT01"에서 "policy_agent" 정책 적용 CLI:"hipstest set policy agent /var/policy/policy_agent.json.enc"을 한다
* "VS_DUT01"에서 DB:"sqlite3 /usr/local/ahnlab/chipsl/db/agent_policy_curr.db 'pragma key='test'; select * from config;'" 적용결과를 확인한다