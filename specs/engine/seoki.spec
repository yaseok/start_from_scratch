# TEST 1

Tags: DEVICE.real_cent.ini, DEVICE.nsel_attacker.ini
table: data/engine/seoki.csv

## TEST 2
* Json Name:"test"을 File:"data/engine/test.json"을 Load해서 생성한다
* Json Name:"test"의 XPATH:"list.[0].rule"의 값을 String value:<signature>로 변경한다
* Json Name:"test"을 Device:"VS_DUT01"의 File:"/tmp/test.json"에 저장한다
* "VS_DUT01"에서 "anse_ctl engine apply /tmp/policy_hips_ips_mgmt.json /tmp/test.json"를 실행한다
* "VS_DUT01"에서 "anse_ctl core show-signature-debug error"를 실행한다
* 예상 결과가 <expect>일 경우, <message> 내용이 <result>