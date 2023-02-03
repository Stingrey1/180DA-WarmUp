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
            # AI
            ai = random.choice(["rock", "paper", "scissors"])
            client.publish("game/rock-paper-scissors", ai)
        else:
            # player
            if play == "rock" and ai == "scissors":
                result = "Player wins!"
            elif play == "paper" and ai == "rock":
                result = "Player wins!"
            elif play == "scissors" and ai == "paper":
                result = "Player wins!"
            elif ai == "rock" and play == "scissors":
                result = "AI wins!"
            elif ai == "paper" and play == "rock":
                result = "AI wins!"
            elif ai == "scissors" and play == "paper":
                result = "AI wins!"
            else:
                result = "It's a tie!"
            client.publish("game/rock-paper-scissors/result", result)

class RockPaperScissorsApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Rock Paper Scissors")
        self.geometry("300x200")

        self.label = tk.Label(text="Make your move!", font=("Helvetica", 16))
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
        self.client.on_message = self.on_result
        self.client.loop_start()

    def play(self, choice):
        self.client.publish("game/rock-paper-scissors", choice)
        self.rock_button["state"] = "disabled"
        self.paper_button["state"] = "disabled"
        self.scissors_button["state"] = "disabled
