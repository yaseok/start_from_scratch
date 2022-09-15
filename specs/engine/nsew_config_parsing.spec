# 패턴 별 파싱 검증

Tags: DEVICE.real_win.ini
table: data/engine/table_config_parsing.csv

## NSEW 설치
* W_HIPS:"W_DUT"에 NSEW를 설치한다.

## 파싱 테스트 수행
* Json Name:"test"을 File:"data/engine/test.json"을 Load해서 생성한다
* Json Name:"test"의 XPATH:"list.[0].rule"의 값을 String value:<signature>로 변경한다
* Json Name:"test"을 Device:"W_DUT"의 File:"/tmp/test.json"에 저장한다
* W_HIPS:"W_DUT"에서 anse_ctl Tool을 이용하여 "engine apply /tmp/policy_hips_ips_mgmt.json /tmp/test.json" 명령을 수행한다
* W_HIPS:"W_DUT"에서 anse_ctl Tool을 이용하여 "core show-signature-debug error" 명령을 수행한다
* 예상 결과가 <expect>일 경우, <message> 내용이 <result>