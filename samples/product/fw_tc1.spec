# 방화벽 테스트
Tags: DEVICE.master_brk.ini, DEVICE.vs_ubuntu_brk.ini, DEVICE.trafficgen_brk.ini
table: data/product/hips_fw_table_sample.csv

## 제품 구동상태 확인
* "VS_DUT01"에서 alias를 설정한다
* "VS_DUT01"에서 제품이 설치된 버전을 확인한다
* "VS_DUT01"에서 제품이 설치된 디렉토리를 확인한다
* "VS_DUT01"에서 제품 툴이 설치된 디렉토리를 확인한다
* "VS_DUT01"에서 데몬 구동상태를 확인한다

## 정책 설정
* "VS_DUT01"에서 기본 정책을 백업 한다
* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 사용여부를 "true"로 한다 xpath는 "body.policy_hips_firewall.enable" 이다
* "VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 정책 rule:<rule_name1>을 action:<action1>, enable:<rule_enable1>, direction:<rule_direction1>, seq_id:<seq_id1>, protocol:<protocol1>, sip:<sip1>, dip:<dip1>, sport:<sport1>, dport:<dport1>, description:<description1> 로 변경을 한다 xpath는 "body.policy_hips_firewall.rule.[*].rule_name" 이다
* "VS_DUT01"에서 "policy_fw" 정책 암호화 CLI:"encrypt enc /var/policy/policy_fw.json"를 한다
* "VS_DUT01"에서 "policy_fw" 정책 적용 CLI:"hipstest set policy fw /var/policy/policy_fw.json.enc"을 한다
* "VS_DUT01"에서 CLI:"hipstest get policy fw" 적용결과를 확인한다


"VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 정책 "rule":"0"의 boolean type 설정 "enable"을 "true"로 변경을 한다 xpath는 "body.policy_hips_firewall.rule.[0].enable" 이다
"VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 정책 "rule":"0"의 array type 설정 "sip"을 "[\"1.1.1.1\"]"로 변경을 한다 xpath는 "body.policy_hips_firewall.rule.[0].sip" 이다
"VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 정책 "rule":"0"의 array type 설정 "dip"을 "[\"0.0.0.0/0\"]"로 변경을 한다 xpath는 "body.policy_hips_firewall.rule.[0].dip" 이다
"VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 정책 "rule":"0"의 string type 설정 "protocol"을 "tcp"로 변경을 한다 xpath는 "body.policy_hips_firewall.rule.[0].protocol" 이다
"VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 정책 "rule":"0"의 array type 설정 "sport"을 "[\"20000\"]"로 변경을 한다 xpath는 "body.policy_hips_firewall.rule.[0].sport" 이다
"VS_DUT01"에서 "policy_fw" 설정파일 "/var/policy/policy_fw.json" 정책 "rule":"0"의 array type 설정 "dport"을 "[\"30000\"]"로 변경을 한다 xpath는 "body.policy_hips_firewall.rule.[0].dport" 이다


## 트래픽 테스트 및 결과확인

* "Trafficgen02"에서 hping으로 탐지 트래픽을 발생 한다 조건은 sip:"1.1.1.1", dip:"192.168.183.101", sport:"20000", dport:"30000", protocol:"S" 이다
* 3초 동안 대기
* "VS_DUT01"에서 "event" 로그 처리결과를 확인 한다 예상결과가 <expect_result1>이고 로그결과는 <log_result1>이다, 추가판단조건 sip:<traffic_sip1>, dip:<traffic_dip1>, rule_name:<rule_name1>

초기화 수행
* "VS_DUT01"에서 방화벽 정책 초기화를 한다
"VS_DUT01"에서 "event" 로그 초기화를 한다
"VS_DUT01"에서 "operating" 로그 초기화를 한다



