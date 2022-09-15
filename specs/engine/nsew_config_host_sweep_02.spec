# host sweep test 02

Tags: DEVICE.real_win.ini, DEVICE.nsew_attacker.ini

## NSEW 설치
* W_HIPS:"W_DUT"에 NSEW를 설치한다.

## 기본 Setup
* W_HIPS:"W_DUT"에 Port Scan 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다02

## Zero I/O Host Sweep 동작 확인 02
* "W_DUT"에서 "tcping 13.13.1.1"를 실행한다
* "W_DUT"에서 "tcping 13.13.1.2"를 실행한다
* 3초 동안 대기
* "W_DUT"에서 "Get-Content -Path c:/tmp/engine_event.json -TotalCount 1"를 실행한다
* EXEC 실행 결과 메시지는 "11200205"를 포함 한다
* "W_DUT"에서 "./anse_ctl engine chcb json"를 실행한다
* "W_DUT"에서 "del c:/tmp/engine_event.json"를 실행한다
* "W_DUT"에서 "./anse_ctl engine chcb json c:/tmp/engine_event.json"를 실행한다




