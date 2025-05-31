# Biological Computation - Graph Analysis

This repository contains Python scripts for analyzing and finding motifs in graphs, part of a Biological Computation assignment.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Noam-Diamant/BioComp.git
cd BioComp
```

## Usage

### Part 1 - Graph Generation
To generate all possible unique graphs of some size and save results to graphs.txt:
```bash
python Part1.py
```

notice that you need to change line 122 in ```Part1.py``` to the range of the sizes you want to see.

### Part 2 - Motif Analysis
To analyze motifs in a graph, run:
```bash
python Part2.py
```

The program expects input in the following format:
```
n
v1 v2
v2 v3
...
```
where:
- `n` is the motif size to search for
- Following lines contain edges of the graph (one edge per line)
- Input ends with an empty line or EOF

Example input:
```
3
1 2
2 3
1 3
3 4
```

### Execution Time Analysis
To analyze and plot execution times:
```bash
python plotting.py
```
This will create a plot based on the execution times recorded in graphs.txt.

## Output

- The programs will print results to the console
- Graph generation results are saved in `graphs.txt`
- Execution time plots are displayed and can be saved
