# Package Installation

Tags: DEVICE.real_cent.ini

## 패키지 설치
* "VS_DUT01"에서 "cd /tmp"를 실행한다
* "VS_DUT01"에서 "curl -k -L https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64 -o /usr/local/bin/jq && chmod a+x /usr/local/bin/jq"를 실행한다
* EXEC 실행 결과 코드는 "0"와 같다
* "VS_DUT01"에서 "wget --no-check-certificate https://vault.centos.org/6.10/os/x86_64/Packages/nmap-5.51-6.el6.x86_64.rpm"를 실행한다
* "VS_DUT01"에서 "rpm -ivh nmap-5.51-6.el6.x86_64.rpm"를 실행한다
* "VS_DUT01"에서 "rpm -qa |grep nmap"를 실행한다
* EXEC 실행 결과 코드는 "0"와 같다