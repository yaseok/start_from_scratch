# CPPM 추천 시그니처 목록 검사
Tags: DEVICE.RECOMM.ini
table: data/product/recomm_check.csv

## 테스트 디렉토리 생성
* <OS>에서 "rm -rf /tmp/recom"를 실행한다
* <OS>에서 "mkdir /tmp/recom"를 실행한다

## 기본 시그니처 SID 목록 업데이트
* 로컬 파일:"data/product/sid.txt"을 Device:<OS>의 경로:"/tmp/recom/sid.txt"로 SCP 복사 한다
* 로컬 파일:"data/product/recomm_check.sh"을 Device:<OS>의 경로:"/tmp/recom/recomm_check.sh"로 SCP 복사 한다
* <OS>에서 "chmod 755 /tmp/recom/recomm_check.sh"를 실행한다

## OS 추천 시그니처 목록 확인
* <OS>에서 "cp /usr/local/ahnlab/chipsl/var/recomm_backup/*.tar.gz /tmp/recom"를 실행한다
* <OS>에서 "cd /tmp/recom"를 실행한다
* <OS>에서 "tar xzvf *.tar.gz"를 실행한다
* <OS>에서 "grep -o '[0-9]*' basic_recommendation.json |head -n -1 > recommendation.txt"를 실행한다

## 추천 시그니처 결과 확인
* <OS>에서 기본 시그니처 추천 목록을 확인한다