# Self Assessment Interpreter

Fast and automatic group repartition with comparable skillsets.

## About

For the purpose of our RESTify controlled experiment we strive for control groups with comparable skill sets. We want to ensure that the insight compaared for a given group is as comparable as possible to the data collected for any other group. This means we must ensure the group participants showcase comparable skills for the technologies involved.  
This repository contains a simple python program to automatize the group partition task, based on the recruits self-declared skill sets.

## Functionality

The program has just one main procedure that does the following:

 * Parse the provided [input forms](https://www.cs.mcgill.ca/~mschie3/recruitment/self-assessment.txt).
 * Extracted skill data to a markdown table.
 * Mine statistical skill data to a markdown table.
 * Run [*Timo's Heuristic*]() to create and print four comparable control groups.

### Input Form Parsing

The program searches recursively for ```.txt.``` files in the encrypted *RESTify* volume. The volume contains one folder per participant (named *first-lastname*) with the filled out [input form](https://www.cs.mcgill.ca/~mschie3/recruitment/self-assessment.txt) inside. If the volume is not mounted the program stops with exit code ```255``` and prints an error message.

### Skill Extraction

Filled input forms are reduced to lines containing any variant of ```[x]``` (variants defined as spaces at random positions. Using the line numbers of previous matches allows a subsequent quantification of every requested skill ration on a scale of [1-5], 1 being the lowest, 5 being the highest score possible.

### Statistics Extraction

The subsequent comparison / building of fair groups requires groups that are as similar as possible. Similarity is measured by comparison of the groups' overall normalized skill vectors. For skill vector comparison we use a the [cosine distance metric](https://en.wikipedia.org/wiki/Cosine_similarity), to sidestep the [curse of dimensionality of a standard euclidian metric](https://bib.dbvis.de/uploadedFiles/155.pdf).

### Timos Heuristic

A brute force testing of all possible group partitions is not technically feasible (```1.1E10``` combinations).  
Timo's algorithm attempts to search for the fairest possible partition where the first group created is as close as possible to the normalized average skill vector. This reduces the combinatoric charge for brute force testing of the remaining groups to ```757E3``` possible partitions, which can be checked manually for the best solution.

## Usage

...

## Contact / Pull Requests

 * Author: Maximilian Schiedermeier ![email](email.png)
 * Github: Kartoffelquadrat
 * Webpage: https://www.cs.mcgill.ca/~mschie3
 * License: [MIT](https://opensource.org/licenses/MIT)

