Performance monitoring tools.

# Collect IP interface rates
```bash
salloc ...
./start-collect-iface.sh ib0
srun ...
```
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
