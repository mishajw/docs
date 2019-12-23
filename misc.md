# Misc. research

## COZ: Causal profiling

Doc: [coz](https://arxiv.org/pdf/1608.03676v1.pdf)

- Manually insert "progress points" into code.
- COZ will randomly slow down *all other* code when each progress point is hit.
- Effectively speeds up progress points.
- Measures effect of "speed up" on total program execution (by using time between progress points).

TODO: Why are progress points manual? Can't this be done automatically?
