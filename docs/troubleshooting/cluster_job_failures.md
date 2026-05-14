# Cluster Job Failures

Owner: Computational lead  
Last reviewed: 2026-05-06  
Status: Example troubleshooting entry

## Symptom

A submitted job fails quickly, never starts, or exits with an unclear scheduler message.

## Common Causes

| Symptom | Likely Cause | First Check |
| --- | --- | --- |
| `OUT_OF_MEMORY` | Memory request too low | Review peak memory in scheduler accounting |
| Job pending for days | Queue or partition mismatch | Check requested partition and wall time |
| `command not found` | Environment not loaded in batch script | Confirm activation lines are inside the script |
| Empty output file | Script ran in unexpected working directory | Print `pwd` and input paths in the job log |

## Checks

```bash
sacct -j JOB_ID --format=JobID,State,Elapsed,MaxRSS,ExitCode
```

```bash
tail -n 100 logs/job_JOB_ID.err
```

## Fixes

- Request memory based on observed peak usage plus a modest margin.
- Use absolute paths for shared inputs.
- Load modules or activate conda environments inside the batch script.
- Add a small test job before submitting hundreds of tasks.

## Escalate When

- The same job fails on multiple nodes with no script changes.
- Scheduler accounting is unavailable.
- The job touches controlled-access data and may have written outputs to the wrong location.
