# Deployability and distribution

## Deployment unit

The primary release unit is the `repo-os` Python CLI. The generated support-agent service under `src/support_agent` is a reference output, not the generator runtime.

## Clean proof

```bash
pip install .
repo-os init --spec examples/project-spec.json --target /tmp/generated-repo
repo-os validate /tmp/generated-repo
```

## Distribution channel

- Python wheel and source archive for the generator.
- GitHub repository for inspectability and contributions.
- Generated repositories are independent artifacts and must declare their own deployment paths.

## Release invariant

A release fails if a clean spec cannot produce a deterministic, validated repository without mutating an existing non-empty target unless `--force` is explicit.
