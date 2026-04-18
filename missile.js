class Missile {
  constructor(name, rangeKm, speedMach) {
    this.name = name;
    this.rangeKm = rangeKm;
    this.speedMach = speedMach;
  }

  launch() {
    return `${this.name} launched at Mach ${this.speedMach}!`;
  }
}

module.exports = Missile;
