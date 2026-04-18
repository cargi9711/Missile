from missile import Missile

def simulate():
    m = Missile("Falcon-X", 1200, 3.5)
    print(m)
    print(m.launch())

if __name__ == "__main__":
    simulate()
