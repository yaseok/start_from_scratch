#! /bin/bash

export ss

while read ss
	do
		gauge -v run vm_ctrl.spec nsel_initialize.spec nsel_config_fw_mode.spec nsel_finalize.spec 
	done < engine.txt

