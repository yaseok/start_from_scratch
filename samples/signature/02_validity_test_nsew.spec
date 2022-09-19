# 시그니처 유효성 검사
Tags: DEVICE.nsew_attacker.ini, DEVICE.win2016_sig_db_check.ini

## 기본 Setup
* W_HIPS:"W_DUT"에 NSEW 패치키를 위치시킨다.

## NSEW 설치
* W_HIPS:"W_DUT"에 NSEW를 설치한다.

## 신규 시그니처 파일 업데이트
* 로컬 파일:"SIG/hips_signature.zip"을 Device:"ATTACK"의 경로:"/root/kjcho/signature_db_check/rule/hips_signature.zip"로 업로드 한다
* "ATTACK"에서 "cd /root/kjcho/signature_db_check/rule"를 실행한다
* "ATTACK"에서 "unzip hips_signature.zip"를 실행한다
* "ATTACK"에서 "../make_hips_policy_2.sh hips_signature_meta.json hips_signature_policy.json"를 실행한다
* "ATTACK"에서 "sshpass -p 'qwe123!@#' scp -o StrictHostKeyChecking=no hips_signature_policy.json nqa@192.168.181.16:/tmp/hips_signature_policy.json"를 실행한다
* "ATTACK"에서 "sshpass -p 'qwe123!@#' scp -o StrictHostKeyChecking=no hips_signature_list.json nqa@192.168.181.16:/tmp/hips_signature_list.json"를 실행한다

## 신규 시그니처 적용
* "W_DUT"에서 "cd /"를 실행한다
* "W_DUT"에서 "./signature_apply.ps1"를 실행한다
* 60초 동안 대기

## 엔진, 시그니처 버전 및 결과 확인
* W_HIPS:"W_DUT"에서 신규 시그니처 옵션 유효성을 확인
