
nodes=`scontrol show hostname $SLURM_NODELIST`
for x in $nodes; do
  pid=`ssh $x ps aux | grep sar | grep -v grep | awk '{ print $2 }'`
  ssh $x kill $pid
done
