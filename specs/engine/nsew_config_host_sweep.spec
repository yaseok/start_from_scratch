# host sweep test

Tags: DEVICE.real_win.ini, DEVICE.nsew_attacker.ini

## NSEW 설치
* W_HIPS:"W_DUT"에 NSEW를 설치한다.

## 기본 Setup
* W_HIPS:"W_DUT"에 Port Scan 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다

## TCP Host Sweep 동작 확인
* "W_DUT"에서 "tcping 10.10.1.1"를 실행한다
* "W_DUT"에서 "tcping 10.10.1.2"를 실행한다
* "W_DUT"에서 "tcping 10.10.1.3"를 실행한다
* "W_DUT"에서 "Get-Content -Path c:/tmp/engine_event.json -TotalCount 1"를 실행한다
* EXEC 실행 결과 메시지는 "11200201"를 포함한다
* "W_DUT"에서 "./anse_ctl engine chcb json"를 실행한다
* "W_DUT"에서 "del c:/tmp/engine_event.json"를 실행한다
* "W_DUT"에서 "./anse_ctl engine chcb json c:/tmp/engine_event.json"를 실행한다

## UDP Host Sweep 동작 확인
* "W_DUT"에서 "udping 11.11.1.1"를 실행한다
* "W_DUT"에서 "./anse_ctl engine chcb json"를 실행한다
* "W_DUT"에서 "del c:/tmp/engine_event.json"를 실행한다
* "W_DUT"에서 "./anse_ctl engine chcb json c:/tmp/engine_event.json"를 실행한다
* "W_DUT"에서 "udping 11.11.1.2"를 실행한다
* "W_DUT"에서 "udping 11.11.1.3"를 실행한다
* "W_DUT"에서 "udping 11.11.1.4"를 실행한다
* 3초 동안 대기
* "W_DUT"에서 "Get-Content -Path c:/tmp/engine_event.json -TotalCount 1"를 실행한다
* EXEC 실행 결과 메시지는 "11200202"를 포함한다


## Ping Host Sweep 동작 확인
* "W_DUT"에서 "ping 12.12.1.1 -n 1"를 실행한다
* "W_DUT"에서 "ping 12.12.1.2 -n 1"를 실행한다
* "W_DUT"에서 "ping 12.12.1.3 -n 1"를 실행한다
* "W_DUT"에서 "./anse_ctl engine chcb json"를 실행한다
* "W_DUT"에서 "del c:/tmp/engine_event.json"를 실행한다
* "W_DUT"에서 "./anse_ctl engine chcb json c:/tmp/engine_event.json"를 실행한다
* "W_DUT"에서 "ping 12.12.1.4 -n 1"를 실행한다
* "W_DUT"에서 "ping 12.12.1.5 -n 1"를 실행한다
* 3초 동안 대기
* "W_DUT"에서 "Get-Content -Path c:/tmp/engine_event.json -TotalCount 1"를 실행한다
* EXEC 실행 결과 메시지는 "11200203"를 포함한다


## ARP Host Sweep 동작 확인
* "W_DUT"에서 "arp -d"를 실행한다
* "W_DUT"에서 "netsh interface ip delete arpcache"를 실행한다
* "W_DUT"에서 "ping 192.168.181.100 -n 1"를 실행한다
* "W_DUT"에서 "./anse_ctl engine chcb json"를 실행한다
* "W_DUT"에서 "del c:/tmp/engine_event.json"를 실행한다
* "W_DUT"에서 "./anse_ctl engine chcb json c:/tmp/engine_event.json"를 실행한다
* "W_DUT"에서 "ping 192.168.181.101 -n 1"를 실행한다
* "W_DUT"에서 "ping 192.168.181.102 -n 1"를 실행한다
* "W_DUT"에서 "ping 192.168.181.103 -n 1"를 실행한다
* 3초 동안 대기
* "W_DUT"에서 "Get-Content -Path c:/tmp/engine_event.json -TotalCount 1"를 실행한다
* EXEC 실행 결과 메시지는 "11200204"를 포함한다
