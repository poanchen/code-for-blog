import processing.sound.*;
    
SoundFile file;
//put your audio file name here
String audioName = "sample.mp3";
String path;

//runs once when the app first starts
void setup() {
  // for more info about sketchPath, go to https://processing.org/discourse/beta/num_1229443269.html
  path = sketchPath(audioName);
  file = new SoundFile(this, path);
  file.play();
}

//runs all the time, this is the main app loop
void draw() {
}