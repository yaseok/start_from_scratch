# 테스트 환경 준비
Tags: DEVICE.vsphere_116.ini, DEVICE.vsphere_243.ini

## 테스트 환경 초기화
* "ESXI_116"에서 VM 정보를 얻어서 시나리오 변수에 저장한다
* "ESXI_116"에서 VM:"NSEW_Win2016_signature"의 Snapshot 정보를 얻어서 시나리오 변수에 저장한다
* "ESXI_116"에서 VM:"NSEW_Win2016_signature"을 SnapShot 이름:"signature"으로 복구한다
* 15초 동안 대기
* "ESXI_243"에서 VM 정보를 얻어서 시나리오 변수에 저장한다
* "ESXI_243"에서 VM:"NSEW_Attacker"의 Snapshot 정보를 얻어서 시나리오 변수에 저장한다
* "ESXI_243"에서 VM:"NSEW_Attacker"을 SnapShot 이름:"signature"으로 복구한다
* 15초 동안 대기
