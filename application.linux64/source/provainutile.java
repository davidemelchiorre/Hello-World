import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class provainutile extends PApplet {

public void setup()
{
  
}
public void draw()
{
  clear();
  text("Hello world",width/2,height/2);
}
  public void settings() {  size(800,600); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "provainutile" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
