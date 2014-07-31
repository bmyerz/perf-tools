samples=$1  # number of samples to take; note you can instead stop all collection with stop-collect-all.sh
iface_pattern=$2  # e.g., ib0, eth0, ...

nodes=`scontrol show hostname $SLURM_NODE_LIST`
localdir=`pwd`
for x in $nodes; do
  ssh $x sar -n DEV 1 $samples | grep $iface_pattern > $localdir/$x.$iface_pattern.$SLURM_JOB_ID.log && echo "$x done" &
done
