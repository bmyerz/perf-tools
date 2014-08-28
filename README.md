Performance monitoring tools for Linux clusters that are managed by [Slurm](http://slurm.schedmd.com).

# Collect IP interface rates from all nodes
```bash
# create your SLURM allocation
salloc ...

# start collecting
./start-collect-iface.sh ib0

# issue commands you wish to profile
srun ...
```

A log file will be created for each node.

Collection will end when your allocation is revoked (SLURM kills all your user processes).
To stop collection yourself, do

```bash
./stop-collect-all.sh
```

# If you don't have $SLURM\* set (e.g., not using salloc)
```bash
srun ...
. source-slurm.sh <jobid>
```

# Collect rates from mellanox IB counters
```bash
salloc ...
./start-collect-hca.sh
srun ...
```
Either wait until your allocation is revoked and kills your processes, or use
```bash
./stop-collect-hca.sh
```
