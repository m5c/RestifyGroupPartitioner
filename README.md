# Self Assessment Interpreter

Fast and automatic group repartition with comparable skillsets.

 > **THIS VERSION IS A STATIC SNAPSHOT, CREATED FOR THE MODELS ARTIFACT EVALUATION. UNLESS YOU ARE A REVIEWER, PLEASE [ACCESS THE ORIGINAL ARTIFACT](https://github.com/m5c/RestifyGroupPartitioner)**

## About

For the purpose of our RESTify controlled experiment we strive for control groups with comparable skill sets. We want to
ensure that the insight compared for a given group is as comparable as possible to the data collected for any other
group. This means we must ensure the group participants showcase comparable skills for the technologies involved.  
This repository contains a simple python program to automatize the group partition task, based on the recruits
self-declared skill sets.

 > Note: This software cannot be run without personal participant information (actual name linked to self-reported skills). The code cannot be executed without that undisclosed data. Nonetheless the algorothm code can be reviewed and reused for future projects.

## Functionality

The program has just one main procedure that does the following:

* Parse the provided [input forms](https://www.cs.mcgill.ca/~mschie3/recruitment/self-assessment.txt).
* Extracted skill data to a markdown table.
* Mine statistical skill data to a markdown table.
* Run a combination of Bettina's algorithm with subsequent brute force search for optimized variants. The details of
  this algorithm are described in ```MinniMaxOptimizer.py```.
* Participant droppers, resulting in two additional recruitment rounds were distributed with a brute force algorithm
  that testes all possible combinations and selected the ones with minimal skill offset between groups.

> Timo's Heuristic was considered, but never implemented due to insufficient computational power.

### Input Form Parsing

The program searches recursively for ```.txt.``` files in the [encrypted *RESTify* volume](#usage). The volume contains
one folder per participant (named *first-lastname*) with the filled
out [input form](https://www.cs.mcgill.ca/~mschie3/recruitment/self-assessment.txt) inside. If the volume is not mounted
the program stops with exit code ```255``` and prints an error message.

### Skill Extraction

Filled input forms are reduced to lines containing any variant of ```[x]``` (variants defined as spaces at random
positions. Using the line numbers of previous matches allows a subsequent quantification of every requested skill ration
on a scale of [1-5], 1 being the lowest, 5 being the highest score possible.

### Bettina's Heuristic

Only distribute based in *Total* skill points. Start on one side of ordered list and distribute into groups until end
reached. Total skills per group should be roughly the same.  
Implementation: Sort all participants by total points, then go back and forth over target groups. Take four lowest,
place into groups ABCD. On next iteration place into groups DCBA and so on.

### Timo's Heuristic

This algorithm was first proposed by [Dr. Timo Lang](https://interfacereasoning.com/people/):  
A brute force testing of all possible group partitions is not technically feasible (```1.1E10``` combinations).  
Timo's algorithm attempts to search for the fairest possible partition where the first group created is as close as
possible to the normalized average skill vector. This reduces the combinatorics charge for brute force testing of the
remaining groups to ```7.6E5``` possible partitions, which is still considerable.

## Usage

This software can only be used in combination with the original participant self assessment data. The latter cannot be
published for participant anonymity reasons as well as compliance with the McGill Research Ethics Board.

Run instructions:

* Mount the ```RESTify Veracrypt``` volume with all participant self assessment data.  
(Not published to protect participant anonymity)
* Start the partitioner: ```python SelfAssessmentInterpreter.py```.

## Contact / Pull Requests

* Author: [Maximilian Schiedermeier](mailto:schiedermeier.maximilian@uqam.ca)
* Github: [m5c](https://github.com/m5c)
* Webpage: [https://m5c.github.io/](https://m5c.github.io/)
* License: [MIT](https://opensource.org/licenses/MIT)

