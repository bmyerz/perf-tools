Performance monitoring tools for Linux clusters.

# Collect IP interface rates from all nodes
```bash
salloc ...
./start-collect-iface.sh ib0
srun ...
```
A log file will be created for each node.

Either wait until your allocation is revoked and kills your processes, or use
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
