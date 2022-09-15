# 방화벽 테스트케이스(국가DB)
Tags: DEVICE.master_brk.ini, DEVICE.p_real_cent.ini, DEVICE.cpp_attacker.ini
table: data/product/hips_fw_table_nation.csv

## 방화벽 TC 수행

* <testname>의 <status> 검증 시나리오 수행

초기상태 설정
* "VS_DUT01"에서 AGENT 정책 초기화를 한다
* "VS_DUT01"에서 방화벽 정책 초기화를 한다
* "VS_DUT01"에서 FW 이벤트 로그 초기화를 한다

정책 설정
AGENT 정책에 사용자정의 국가 설정
* "VS_DUT01"에서 "policy_agent" 설정파일 "/var/policy/policy_agent.json" 정책 "user_nation":"0"의 string type 설정 "code"을 <user_nation>로 변경을 한다 xpath는 "body.policy_hips_agent.user_nation.[0].code" 이다
* "VS_DUT01"에서 "policy_agent" 설정파일 "/var/policy/policy_agent.json" 정책 "user_nation":"0"의 array type 설정 "ip"을 <user_nation_ip>로 변경을 한다 xpath는 "body.policy_hips_agent.user_nation.[0].ip" 이다
* "VS_DUT01"에서 "policy_agent" 설정파일 "/var/policy/policy_agent.json" 정책 "internal_network":"0"의 array type 설정 "ip"을 <internal_ip>로 변경을 한다 xpath는 "body.policy_hips_agent.internal_network.[0].ip" 이다

방화벽 정책 활성화
* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 사용여부를 <policy_enable>로 한다 xpath는 "body.policy_hips_firewall.enable" 이다

국가DB 정책 0번 설정
* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 정책 "block_nation":"0"의 string type 설정 "nation"을 <nation1>로 변경을 한다 xpath는 "body.policy_hips_firewall.block_nation.[0].nation" 이다
* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 정책 "block_nation":"0"의 string type 설정 "direction"을 <nation_direction1>로 변경을 한다 xpath는 "body.policy_hips_firewall.block_nation.[0].direction" 이다
* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 정책 "block_nation":"0"의 string type 설정 "description"을 <nation_description1>로 변경을 한다 xpath는 "body.policy_hips_firewall.block_nation.[0].description" 이다

국가DB 정책 1번 설정
* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 정책 "block_nation":"1"의 string type 설정 "nation"을 <nation2>로 변경을 한다 xpath는 "body.policy_hips_firewall.block_nation.[1].nation" 이다
* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 정책 "block_nation":"1"의 string type 설정 "direction"을 <nation_direction2>로 변경을 한다 xpath는 "body.policy_hips_firewall.block_nation.[1].direction" 이다
* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 정책 "block_nation":"1"의 string type 설정 "description"을 <nation_description2>로 변경을 한다 xpath는 "body.policy_hips_firewall.block_nation.[1].description" 이다

사용자정의 국가DB 정책 2번 설정
* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 정책 "block_nation":"2"의 string type 설정 "nation"을 <user_nation>로 변경을 한다 xpath는 "body.policy_hips_firewall.block_nation.[2].nation" 이다
* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 정책 "block_nation":"2"의 string type 설정 "direction"을 <nation_direction2>로 변경을 한다 xpath는 "body.policy_hips_firewall.block_nation.[2].direction" 이다
* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 정책 "block_nation":"2"의 string type 설정 "description"을 <nation_description2>로 변경을 한다 xpath는 "body.policy_hips_firewall.block_nation.[2].description" 이다

국가 DB를 적용시키기 위해 policy_agent.json 암호화 및 정책적용
* "VS_DUT01"에서 "policy_agent" 정책 암호화 CLI:"../exec.sh ./encrypt enc /var/policy/policy_agent.json"를 한다
* "VS_DUT01"에서 "policy_agent" 정책 적용 CLI:"../exec.sh ./hipstest set policy agent /var/policy/policy_agent.json.enc"을 한다

방화벽 정책을 적용시키기 위해 policy_fw.json 암호화 및 정책적용
* "VS_DUT01"에서 "policy_fw" 정책 암호화 CLI:"../exec.sh ./encrypt enc /var/policy/policy_fw.json"를 한다
* "VS_DUT01"에서 "policy_fw" 정책 적용 CLI:"../exec.sh ./hipstest set policy fw /var/policy/policy_fw.json.enc"을 한다
* "VS_DUT01"에서 CLI:"../exec.sh ./hipstest get policy fw" 적용결과를 확인한다

트래픽 테스트 및 결과확인
* "ATTACK01"에서 hping으로 탐지 트래픽을 발생 한다 조건은 sip:<traffic_sip1>, dip:"$VS_DUT01.ip", sport:<traffic_sport1>, dport:<traffic_dport1>, protocol:<traffic_protocol1> 이다
* "ATTACK01"에서 hping으로 탐지 트래픽을 발생 한다 조건은 sip:<traffic_sip2>, dip:"$VS_DUT01.ip", sport:<traffic_sport2>, dport:<traffic_dport2>, protocol:<traffic_protocol2> 이다
* "ATTACK01"에서 hping으로 탐지 트래픽을 발생 한다 조건은 sip:<user_tip>, dip:"$VS_DUT01.ip", sport:<traffic_sport2>, dport:<traffic_dport2>, protocol:<traffic_protocol2> 이다
* 5초 동안 대기
* "VS_DUT01"에서 "event" 로그 처리결과를 확인 한다 예상결과가 <expect_result1>이고 로그결과는 <log_result1>이다, 추가판단조건 sip:<traffic_sip1>, dip:"$VS_DUT01.ip", block_reason:"sn", rule_name:"nation", block_nation:<nation1>, ndir:<ndir1> json 사용
* "VS_DUT01"에서 "event" 로그 처리결과를 확인 한다 예상결과가 <expect_result2>이고 로그결과는 <log_result2>이다, 추가판단조건 sip:<traffic_sip2>, dip:"$VS_DUT01.ip", block_reason:"sn", rule_name:"nation", block_nation:<nation2>, ndir:<ndir2> json 사용
* "VS_DUT01"에서 "event" 로그 처리결과를 확인 한다 예상결과가 <expect_result2>이고 로그결과는 <log_result2>이다, 추가판단조건 sip:<user_tip>, dip:"$VS_DUT01.ip", block_reason:"sn", rule_name:"nation", block_nation:<user_nation>, ndir:<ndir2> json 사용


초기화 수행
* "VS_DUT01"에서 AGENT 정책 초기화를 한다
* "VS_DUT01"에서 방화벽 정책 초기화를 한다
* "VS_DUT01"에서 FW 이벤트 로그 초기화를 한다


