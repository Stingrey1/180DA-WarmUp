import paho.mqtt.client as mqtt
import random

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("game/rock-paper-scissors")

def on_message(client, userdata, msg):
    if msg.topic == "game/rock-paper-scissors":
        play = msg.payload.decode()
        if play == "start":
            # player 1
            player1 = random.choice(["rock", "paper", "scissors"])
            client.publish("game/rock-paper-scissors", player1)
        else:
            # player 2
            player2 = random.choice(["rock", "paper", "scissors"])
            if player1 == "rock" and player2 == "scissors":
                result = "Player 1 wins!"
            elif player1 == "paper" and player2 == "rock":
                result = "Player 1 wins!"
            elif player1 == "scissors" and player2 == "paper":
                result = "Player 1 wins!"
            elif player2 == "rock" and player1 == "scissors":
                result = "Player 2 wins!"
            elif player2 == "paper" and player1 == "rock":
                result = "Player 2 wins!"
            elif player2 == "scissors" and player1 == "paper":
                result = "Player 2 wins!"
            else:
                result = "It's a tie!"
            client.publish("game/rock-paper-scissors/result", result)

client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
