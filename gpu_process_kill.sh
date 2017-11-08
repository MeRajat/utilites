 kill $(nvidia-smi | awk '$2=="Processes:" {p=1} p && $2 == 0 && $3 > 0 {print $3}')
 
 // Kill process on GPU = 0, replace 0 with number of gpu that you want to kill 
