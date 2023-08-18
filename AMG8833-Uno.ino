#include <Wire.h>
#include <Adafruit_AMG88xx.h>

Adafruit_AMG88xx amg;

void setup() {
    Serial.begin(115200);
    if (!amg.begin()) {
        Serial.println("Failed to initialize AMG88xx sensor");
        while (1);
    }
    delay(100);  // give some time for the sensor to stabilize
}

void loop() {
    float pixels[AMG88xx_PIXEL_ARRAY_SIZE];
    amg.readPixels(pixels);
    
for (int i = 0; i < AMG88xx_PIXEL_ARRAY_SIZE; i++) {
    Serial.print(pixels[i]);
    if (i < AMG88xx_PIXEL_ARRAY_SIZE - 1) {
        Serial.print(",");  // separate each pixel reading with a comma
    } else {
        Serial.println();  // newline after sending all pixel readings
    }
}
    
    delay(100);  // delay to give time for processing and avoid flooding the serial port
}
