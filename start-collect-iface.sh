iface_pattern=${1:-ib0}  # e.g., ib0, eth0, ...
samples=${2:-1800} # number of samples to take; note you can instead stop all collection with stop-collect-all.sh

nodes=`scontrol show hostname $SLURM_NODE_LIST`
localdir=`pwd`
for x in $nodes; do
  ssh $x sar -n DEV 1 $samples | grep $iface_pattern > $localdir/$x.$iface_pattern.$SLURM_JOB_ID.log && echo "$x done" &
done
