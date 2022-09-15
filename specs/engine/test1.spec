# TEST1

Tags: DEVICE.vsphere_244.ini

## TEST1
* "0"에서 "20"초 사이 임의로 강제 대기
* "ESXI_244"에서 VM 정보를 얻어서 시나리오 변수에 저장한다
* "ESXI_244"에서 VM:"$vm"의 Snapshot 정보를 얻어서 시나리오 변수에 저장한다
* "ESXI_244"에서 VM:"$vm"을 SnapShot 이름:"$ss"으로 복구한다
* "ESXI_244"에서 VM:"$vm"의 전원을 켜다
* "ESXI_244"에서 VM:"$vm"의 전원 상태를 확인한다
* EXEC 실행 결과 메시지는 "on"를 포함한다
* "0"에서 "10"초 사이 임의로 강제 대기