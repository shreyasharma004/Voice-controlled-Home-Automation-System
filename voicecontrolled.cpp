#define relay1 13 //Connect relay1 to pin 13 String voice;
void setup() {
Serial.begin(9600); //Set rate for communicating with phone pinMode(relay1, OUTPUT); //Set relay1 as an output
digitalWrite(relay1, HIGH); //Switch relay1 off }
void loop() {
while (Serial.available()){ //Check if there is an available byte to read
delay(10); //Delay added to make thing stable char c = Serial.read(); //Conduct a serial read
 
if (c == '#') {break;} //Exit the loop when the # is detected after the word
voice += c; //Shorthand for voice = voice + c }
if (voice.length() > 0) //////////////////////////////////////////////////////////////////// {
if(voice == "*turn on light"){ //Voice Command to ON Relay 01
digitalWrite(relay1, LOW); //Relay 01 ON }
    ////////////////////////////////////////////////////////////////////
else if(voice == "*turn off light") { //Voice Command to OFF Relay 01
digitalWrite(relay1, HIGH); //Relay 01 OFF }
    ////////////////////////////////////////////////////////////////////
voice=""; //Reset the variable after initiating
} }
void switchalloff() //Function for turning OFF all relays {
digitalWrite(relay1, HIGH);
}
void switchallon() //Function for turning ON all relays {
digitalWrite(relay1, LOW);}
