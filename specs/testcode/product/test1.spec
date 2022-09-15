# product 테스트
Tags: DEVICE.master_brk.ini, DEVICE.vs_ubuntu_brk.ini, DEVICE.hpingsvr_brk.ini
table: data/product/hips_fw_table_failcase.csv

test

<testname>의 <status> 검증 시나리오 수행
<policy_name>,<policy_enable>,<rule_enable>,<rule_name1>,<rule_name2>,<rule_direction>,<seq_id>,<sip>,<traffic_sip>,<dip>,<traffic_dip>,<protocol>,<traffic_protocol>,<sport>,<traffic_sport>,<dport>,<traffic_dport>,<action>,<description>,<nation1>,<nation2>,<nation_direction>,<nation_description>,<expect_result>,<log_check> 값을 확인
"VS_DUT01"에서 설치파일 다운로드 및 install
"VS_DUT01"에서 설치파일 uninstall

"VS_DUT01"에서 alias를 설정한다

## 초기화 수행
* "VS_DUT01"에서 방화벽 정책 초기화를 한다
* "VS_DUT01"에서 "event" 로그 초기화를 한다
"VS_DUT01"에서 "operating" 로그 초기화를 한다