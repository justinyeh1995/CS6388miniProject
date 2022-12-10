
Somehow I cannot exec into my webgme container, so I switched to develop the studio locally..
The actual data stores under /var/lib/mongodb/ cause my mongo --dbpath <path> command is not working properly..

## Ideas references
- [petrinet.org](http://petrinet.org/)

- [Homework567](https://mic.isis.vanderbilt.edu/?project=aadid_chih_d_ting_p_yeh_at_Vanderbilt_p_Edu%2BHomework567&branch=master&node=root&visualizer=METAAspect&tab=1&layout=DefaultLayout&selection=%2FH)

- [austin's repo](https://github.com/austinjhunt/petrinet-webgme-designstudio/)

- [WebGME-HFSM](https://github.com/finger563/webgme-hfsm)

## Environment Setup

Install `nvm` & `npm` & `nodejs`

Install `mongodb 4.4.16`

`git clone https://github.com/justinyeh1995/CS6388miniProject.git`

## Run the project

`cd PeNDes`

`webgme start`

go to `http://localhost:8080`

## Usecases of PetriNet

### Split Join Networks

Expressing events happening in parallel is often necessary. 
This net shows how a single, sequential process can be split into two branches which run in parallel and then sync. 
The concept of parallel computing is an important one.
