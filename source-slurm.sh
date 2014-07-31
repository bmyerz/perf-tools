jobid=$1

export SLURM_JOB_ID=$jobid
export SLURM_NODELIST=`squeue -ppal | grep $jobid | awk '{ print $8 }'`
