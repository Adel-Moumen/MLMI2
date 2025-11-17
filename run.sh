
source $HOME/sb/bin/activate

scp $HOME/projects/def-ravanelm/datasets/TIMIT.tar.gz $SLURM_TMPDIR
tar -xzf $SLURM_TMPDIR/TIMIT.tar.gz -C $SLURM_TMPDIR
mv $SLURM_TMPDIR/TIMIT $SLURM_TMPDIR/timit
ls $SLURM_TMPDIR