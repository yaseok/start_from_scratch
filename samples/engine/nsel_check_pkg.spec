# pkg 확인

Tags: DEVICE.real_cent.ini

## os에 해당하는 nsel pkg가 존재하는지 확인
* 로컬 파일:"data/engine/nsel_package.tar.gz"을 Device:"VS_DUT01"의 경로:"/tmp/nsel_package.tar.gz"로 업로드 한다
* "VS_DUT01"에서 "cd /tmp"를 실행한다
* "VS_DUT01"에서 "tar xvfz nsel_package.tar.gz"를 실행한다
* "VS_DUT01"에서 "cd /tmp/nsel_package/"를 실행한다
* "VS_DUT01"에서 "find . -name \"*`uname -r`*\" > pkgname"를 실행한다
* "VS_DUT01"에서 "cat pkgname"를 실행한다
* "VS_DUT01"에서 "find . -size 0"를 실행한다
* EXEC 실행 결과 메시지는 "./pkgname"를 포함 하지 않는다