samples=${1:-1800}

PERF_TOOLS=/people/bdmyers/escience/perf-tools

nodes=`scontrol show hostname $SLURM_NODELIST`
localdir=`pwd`
for x in $nodes; do
  ssh $x python $PERF_TOOLS/collect_hca.py $samples $localdir/$x.hca1.$SLURM_JOB_ID.log && echo "$x done" &
done
