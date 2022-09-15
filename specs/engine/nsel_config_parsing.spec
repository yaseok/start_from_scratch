# 패턴 별 파싱 검증

Tags: DEVICE.real_cent.ini, DEVICE.nsel_attacker.ini
table: data/engine/table_config_parsing.csv

## 파싱 테스트 수행
* 로컬 파일:"data/engine/policy_hips_parsing.json"을 Device:"VS_DUT01"의 경로:"/tmp/policy_hips_parsing.json"로 SCP 복사 한다
* Json Name:"test"을 File:"data/engine/test.json"을 Load해서 생성한다
* Json Name:"test"의 XPATH:"list.[0].rule"의 값을 String value:<signature>로 변경한다
* Json Name:"test"을 Device:"VS_DUT01"의 File:"/tmp/test.json"에 저장한다
* "VS_DUT01"에서 "anse_ctl engine apply /tmp/policy_hips_parsing.json /tmp/test.json"를 실행한다
* "VS_DUT01"에서 "anse_ctl core show-signature-debug error"를 실행한다
* 예상 결과가 <expect>일 경우, <message> 내용이 <result>