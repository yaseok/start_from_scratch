# Package Installation

Tags: DEVICE.vsphere_244.ini

## 신규 스냅샷 생성 및 기존 스냅샷 제거
* "0"에서 "20"초 사이 임의로 강제 대기
* "ESXI_244"에서 VM 정보를 얻어서 시나리오 변수에 저장한다
* "ESXI_244"에서 VM:"$vm"의 Snapshot 정보를 얻어서 시나리오 변수에 저장한다
* "ESXI_244"에서 VM:"$vm"의 Snapshot "$ss"을 생성한다
* "ESXI_244"에서 VM:"$vm"의 기존 SnapShot 이름:"$ss"을 삭제한다