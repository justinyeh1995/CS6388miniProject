
Somehow I cannot exec into my webgme container, so I switched to develop the studio locally..
The actual data stores under /var/lib/mongodb/ cause my mongo --dbpath <path> command is not working properly..

## Environment Setup & Installations

- Install `nvm` & `npm` & `nodejs`

- Install `mongodb 4.4.16`

- Download the project `git clone https://github.com/justinyeh1995/CS6388miniProject.git`

## Run the project

- Go to the project dir `cd CS6388miniProject/PeNDes`

- Install pakages `npm install` 

- To run the project, tyep `webgme start`

- Go to `http://localhost:8888` to see the frontend.

## What is a PetriNet

"A Petri Net is a collection of directed arcs connecting places and transitions. Places may hold tokens. The state or marking of a net is its assignment of tokens to places.

## Usecases of PetriNet

### A real world usecase: Split Join Networks

Expressing events happening in parallel is often necessary. 
This net shows how a single, sequential process can be split into two branches which run in parallel and then sync. 
The concept of parallel computing is an important one.

## Some notes

The plugin classifier is written but it does not show on the visualizations, hoping to fix this issue real quick...

## Ideas references
- [petrinet.org](http://petrinet.org/)

- [Homework567](https://mic.isis.vanderbilt.edu/?project=aadid_chih_d_ting_p_yeh_at_Vanderbilt_p_Edu%2BHomework567&branch=master&node=root&visualizer=METAAspect&tab=1&layout=DefaultLayout&selection=%2FH)

- [austin's repo](https://github.com/austinjhunt/petrinet-webgme-designstudio/)

- [WebGME-HFSM](https://github.com/finger563/webgme-hfsm)
