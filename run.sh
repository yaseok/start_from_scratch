#! /bin/bash

export ss
vm=$1
export vm
cp conf/$vm.ini conf/real_cent.ini
mkdir $vm

echo `sed -i '/^$/d' data/snapshot/$1`

while read ss
	do
		gauge -v run specs/engine/vm_ctrl.spec specs/engine/nsel_initialize.spec specs/engine/nsel_cmd_*.spec specs/engine/nsel_config_*.spec specs/engine/nsel_pcap_mode_on.spec specs/engine/nsel_pcap_sig_pattern* specs/engine/nsel_finalize.spec
		cp -R reports $vm/$ss

	done < data/snapshot/$1
