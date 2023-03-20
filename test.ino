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
setPlane(2)
