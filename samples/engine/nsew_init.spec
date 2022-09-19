# 테스트 환경 준비
Tags: DEVICE.vsphere_243.ini, DEVICE.vsphere_244.ini

## 테스트 환경 초기화
* "ESXI_244"에서 VM 정보를 얻어서 시나리오 변수에 저장한다
* "ESXI_244"에서 VM:"NSEW_Win2008_R2_auto"의 Snapshot 정보를 얻어서 시나리오 변수에 저장한다
* "ESXI_244"에서 VM:"NSEW_Win2008_R2_auto"을 SnapShot 이름:"NSEW 자동화 셋팅 완료"으로 복구한다
* 15초 동안 대기
* "ESXI_243"에서 VM 정보를 얻어서 시나리오 변수에 저장한다
* "ESXI_243"에서 VM:"NSEW_Win2012_R2_auto"의 Snapshot 정보를 얻어서 시나리오 변수에 저장한다
* "ESXI_243"에서 VM:"NSEW_Win2012_R2_auto"을 SnapShot 이름:"NSEW 자동화 셋팅 완료"으로 복구한다
* 15초 동안 대기
* "ESXI_243"에서 VM 정보를 얻어서 시나리오 변수에 저장한다
* "ESXI_243"에서 VM:"NSEW_Win2016_auto"의 Snapshot 정보를 얻어서 시나리오 변수에 저장한다
* "ESXI_243"에서 VM:"NSEW_Win2016_auto"을 SnapShot 이름:"NSEW 자동화 셋팅 완료"으로 복구한다
* 15초 동안 대기