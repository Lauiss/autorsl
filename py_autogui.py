# Importation des modules
from pynput.mouse import Button, Controller, Listener
from threading import Thread
import time
import keyboard
import sys
import pickle


# Création de la class
class AutoClick:

    # Initialisation des variables
    def __init__(self):
        self.x, self.y = 0, 0
        self.time = 1
        self.state = True

        self.mouse = Controller()
        self.keyboard = Controller()

        self.load_coordiante()

    # Fonction pour ajouter les coordonnées
    def add_coordinate(self):
        with Listener(on_click=self.get_click_coordinate) as listener:
            listener.join()

    # Fonction pour start les coordonnées
    def start(self):
        t1 = Thread(target=self.stop)
        t1.daemon = True
        t1.start()
        while self.state:
            self.mouse.position = (self.x, self.y)
            self.mouse.click(Button.left, 1)
            time.sleep(self.time)
        sys.exit()

    # Fonction pour récupéré les coordonnées
    def get_click_coordinate(self, x, y, button, pressed):
        if pressed:
            self.x, self.y = x, y

        if not pressed:
            # Arrete d'ecouter
            return False

    # Fonction pour définir le temps
    def set_time(self, time_user):
        self.time = time_user

    # Fonction pour arreter l'auto cliker
    def stop(self):
        while True:
            if keyboard.is_pressed('echap'):
                self.save_coordinates()
                self.state = False

    def save_coordinates(self):
        pickle.dump([self.x, self.y, self.time], open('coordinates', 'wb'))

    def load_coordiante(self):
        self.x, self.y, self.time = pickle.load(open('coordinates', 'rb'))

