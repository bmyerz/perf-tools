samples=$1

nodes=`scontrol show hostname $SLURM_NODE_LIST`
localdir=`pwd`
for x in $nodes; do
  ssh $x sar -n DEV 1 $samples | grep ib0 > $localdir/$x.$SLURM_JOB_ID.log && echo "$x done" &
done
