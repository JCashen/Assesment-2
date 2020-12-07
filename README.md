# Gacha App

### Resources:
* Presentation and ERD: 
* Git Project Board: https://github.com/users/JCashen/projects/3

## Contents
* [Brief](#brief)
   * [Additional Requirements](#additional-requirements)
   * [My Approach](#my-approach)
* [Architecture](#architecture)
   * [Database Structure](#database-structure)
   * [CI Pipeline](#ci-pipeline)
* [Project Tracking](#project-tracking)
* [Risk Assessment](#risk-assessment)
* [Testing](#testing)
* [Front-End Design](#front-end-design)
* [Authors](#authors)

## Brief
The brief for this project was for us to create an app that uses 4 services and deploy it in a sturdy manner, this is done using docker swarm, nginx, gunicorn and jenkins.

### Additional Requirements
In addition to what has been set out in the brief, I am also required to include the following:
* Kanban Board: Asana or an equivalent Kanban Board
* Version Control: Git
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX

### My Approach
The app i decided to create was a Gacha app.

Service-1
service 1 was the frontend where the user will go and see a character name, affluence and star level.

![Service1][Service1]

Service-2
service 2 generates a random star rating from 1-5 

![Service2][Service2]

Service-3 
service 3 generates a random affluence between water, fire or lightning

![Service3][Service3]

Service-4
service 4 generates a character name it does this by taking in the star level and affluence and passing those values through an if statement.

![Service4][Service4]

## Architecture
### Database Structure
Below is an entity relationship diagram (ERD) showing the structure of the database that i attempted to implement. As the database was only one table it is very basic.

![ERD][ERD]

### App Structure
Below this is my app structure that shows how my services work tegether. 

![structure][structure]

### Infrastructure
below is the infastructure, as you can see jenkins, ansible and nginx are installed on the same machiene as this results in less configuration needed. The swarm is made of 1 manager aand 2 workers which are configured by ansible. nginx is also used as a load balancer. 

![infrstructure][infrastructure]

### CI Pipeline
Pictured below is the continuous integration pipeline.

![ci][ci]

## Project Tracking
GITHUB was used to track the progress of the project as seen on this board:https://github.com/users/JCashen/projects/3
this board contains the Scope, user stories and what has been completed from the scope.

## Version control
For version control i used github this was used as you can develop on many branches, this is useful as you can change the code without it affecting your working branch.
below is an img oof my branches.

![branch][branch]

## Risk Assessment
This is the risk assesment for this project, it shows the risks i though of before starting and whether i thought they where still risks at the end. 

![risk][risk]

## Testing
pytest is used to run unit tests on the app. this was used as it includes a coverage chart which allows the user to see how much of the program has been tested.

test service-1

![coverage1][coverage1]

test service-2

![coverage2][coverage2]

test service-3

![coverage3][coverage3]

test service-4

![coverage4][coverage4]

## Front-End Design
below is a screen grab of the home page, as you can see there is a star level an affluence and a character name.

![home][home]

## Authors
Joshua Cashen

[Service1]: https://i.imgur.com/gQxxK55.jpg
[Service2]: https://i.imgur.com/bJBGbkk.jpg
[Service3]: https://i.imgur.com/PPdnxsr.jpg
[Service4]: https://i.imgur.com/Cu4sjE1.jpg
[ERD]: https://i.imgur.com/6VZphc3.jpg
[risk]: https://i.imgur.com/1Xj9ArL.jpg
[ci]: https://i.imgur.com/l9IDTkU.jpg
[structure]: https://i.imgur.com/SgudEja.jpg
[infrastructure]: https://i.imgur.com/wpkS6w3.jpg
[branch]: https://i.imgur.com/RwBqOpN.jpg
[risk]: https://i.imgur.com/1Xj9ArL.jpg
[coverage1]: https://i.imgur.com/raQwf2d.jpg
[coverage2]: https://i.imgur.com/J5C1Heb.jpg
[coverage3]: https://i.imgur.com/OQrgj7g.jpg
[coverage4]: https://i.imgur.com/fPugvJc.jpg
[home]: https://i.imgur.com/KPGPpWK.jpg
