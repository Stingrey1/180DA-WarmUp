import tkinter as tk
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
            # player 2 (AI)
            player2 = random.choice(["rock", "paper", "scissors"])
            if player1 == "rock" and player2 == "scissors":
                result = "Player 1 wins!"
            elif player1 == "paper" and player2 == "rock":
                result = "Player 1 wins!"
            elif player1 == "scissors" and player2 == "paper":
                result = "Player 1 wins!"
            elif player2 == "rock" and player1 == "scissors":
                result = "AI wins!"
            elif player2 == "paper" and player1 == "rock":
                result = "AI wins!"
            elif player2 == "scissors" and player1 == "paper":
                result = "AI wins!"
            else:
                result = "It's a tie!"
            client.publish("game/rock-paper-scissors/result", result)

class RockPaperScissorsApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Rock Paper Scissors")
        self.geometry("300x200")

        self.label = tk.Label(text="Waiting for AI player...", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.rock_button = tk.Button(text="Rock", command=lambda: self.play("rock"))
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(text="Paper", command=lambda: self.play("paper"))
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.pack(pady=5)

        self.client = mqtt.Client()
        self.client.connect("localhost", 1883, 60)
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.loop_start()

    def play(self, choice):
        self.client.publish("game/rock-paper-scissors", choice)
        self.rock_button.config(state="disabled")