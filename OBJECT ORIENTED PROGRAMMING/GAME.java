import java.util.*;
class GAME 
{
    
    
    public static void main()//def not done!!!
    {
       
        
        int x;
        int y;
        Scanner scan = new Scanner(System.in);
        Random rand = new Random();
        Board playerBoard = new Board(false);
        Board pcBoard = new Board(true);
        Player player1 = new Player("Player",playerBoard);
        Player pc = new Player("Computer",pcBoard);
        System.out.println("Do you want to place your ships randomly ? \n (y=1/n=0) ");
        x=scan.nextInt();
        if(x==1)
        {
            player1.placeAllShips();
        }
        else
        {
            player1.manualPlace();
        }
        pc.placeAllShips();
        System.out.println("OK... let's begin");
        System.out.println("Player goes first... \n ");
        while(pcBoard.allShipsSunk()==false&&playerBoard.allShipsSunk())
        {
            System.out.println("Player's turn...(give coordinates)");
            x=scan.nextInt();
            y=scan.nextInt();
            player1.fire(pcBoard,x,y);
            System.out.println("Computer's turn...");
            pc.fire(playerBoard,rand.nextInt(8),rand.nextInt(8));
        }
        scan.close();
    }
    public void getInput()
    {
        Scanner scan = new Scanner(System.in);
        try
        {
            int row;
            int column;
            int[] array = new int[2];
            System.out.println("Give the coordinates");
            row=scan.nextInt();
            column=scan.nextInt();
            while(row<0||row>8)
            {
                System.out.println("Row not within boundaries");
                row=scan.nextInt();
            }
            while(column<0 ||column >8)
            {
                System.out.println("Column not within Boundaries");
                column=scan.nextInt();
            }
        
        
            scan.close();
            
        }
        catch(InputMismatchException q)
        {
            this.getInput();
        }
       
    }
    public int[] getRandInput()
    {
        Random rand = new Random();
         int[] arr = new int[2];
        arr[0] = rand.nextInt(9);
        arr[1] = rand.nextInt(9);
        return arr;
    }
    public void getOrientation()
    {
        
    }
    public void randomPlace()
    {
    }
    
}