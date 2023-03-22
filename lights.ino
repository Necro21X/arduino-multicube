#define DATA_PIN 2
#define LATCH_PIN 4
#define CLOCK_PIN 3

#define NUM_SHIFT_PIN 20

int c = 0;
int p = 16;

const uint8_t numOfRegPins = NUM_SHIFT_PIN;

bool registers[numOfRegPins];

void setup() {
  pinMode(DATA_PIN, OUTPUT);
  pinMode(CLOCK_PIN, OUTPUT);
  pinMode(LATCH_PIN, OUTPUT);
  stopRegisters();
  shiftRegisters();

}

bool power = true;

void loop() {
	stopRegisters();
setCoord(0, 0);
setCoord(1, 0);
setCoord(2, 0);
setCoord(3, 0);
setPlane(1);
setPlane(2);
setPlane(3);
setPlane(0);
shiftRegisters(); delay(200); stopRegisters();
setCoord(0, 1);
setCoord(1, 1);
setCoord(2, 1);
setCoord(3, 1);
setPlane(0);
setPlane(1);
setPlane(2);
setPlane(3);
shiftRegisters(); delay(200); stopRegisters();
setCoord(0, 2);
setCoord(1, 2);
setCoord(2, 2);
setCoord(3, 2);
setPlane(3);
setPlane(2);
setPlane(1);
setPlane(0);
shiftRegisters(); delay(200); stopRegisters();
setCoord(3, 3);
setCoord(2, 3);
setCoord(1, 3);
setCoord(0, 3);
setPlane(0);
setPlane(1);
setPlane(2);
setPlane(3);
shiftRegisters(); delay(200); stopRegisters();
}

void stopRegisters() {
  for (int i = numOfRegPins - 1; i >= 0; i--) {
    if (i < 16) {
      registers[i] = LOW;
    }
    else {
      registers[i] = HIGH;
    }
  }
}

void shiftRegisters() {
  digitalWrite(LATCH_PIN, LOW);

  for (int i = numOfRegPins -1; i >= 0; i--) {
    digitalWrite(CLOCK_PIN, LOW);
    digitalWrite(DATA_PIN, registers[i]);
    digitalWrite(CLOCK_PIN, HIGH);
  }

  digitalWrite(LATCH_PIN, HIGH);
}

void setReg(int index, int value) {
  registers[index] = value;
}

void setCoord(int x, int y) {
  c = 1 * x + 4 * y;
  setReg(c, power);
}

void setPlane(int z) {
  p = z + 16;
  setReg(p, !power);
}
