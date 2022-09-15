# NQPlus 테스트 Spec - HIPS Windows 샘플 테스트

Tags: DEVICE.win2016_ps.ini, DEVICE.dc_hping_1c.ini

## HIPS 샘플 테스트
[STEP 1] anse_mon 구동
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
anse_mon 구동및 anse.dll load( 테스트 기간에 반드시 실행되고 있어야함. )
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* "WINSVR"에서 "cd c:\\Users\\vmadmin\\Downloads\\amd64"를 실행한다
* "WINSVR"에서 "dir"를 실행한다
* "WINSVR"에서 "Start-Process -NoNewWindow -RedirectStandardOutput c:\\tmp\\anse_mon.log .\\anse_mon"를 실행한다
* "WINSVR"에서 ".\\anse_ctl server load anse.dll"를 실행한다


[STEP 2] Driver 초기화
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Driver 초기화 수행
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* "WINSVR"에서 ".\\anse_ctl driver install"를 실행한다
* "WINSVR"에서 ".\\anse_ctl driver load"를 실행한다
* "WINSVR"에서 ".\\anse_ctl driver init"를 실행한다
* "WINSVR"에서 ".\\anse_ctl engine init"를 실행한다
* "WINSVR"에서 ".\\anse_ctl driver start"를 실행한다

[STEP 3] 로그 저장소 설정
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
c:\tmp\enginelog.json으로 로그 저장소 초기화 및  변경
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* "WINSVR"에서 "del c:\\tmp\\enginelog.json"를 실행한다
* "WINSVR"에서 ".\\anse_ctl  engine chcb json c:\\tmp\\enginelog.json"를 실행한다

[STEP 4] 방화벽 설정
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
c:\tmp\enginelog.json으로 로그 저장소 초기화 및  변경
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* "WINSVR"에서 ".\\anse_ctl engine apply c:\\tmp\\firewall.json"를 실행한다

[STEP 4] 탐지 트래픽 전송
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
탐지 트래픽 전송
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* "HPING01"에서 "hping3 -S 192.168.184.20 -p 443 -c 1"를 실행한다

[STEP 5] 로그 확인
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
탐지 트래픽 전송
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* "WINSVR"에서 "cat c:\\tmp\\enginelog.json"를 실행한다

[STEP 6] Driver 종료 및 anse_mon 종료
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
탐지 트래픽 전송
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* "WINSVR"에서 ".\\anse_ctl driver stop"를 실행한다
* "WINSVR"에서 ".\\anse_ctl engine deinit"를 실행한다
* "WINSVR"에서 ".\\anse_ctl driver deinit"를 실행한다
* "WINSVR"에서 ".\\anse_ctl driver unload"를 실행한다
* "WINSVR"에서 ".\\anse_ctl driver uninstall"를 실행한다
