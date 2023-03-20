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

