import java.util.*;
public class Player
    {
      private String user;
      private int shotscounter = 0,misscounter = 0,hitcounter = 0, repcounter = 0;
      private Board ownboard;
      public Player (String user,Board a)
      {
        this.user = user;
        this.ownboard=a;
      }
      public Board getOwnboard(){return ownboard;}
      public int getShotsCounter(){return shotscounter;}
      public int getMissCounter(){ return misscounter;}
      public int getHitCounter(){return hitcounter;}
      public int getRepCounter(){return repcounter;}
      public String getUser(){return user;}
      public Board getBoard(){return ownboard;}
      public void placeAllShips() 
      {
          ownboard.placeAllShips(ownboard);
      }
      public void placeShip(Ship a,int X,int Y,int gorientation)
      {   
          a.placeShip(ownboard.board[X][Y],gorientation,ownboard,true); 
         
        }                
      public void fire(Board f,int X,int Y)
      {
          shotscounter ++;
          System.out.print("Player  :"+getUser()+"fired and... ");
          if(f.board[X][Y].getValue() == "~")
          {
              ownboard.board[X][Y].setValue("O");
              misscounter ++;
              System.out.println(" missed");
                    }
          if(f.board[X][Y].getValue() == "S")
          {
                        ownboard.board[X][Y].setValue("X");
                        hitcounter ++;
                        System.out.println("hit");
            
          }
          if(f.board[X][Y].getValue() == "X"||ownboard.board[X][Y].getValue() == "O")
          {
                repcounter++;
                System.out.println("but he already fired there..");
          }
      }
      public  void getStats()
      {
          System.out.println("Shots fired : "+getShotsCounter());
          System.out.println("Hits achieved : "+getHitCounter());
          System.out.println("Misses : "+ getMissCounter());
          System.out.println("Repetitions : "+getRepCounter());
      }
      public void manualPlace()//not done!!!
    {
         int row;
        int column;   
        int orientation;
        Scanner scan = new Scanner(System.in);
        // Carrier !!!
        System.out.println("Ok where would you like to place the Carrier(size=5)?,first give me the coordinates of the starting cell");
            Carrier C1 = new Carrier();
            row=scan.nextInt();
            column = scan.nextInt();
           
            System.out.println("Ok,now give me its orientation");
            orientation=scan.nextInt();
          this.placeShip(C1,row,column,orientation);
          this.getOwnboard().drawBoards();
          
          
          
          //BAttleship!!! 
            System.out.println("Ok where would you like to place the Battleship(size=4)?,first give me the coordinates of the starting cell");
            Battleship B1 = new Battleship();
            row=scan.nextInt();
            column = scan.nextInt();
            
            System.out.println("Ok,now give me its orientation");
           orientation=scan.nextInt();
          this.placeShip(B1,row,column,orientation);
          this.getOwnboard().drawBoards();
          
          
          //Submarine !!!
          System.out.println("Ok where would you like to place the Submarine(size=3)?,first give me the coordinates of the starting cell");
            Submarine S1 = new Submarine();
            row=scan.nextInt();
            column = scan.nextInt();
            
            System.out.println("Ok,now give me its orientation");
            orientation=scan.nextInt();
          this.placeShip(S1,row,column,orientation);
         this.getOwnboard().drawBoards();
         
          
          ///Cruiser!!!
          System.out.println("Ok where would you like to place the Cruiser(size=3)?,first give me the coordinates of the starting cell");
            Cruiser Cr1 = new Cruiser();
            row=scan.nextInt();
            column = scan.nextInt();
            
            System.out.println("Ok,now give me its orientation");
            orientation=scan.nextInt();
          this.placeShip(Cr1,row,column,orientation);
          this.getOwnboard().drawBoards();
          
         
          //Destroyer !!!
          System.out.println("Ok where would you like to place the Destroyer(size=2)?,first give me the coordinates of the starting cell");
            Destroyer D1 = new Destroyer();
            row=scan.nextInt();
            column = scan.nextInt();
         
            System.out.println("Ok,now give me its orientation");
             orientation=scan.nextInt();
            this.placeShip(D1,row,column,orientation);
             this.getOwnboard().drawBoards();
             scan.close();
    }
        }