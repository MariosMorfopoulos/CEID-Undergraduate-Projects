/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


package onto18;

import java.util.*;

enum Type {
    Sea, Ship, Hit, Miss 
};

enum Orientation {
    horizontal, vertical
};


class Tile 
{
    
    private    int x,y;
    private    Type shiptype;
            
        Tile()
        {
            x=0; y=0; shiptype=Type.Sea;
        }
        
        Tile(int x1,int y1, Type S)
        {
            x=x1; y=y1;
            shiptype=S;
        }
        
        void draw(boolean hidden)
        {
            switch (shiptype)
            {
                case Sea:
                System.out.print("~");
                break;
                case Ship:
                if(!hidden) System.out.print("s");
                break;
                case Hit:
                System.out.print("X");
                break;
                case Miss:
                System.out.print("o");
                break;
                        
            }
        }
        
        
        void setPosition(int x1,int y1)
        {
            x=x1; y=y1;
        }
        void setType(Type T)
        {
            shiptype=T;
        }
        
        int getX()
        {
            return x;
            
        }
        
        int getY()
        {
            return y;
            
        }
        
        Type getType()
        {
            return shiptype;
        }
}


class OversizeException extends Exception
{
    OversizeException()
    {
        
    }
    
    @Override
    public void printStackTrace()
    {
        System.out.println("Error Oversize Array");
    }
}

class OverlapTilesException extends Exception
{
    OverlapTilesException()
    {
        
    }
    
    @Override
    public void printStackTrace()
    {
        System.out.println("Error OvelLapTile ");
    }
}

class AdjacentTilesException extends Exception
{
    AdjacentTilesException()
    {
        
    }
    
    @Override
    public void printStackTrace()
    {
        System.out.println("Error  AdjacentTiles ");
    }
}

abstract class Ship
{
    private Tile point;
    private Orientation H; // katefthinsi
    protected int L; // megethos
    
    Ship()
    {
        point=new Tile();
        H=Orientation.horizontal;
        L=0;
    }
    
    Ship(Tile T, Orientation h)
    {
        point=T;
        H=h;
       
    }
    
    void setTile(Tile T)
    {
        point=T;
    }
    
    void setH(Orientation h)
    {
        H=h;
    }
    
    void setL(int l)
    {
        L=l;
    }
    
    void placeShip(Board B) throws AdjacentTilesException, OversizeException,  OverlapTilesException
    {
        ArrayList S;
     
            S=B.getAdjacentTiles(point);
            
            for (int j=0;j<S.size();j++)
            {
                Tile t1=(Tile )S.get(j);
                if (t1.getType()!=Type.Sea) {
                    throw new AdjacentTilesException();
                }
                
            }
            
        for (int i=0;i<L;i++)
        {
            if (H==Orientation.horizontal)
            {
                int x=point.getX();
                 int y=point.getY();
                if (x+i>6) {
                    throw new OversizeException();
                }
                
                if (B.A[x+i][y].getType()!=Type.Sea)
                {
                    throw new OverlapTilesException();
                }
            }
            if (H==Orientation.vertical)
            {
                int y=point.getY();
                if (y+i>6) {
                    throw new OversizeException();
                }

        
            }
            
           
            
            
        }
        
         for (int i=0;i<L;i++)
        {
            if (H==Orientation.horizontal)
            {
                int x=point.getX();
                 int y=point.getY();
                 
                 B.A[x+i][y].setType(Type.Ship);
            }
            if (H==Orientation.vertical)
            {
                int x=point.getX();
                 int y=point.getY();
                 
                 B.A[x][y+i].setType(Type.Ship);
            }
            
        }
        
    }        
    
            
}

class Carrier extends Ship
{
    Carrier()
    {
        super();
        L=5;        
    }
    
      Carrier(Tile T, Orientation h)
      {
          super(T,h);
          L=5;
          
      }
}

class Battleship extends Ship
{
    Battleship()
    {
        super();
        L=4;        
    }
    
      Battleship(Tile T, Orientation h)
      {
          super(T,h);
          L=4;
          
      }
}

class Cruiser extends Ship
{
    Cruiser()
    {
        super();
        L=3;        
    }
    
      Cruiser(Tile T, Orientation h)
      {
          super(T,h);
          L=3;
          
      }
}

class Submarine extends Ship
{
    Submarine()
    {
        super();
        L=3;        
    }
    
      Submarine(Tile T, Orientation h)
      {
          super(T,h);
          L=3;
          
      }
}

class Destroyer extends Ship
{
    Destroyer()
    {
        super();
        L=2;        
    }
    
      Destroyer(Tile T, Orientation h)
      {
          super(T,h);
          L=2;
          
      }
}

class Board
{
    Tile A[][]=new Tile[7][7];
    
    Board()
    {
        for (int i=0;i<7;i++)
            for (int j=0;j<7;j++)
                A[i][j]=new Tile();
        
    }
    
    // ektyposi tou pinaka tou paikti kai tou antipallou OP
    void drawboards(Board OP)
    {
        System.out.println(" - - - Y O U - -     - O P P O N E N T -");
        System.out.println("  0 1 2 3 4 5 6         0 1 2 3 4 5 6 ");
        for (int i=0;i<7;i++)
        {
            System.out.print(i+" ");
            for (int j=0;j<7;j++)
            {
                
                A[i][j].draw(false);
                System.out.print(" ");
            }
            System.out.print("      "+i+" ");
            for (int j=0;j<7;j++)
            {
                A[i][j].draw(true);
                System.out.print(" ");
            }
            System.out.println(" ");
                
        }
    }
    
    
    // vazoume se ena arraylist ta geitonika simeia tou keliou B
    ArrayList getAdjacentTiles(Tile B)
    {
      ArrayList Lst=new ArrayList();
      int x=B.getX();
      int y=B.getY();
      if (x>0){
          Lst.add(A[x-1][y]);
          
      }
      if (x<6){
          Lst.add(A[x+1][y]);
          
      }
      if (y>0){
          Lst.add(A[x][y-1]);
          
      }
      if (y<6){
          Lst.add(A[x][y+1]);
          
      }
      return Lst;
    }
    
    
    void placeAllShips()
    {
        Random r=new Random();
        Orientation h2=Orientation.horizontal;
       
        boolean f;
        
        do {
            int x=r.nextInt(); int y=r.nextInt();
            int h=r.nextInt(2);
            if (h==0) h2=Orientation.horizontal;
            if (h==1) h2=Orientation.vertical;
            Tile T=new Tile(x,y,Type.Sea);
            Carrier S1=new Carrier(T,h2);
            try {
                S1.placeShip(this);
                f=false;
            } catch (Exception e)
            {
                f=true;
            }
        } while(f);
        
        
         do {
               int x=r.nextInt(); int y=r.nextInt();
            int h=r.nextInt(2);
            if (h==0) h2=Orientation.horizontal;
            if (h==1) h2=Orientation.vertical;
            Tile T=new Tile(x,y,Type.Sea);
            Destroyer S1=new Destroyer(T,h2);
            try {
                S1.placeShip(this);
                f=false;
            } catch (Exception e)
            {
                f=true;
            }
        } while(f);
         
        do {
               int x=r.nextInt(); int y=r.nextInt();
            int h=r.nextInt(2);
            if (h==0) h2=Orientation.horizontal;
            if (h==1) h2=Orientation.vertical;
            Tile T=new Tile(x,y,Type.Sea);
            Cruiser S1=new Cruiser(T,h2);
            try {
                S1.placeShip(this);
                f=false;
            } catch (Exception e)
            {
                f=true;
            }
        } while(f);
         
        
        do {
               int x=r.nextInt(); int y=r.nextInt();
            int h=r.nextInt(2);
            if (h==0) h2=Orientation.horizontal;
            if (h==1) h2=Orientation.vertical;
            Tile T=new Tile(x,y,Type.Sea);
            Submarine S1=new Submarine(T,h2);
            try {
                S1.placeShip(this);
                f=false;
            } catch (Exception e)
            {
                f=true;
            }
        } while(f);
        
          do {
               int x=r.nextInt(); int y=r.nextInt();
            int h=r.nextInt(2);
            if (h==0) h2=Orientation.horizontal;
            if (h==1) h2=Orientation.vertical;
            Tile T=new Tile(x,y,Type.Sea);
            Battleship S1=new Battleship(T,h2);
            try {
                S1.placeShip(this);
                f=false;
            } catch (Exception e)
            {
                f=true;
            }
        } while(f);
         
    }
    
    boolean allShipsSunk(Board B){
        int i,j;
        
        for (i=0;i<7;i++)
            for (j=0;j<7;j++)
            {
                if(B.A[i][j].getType()==Type.Ship) return false;
            }
        return true;
    } 
    
}

class Game
{
    Player P1, P2;
    Game()
    {
        P1=new Player("Paiktis");
        P2=new Player("Computer");
    }
    
    void Main()
    {
       
          if (randomPlace())
          {
              P1.placeAllShips();
              P2.placeAllShips();
              
          }
          else
          {
              
          }
              
          
    }
    
    int[] getInput()
    {
        Scanner sc = new Scanner(System.in);
        int P[]=new int[2];
        System.out.println("give coordinates (x,y) (ex. 10 2):");
        P[0]=sc.nextInt();
        
        P[1]=sc.nextInt();
        
        return P;
    }
    
    int[] getRandInput()
    {
        Random rand = new Random();
        int P[]=new int[2];
        P[0]=rand.nextInt(7);
        P[1]=rand.nextInt(7);
        
        return P;
    }
    
    Orientation  getOrienation()
    {
        Scanner sc = new Scanner(System.in);
        do {
            System.out.println("Do you want random Ships or not?");
            String S=sc.nextLine();
            if(S.equals("H"))
                return Orientation.horizontal;
            if(S.equals("V"))
                return Orientation.vertical;
            System.out.println("Error input");
        }while(true);
        
        
    }
    
    boolean randomPlace()
    {
        Scanner sc = new Scanner(System.in);
        do {
         System.out.println("Do you want random Ships (Y/N)?");
        String S=sc.nextLine();
        if(S.equals("Y"))
            return true;
        if(S.equals("N"))
            return false;
        }while(true);
        
    }   
}


class Player
{
    Board B;
    String onoma;
    int voles;
    int astoxies;
    int efstoxies;
    int epanalipseis;
    
    static int svoles;
    static int sastoxies;
    static int sefstoxies;
    static int sepanalipseis;
    
    Player(String Name)
    {
        onoma=Name;
        B=new Board();
        voles=0;
        astoxies=0;
        efstoxies=0;
        epanalipseis=0;
        
    }
    void placeAllShips()
    {
        B.placeAllShips();
    }
    
    void placeShip()
    {
        
    }
    
    void fire()
    {
        
    }
    
    void getStats()
    {
        System.out.println("Name player:"+onoma);
        System.out.println("Voles:"+voles);
        System.out.println("Astoxies:"+astoxies);
        System.out.println("Efstoxies:"+efstoxies);
        System.out.println("Epanalipseis:"+epanalipseis);
    }

}

public class Onto18 {

    
    public static void main(String[] args) {
      Game G=new Game();
      G.Main();
       
    }
    
}
