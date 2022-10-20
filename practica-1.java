float x  = 100;
float y = 100;
float xspeed = 2.5;
float yspeed = 2;

void setup(){
  size(800, 200);
  smooth();

void draw(){
  background(255);
}

x = x + speed;
y = y + speed;

if ((x > width) || (x < 0)){
  xspeed = xspeed + -1;
}

if ((y > height)||(y < 0)){
  yspeed = yspeed *= -1;
}

stroke(0);
strokweight(2);
fill(127);
ellipse(x,48,48);
}