# DockerTelegramBot
In this project i create a Telegram bot for a game with farmer.

Using Telethon library, Python.

In this project, you will find the necessary code and instructions to build and run the Telegram bot in a Docker container. You can use this as a starting point to create your own custom bot and interact with the Telegram API in a seamless and efficient way.

## Running the Project
1. To get started, make sure you have Docker installed on your machine: https://docs.docker.com/get-docker/
2. Clone this repository to you computer
3. Change the config.ini file with you values: 

    -> APP_ID and API_HASH for telethon: https://my.telegram.org/auth
    
    -> BOT_TOKEN: Write on telegram to @BotFather and follow the instructions
    
4. Then, navigate to the project folder and run the following command to build the Docker image:
`docker build --tag dockerbot .`
5. To run the Docker container, use the following command:
`docker-compose up`
6. Once the container is running, go to Telegram and send the /start command to your bot. You can now enjoy using your Python script within the Docker container!
