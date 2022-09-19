# chw package patch rollback and upgrade
Tags: DEVICE.p_real_win.ini
table: data/product/hips_fw_table_full.csv

## 정책 초기화
\chw_setup_typeC을 선 수행 해야 함.
* "P_W_DUT"에서 policy 초기화

## 롤백 패치수행
* "P_W_DUT"에서 agent 설정 변경 - 롤백 패치서버for 20H2
* "P_W_DUT"에서 롤백 업데이트 수행
* "P_W_DUT"에서 롤백 업데이트 수행결과 확인
* "P_W_DUT"에서 엔진구동 여부 확인

## 업데이트 패치수행
* "P_W_DUT"에서 agent 설정 변경 - 업데이트 패치서버for 20H2
* "P_W_DUT"에서 패치 업데이트 수행
* "P_W_DUT"에서 패치 업데이트 수행결과 확인
* "P_W_DUT"에서 엔진구동 여부 확인