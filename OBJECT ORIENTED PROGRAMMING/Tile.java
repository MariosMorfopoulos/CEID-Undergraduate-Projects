public class Tile
{
    int X;
    int Y;
    private String  value;
    boolean hidden = true;
    boolean Illegal = false;
    public void setX(int X){this.X=X;}
    public void setY(int Y){this.Y=Y;}
    public void setValue(String givenx){this.value = givenx;}
    public void setHidden(boolean a) {this.hidden = a;}
    public int getX(){return X;}
    public int getY(){return Y;}
    public String getValue(){return value;}
    public String draw()
    {
        if  (hidden == true){return "~";}
        return value;
    }
}