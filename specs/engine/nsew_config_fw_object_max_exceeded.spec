# 방화벽 정책 - 객체 유형별 최대 개수 초과 적용 케이스
Tags: DEVICE.real_win.ini, DEVICE.nsew_attacker.ini
table: data/engine/w_table_config_fw_object_max_exceeded.csv

## NSEW 설치
* W_HIPS:"W_DUT"에 NSEW를 설치한다.

## 기본 Setup
* W_HIPS:"W_DUT"에 방화벽 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다

## 방화벽 정책 객체 유형별 최대 개수를 초과했을 때 예외 처리 검증(적용 실패 처리)
최대 개수: 객체당 255개

아래와 같이 설정 후 적용
1. 출발지 IP주소: 256개, 나머지 객체 1개
2. 목적지 IP주소: 256개, 나머지 객체 1개
3. 출발지 포트: 256개, 나머지 객체 1개
4. 목적지 포트: 256개, 나머지 객체 1개

* W_HIPS:"W_DUT"에서 엔진의 설정을 변경하고 적용했을 때 적용 실패한다 (String Type, <menu>, <xpath>, <path_local>, <path_remote_1>, <path_remote_2>, <value>)
* "W_DUT"에서 "cat /tmp/policy_hips_firewall.json"를 실행한다
* W_HIPS:"W_DUT"에서 엔진의 설정을 확인한다 (Object Type, <anse_cmd>, <result_path>, <result_value>)

______
수정했던 방화벽 정책의 객체를 초기화하기 위해 아래 step 수행한다. 엔진에 적용하지는 않는다.
* Json Name:"policy_hips_fw_mgmt"을 File:"data/engine/policy_hips_firewall.json"을 Load해서 생성한다
* Json Name:"policy_hips_fw_mgmt"의 XPATH:"policy_hips_firewall.enable"의 값을 Boolean value:"true"로 변경한다
* Json Name:"policy_hips_fw_mgmt"을 Device:"W_DUT"의 File:"/tmp/policy_hips_firewall.json"에 저장한다