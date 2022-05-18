import java.util.*;
public class Board 
{
    int  hcounter = 0 ; 
    int vcounter = 1;
    public Tile[][] board= new Tile[8][8] ;
    public Board(boolean a)
    {
        for(int g=0;g<8;g++)
            {
                for(int i=0;i<8;i++)
                {
                    board[i][g]= new Tile();
                }
            }
        for(int i = 0 ; i < 8;i++)
        {
            for(int g=0;i<8;i++)
            {
                board[i][g].setX(i);
                board[i][g].setY(g);
            }
        }
        for(int i = 0 ; i < 8;i++)
        {
            for(int g=0;g<8;g++)
            {
                board[i][g].setValue("~");
            }
        }
       for(int g=0;g<8;g++)
            {
                for(int i=0;i<8;i++)
                {
                    board[i][g].setHidden(a);
                }
            }
    }
    public void drawBoards() 
    {    
        for(int k=0;k<8;k++)
        {
            System.out.print("\t"+k);
        }
        System.out.println();
        for(int i=0 ; i<8 ; i++)
        {
            System.out.print(i+"\t");
            for(int g=0; g<8 ; g++)
            {
                System.out.print(board[i][g].draw() +"\t");
            }
            System.out.println("");
        }
        System.out.println("\n");
    }
    public String getAdjacentTiles(Tile gtile,String g)
    {
        if(g=="up")
        {   

            return board[gtile.getX()][gtile.getY()-1].getValue();
        }
        if(g=="left")
        {
            return board[gtile.getX()-1][gtile.getY()].getValue();
        }
        if(g=="right")
        {
            return board[gtile.getX()+1][gtile.getY()].getValue();
        }
        if(g=="down")
        {
            return board[gtile.getX()][gtile.getY()+1].getValue();
        }
        return "error";
    }
    public void placeAllShips(Board g2board)
    {
        Random rand = new Random();
        String[] arr = new String[2];
        Carrier c1 = new Carrier();
        Battleship b1 = new Battleship();
        Cruiser Cr1 = new Cruiser();
        Submarine Sub1 = new Submarine();
        Destroyer Des1 = new Destroyer();
        c1.placeShip(g2board.board[rand.nextInt(8)][rand.nextInt(8)],rand.nextInt(2),g2board,false);
        b1.placeShip(g2board.board[rand.nextInt(8)][rand.nextInt(8)],rand.nextInt(2),g2board,false);
        Cr1.placeShip(g2board.board[rand.nextInt(8)][rand.nextInt(8)],rand.nextInt(2),g2board,false);
        Sub1.placeShip(g2board.board[rand.nextInt(8)][rand.nextInt(8)],rand.nextInt(2),g2board,false);
        Des1.placeShip(g2board.board[rand.nextInt(8)][rand.nextInt(8)],rand.nextInt(2),g2board,false);
        g2board.drawBoards();
    }
    public boolean allShipsSunk()
    {
        for (int i=0;i<8;i++)
        {
            for( int q=0;q<8;q++)
            {
                if (board[i][q].getValue()=="S")
                {
                    return false;
                }
            }
        }
        return true;
    }
}

