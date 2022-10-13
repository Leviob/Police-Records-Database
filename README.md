# Police-Records-Database
This project pulls public data regarding police activities in Seattle. Data is downloaded from various datasets and loaded into a database.

## Overview
The data is explored initially in `exploration.ipynb`. From there, insights are applied to create an ETL in `etl.ipynb` which creates a SQL database.

## Raw Datasets
### Crisis Data
Includes officer number, officer date of birth, if the officer is certified in crisis intervention (CIT), officer race, precinct, sector, beat. 

### Use of Force
Contains information about the use of force, and the subject and officer involved.

### SPD Crime Data
Contains all crime reports that have been finalized. Includes Micro-Community Policing Plans(MCPP) designated by neighborhood names, beat, approximate address, and types of crimes.

## Beats
A "beat" is a defined area within a Sector. Sectors are geographic areas within Precincts. Seattle has 5 Precincts, each with their own geographic coverage. There are a total of 51 beats in Seattle.
Each beat is named with a letter-number combination and corresponds to a geographic area / group of neighborhoods.


