# 사용자 정의 국가객체 최대룰 추가
Tags: DEVICE.master_brk.ini, DEVICE.p_real_cent.ini
table:data/product/hips_user_nation_full.csv

## Agent 룰추가 TC 수행
hips_config_init.spec을 선행하여 수행한다.
* "VS_DUT01"에서 alias를 설정한다

정책설정

* "VS_DUT01"에서 "policy_agent" 설정파일 "/var/policy/policy_agent.json" Agent 정책에 rule:"user_nation", code:<user_nation_code>, ip:<user_nation_ip>로 추가. xpath는 "body.policy_hips_agent.user_nation"이다
* "VS_DUT01"에서 "policy_agent" 정책 암호화 CLI:"encrypt enc /var/policy/policy_agent.json"를 한다
* "VS_DUT01"에서 "policy_agent" 정책 적용 CLI:"hipstest set policy agent /var/policy/policy_agent.json.enc"을 한다
* "VS_DUT01"에서 DB:"sqlite3 /usr/local/ahnlab/chipsl/db/agent_policy_curr.db 'pragma key='test'; select * from config;'" 적용결과를 확인한다

트래픽 테스트 및 결과확인

"ATTACK01"에서 hping으로 탐지 트래픽을 발생 한다 조건은 sip:<traffic_sip1>, dip:<traffic_dip1>, sport:<traffic_sport1>, dport:<traffic_dport1>, protocol:<traffic_protocol1> 이다
"ATTACK01"에서 hping으로 탐지 트래픽을 발생 한다 조건은 sip:<traffic_sip2>, dip:<traffic_dip2>, sport:<traffic_sport2>, dport:<traffic_dport2>, protocol:<traffic_protocol2> 이다
5초 동안 대기
"VS_DUT01"에서 "event" 로그 처리결과를 확인 한다 예상결과가 <expect_result1>이고 로그결과는 <log_result1>이다, 추가판단조건 sip:<traffic_sip1>, dip:<traffic_dip1>, block_reason:"fw", rule_name:<rule_name1>, pdir:<rule_direction1> json 사용
"VS_DUT01"에서 "event" 로그 처리결과를 확인 한다 예상결과가 <expect_result2>이고 로그결과는 <log_result2>이다, 추가판단조건 sip:<traffic_sip2>, dip:<traffic_dip2>, block_reason:"fw", rule_name:<rule_name2>, pdir:<rule_direction2> json 사용



초기화 수행
"VS_DUT01"에서 alias를 설정한다
"VS_DUT01"에서 방화벽 정책 초기화를 한다
"VS_DUT01"에서 "event" 로그 초기화를 한다
"VS_DUT01"에서 "operating" 로그 초기화를 한다


