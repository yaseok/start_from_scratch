# 전체 초기화
Tags: DEVICE.master_brk.ini, DEVICE.p_real_cent.ini


## 정책 초기화 TC 수행

초기상태 체크
* "VS_DUT01"에서 alias를 설정한다
* "VS_DUT01"에서 제품이 설치된 버전을 확인한다
* "VS_DUT01"에서 제품이 설치된 디렉토리를 확인한다
* "VS_DUT01"에서 제품 툴이 설치된 디렉토리를 확인한다
* "VS_DUT01"에서 데몬 구동상태를 확인한다
* "VS_DUT01"에서 방화벽 정책 초기화를 한다
* "VS_DUT01"에서 AGENT 정책 초기화를 한다
* "VS_DUT01"에서 IPS 정책 초기화를 한다
* "VS_DUT01"에서 "event" 로그 초기화를 한다
* "VS_DUT01"에서 "cp /var/policy/org/policy_fw_none_rule.json /var/policy/policy_fw.json"를 실행한다
"VS_DUT01"에서 "cp /var/policy/org/policy_agent_none_rule.json /var/policy/policy_agent.json"를 실행한다


