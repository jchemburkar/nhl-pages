# nhl-pages

A basic structure for a full-stack app displaying NHL data.

## Overview

### Goals
1. Put together a simple full stack app, to figure out how each piece fits together: backend, api, frontend.
2. Get practice with Typescript
3. Do 1 and 2 in a way that promotes scalibility, if new data sources were to be added, new views were needed, etc.

### What it does
When the project is run, it will use `docker-compose` to start a container with a mysql instance, then a python container, and load some sample data into it. I am not a huge fan of uploading data using `docker exec`, especially given the time cost in this project, but I found it to be the simplest way to ensure the proper data was present for this demo without including hard coded data files (which I thought would defeat the purpose). 

Then, the project uses npm to initalize and host a react app, which begins on a page with NHL standings, broken up by division. These tables are clickable, bringing you to a "team page" containing some simple metadata in the header, and the roster, split by position.

### What comes next?
As mentioned in the Goals section, I set this up in a way that would be expandible for future data sources. Some thoughts on possible additions:
- expand data offering to include advanced metrics -- for the standings page, this could be playoff odds. For the team page, this could be team level statistics
- add player pages with their indvidual stats, by season and career
- add the ability to create notes or attachments specific to teams or players.

## Project Structure

This repo serves as a monorepo for the python and typescript code for the app. Each dir is described below.

### apps

The `apps` dir is the Typescript repo holding the frontend code. The `src` folder is where the main logic exists, with a subfolder in `components` for the two main views (standings, team). Some packages used in the frontend:
- material-ui
- emotion/styled
- react-router-dom

### backend

There are two main subfolders to the backend: `api` and `uploader`. The `uploader` folder stores information for parsing data from external sources into the MySQL database. The `api` folder sets up a Flask api to serve that data to the frontend. Some packages central to this:
- Flask for the api
- Marshmallow, for creating schemas to validate and transform data
- SQLAlchemy as the ORM

## How to Run

To run the project, there are two main make commands that compose the individual commands. To load data, and start the app, run:

``` make up ```

To tear the project down in its entirety, run:

``` make down ```

### sub-commands

- to build the image (e.g., if you added a new import to `requirements.txt`): `make backend-build`
- to create the mysql database, a python container, and upload some base statsapi data to it: `make backend-up`
- to take the mysql database and python container down: `make backend-down`
- to rebulid the database and python container: `make backend-bounce`
- to enter a bash shell within the python container: `make backend-enter`
- to start the api: `make api-start`
- to start the app: `make app-start`
- to stop the app: `make app-stop`