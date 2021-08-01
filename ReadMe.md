# Viruses's Diagnosis
This project diagnose urls in domains according to the user's request.


## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [How to run](#how-to-run)
* [How it works](#how-it-works)


## General info
This project uses Python 3.7 , Virustotal's api and helps to detect saspicious urls in domains.

## Technologies
* Python (3.7) 

## Setup
* install python 3 (or above)
* Make sure you have python packages: requests , datetime , json , os
 
## How to run
* Create domains files( each domain url (i.e msn.com) in a seperate line ) and put it inside folder X .
* Run the program and answer the stdin protocol questions (path to folder X , number of lines to read in each iteration)

## How it works
* The script connects Virustotal's api to ask for saspicious urls in the user's domain. Getting back the JSON response from the API, get the saspicious urls in the domain.

* The diagnostics would be located in Output_Folder.
