

public class tester
{
   public static void main()
   {
       Carrier c1 = new Carrier();
       Destroyer Des = new Destroyer();
       Board g1 = new Board(false);
       c1.placeShip(g1.board[0][0],0,g1,true);
       g1.drawBoards();
       Des.placeShip(g1.board[1][0],0,g1,true);
   }
}
