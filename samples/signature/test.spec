# 시그니처 유효성 검사
Tags: DEVICE.HIPS.ini

## 신규 시그니처 파일 업데이트
* 로컬 파일:"SIG/hips_signature.zip"을 Device:"HIPS"의 경로:"/tmp/hips_signature.zip"로 업로드 한다

## 엔진 패키지 업데이트
* 로컬 파일:"SIG/nsel_package.tar.gz"을 Device:"HIPS"의 경로:"/tmp/nsel_package.tar.gz"로 업로드 한다
* 로컬 파일:"SIG/nsel_testsuite_package.tar.gz"을 Device:"HIPS"의 경로:"/tmp/nsel_testsuite_package.tar.gz"로 업로드 한다

## 엔진 설치
* HIPS:"VS_DUT01"에 시그니처 테스트 환경 Initialize

## 시그니처 유효성 검증 수행
* HIPS:"VS_DUT01"에 시그니처 준비
* HIPS:"VS_DUT01"에 시그니처 로드 및 결과 확인