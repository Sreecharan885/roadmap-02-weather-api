Hi There!

This is a [project from Roadmap.Sh Backend Roadmap](https://roadmap.sh/projects/weather-api-wrapper-service)

## Pre-requisites
1. Before proceeding, please create an account in the Visual Crossing Weather API site and generate an API Key.
2. Also, please setup Redis on your computer. If you're on Windows, you can utilize WSL for installing Redis. Please check out [this video by Web Dev Simplified](https://www.youtube.com/watch?v=jgpVdJB2sKQ&t=35s&pp=ygULbGVhcm4gcmVkaXM%3D) for more information.
3. Last but not least, please install Python 3.11 on your computer and install the required packages specified in `requirements.txt`. Using a virtual environment is highly preferred.

## Usage
1. Clone the repository to your local system using the following commands
   - `git clone https://github.com/Sreecharan885/roadmap-02-weather-api.git`
2. Navigate into the project directory
   - `cd roadmap-02-weather-api`
3. Ensure you're in your virtual environment if there is one with necessary packages installed.
4. Set the following environment variables in your console. 
   1. In Windows
      1. `set API_KEY=<your-api-key>`
         - This API KEY is the API Key of Visual Crossings API.
      2. `set REDIS_CONN_STRING=<your-redis-connection-string>`
         - This is the connection string to your Redis instance. 
5. Run the following 
   - `python app.py`
6. Once it starts running, use `http://localhost:5000/weather/<city-name>` to get the necessary data.

*Note*: If you get invalid API call as a response, please check the server logs for more information.

## Project Criteria
1. Redis has been utilized for caching where any key's expiry time is set to 12 hours.
2. Flask Limiter has been utilized for limiting the requests to the API. Currently set to 10 per hour, can be modified accordingly.
3. The `requests` module is utilized for getting response from the Visual Crossings API.