# engine apply - host sweep test

Tags: DEVICE.real_cent.ini, DEVICE.nsel_attacker.ini

## 기본 Setup
* HIPS:"VS_DUT01"에 Host Sweep 테스트를 위한 기본 설정 파일을 저장하고 설정을 적용한다

## TCP Host Sweep 동작 확인
* "VS_DUT01"에서 TCP Host Sweep 패킷을 전송한다
* 3초 동안 대기
* "VS_DUT01"에서 "cat /tmp/engine_event.json |tail -n 1 |grep 11200201"를 실행한다
* EXEC 실행 결과 메시지는 "11200201"를 포함한다

## UDP Host Sweep 동작 확인
* "VS_DUT01"에서 UDP Host Sweep 패킷을 전송한다
* 3초 동안 대기
* "VS_DUT01"에서 "cat /tmp/engine_event.json |tail -n 1 |grep 11200202"를 실행한다
* EXEC 실행 결과 메시지는 "11200202"를 포함한다

## Ping Host Sweep 동작 확인
* "VS_DUT01"에서 Ping Host Sweep 패킷을 전송한다
* 3초 동안 대기
* "VS_DUT01"에서 "cat /tmp/engine_event.json |tail -n 1 |grep 11200203"를 실행한다
* EXEC 실행 결과 메시지는 "11200203"를 포함한다

## ARP Host Sweep 동작 확인
* "VS_DUT01"에서 ARP Host Sweep 패킷을 전송한다
* 3초 동안 대기
* "VS_DUT01"에서 "cat /tmp/engine_event.json |tail -n 1 |grep 11200204"를 실행한다
* EXEC 실행 결과 메시지는 "11200204"를 포함한다

## Zero I/O Host Sweep 동작 확인
* "VS_DUT01"에서 Zero I/O Host Sweep 패킷을 전송한다
* 10초 동안 대기
* "VS_DUT01"에서 "cat /tmp/engine_event.json |tail -n 1 |grep 11200205"를 실행한다
* EXEC 실행 결과 메시지는 "11200205"를 포함한다