import java.util.*;
public abstract class Ship
{
    private Tile startcell;
    private String[] arr ={"horizontal","vertical"};
    private int size;
    int flag=0;
    private int newcellX ;
    private int newcellY ;
    private int newor;
    private int neworientation;
    public void setSize(int i){this.size=i;}
    public int getSize(){return this.size;}
    public void placeShip(Tile gstartcell,int gorientation,Board gboard,boolean verbose)
    {
        Scanner scan1= new Scanner(System.in);
        Random rand = new Random();
        try
        {
            if(arr[gorientation]=="horizontal")
            {
                for(int i=0;i<this.size;i++)
                {
                   if("s"==gboard.board[gstartcell.getX()][i].draw())
                   {
                       this.flag=1;
                   }
                   if(gboard.board[gstartcell.getX()][i].Illegal==true)
                   {
                       this.flag=2;
                   }
                }
                if(flag==0)
                {
                    for (int k=0;k<this.size;k++)
                    {
                        gboard.board[gstartcell.X][gstartcell.Y+k].setValue("s");
                        gboard.drawBoards();
                        if(gstartcell.X<8)
                        {
                            gboard.board[gstartcell.X+1][gstartcell.getY()+k].Illegal=true;
                        }
                        if(gstartcell.X>1)
                        {
                            gboard.board[gstartcell.X-1][gstartcell.getY()+k].Illegal=true;
                        }
                        if(gstartcell.Y>1)
                        {
                            gboard.board[gstartcell.getX()][gstartcell.getY()-1].Illegal=true;
                        }
                        if(gstartcell.Y+this.size<8)
                        {
                            gboard.board[gstartcell.getX()][gstartcell.getY()+this.size].Illegal=true;
                        }
                    }
                }
              
            }
            if(arr[gorientation]=="vertical")
            {
                for(int i=0;i<this.size;i++)
                {
                   if("s"==gboard.board[gstartcell.getX()][i].draw())
                   {
                       this.flag=1;
                   }        
                   if(gboard.board[i][gstartcell.getY()].Illegal==true)
                   {
                       this.flag=2;
                   }
                }
                if(flag==0)
                    {
                        for (int k=0;k<this.size;k++)
                        {
                            gboard.board[gstartcell.X+k][gstartcell.Y].setValue("s");
                            gboard.drawBoards();
                            if(gstartcell.X>=1) //panw
                            {
                                gboard.board[gstartcell.X-1][gstartcell.getY()].Illegal=true;
                            }
                            if(gstartcell.X+this.size-1<=8) //katw
                            {
                                gboard.board[gstartcell.X+this.size][gstartcell.Y].Illegal=true;
                            }
                            if(gstartcell.Y>=1)//aristera
                            {
                                gboard.board[gstartcell.getX()+k][gstartcell.getY()-1].Illegal=true;
                            }
                            if(gstartcell.Y<=7)//deksia
                            {
                                gboard.board[gstartcell.getX()+k][gstartcell.getY()+1].Illegal=true;
                            }
                            }
                    }
                }
            
            
            if (this.flag==1)
            {throw new OverlapTilesException() ;}
            if (this.flag==2)
            {throw new AdjacentTilesException();}
            scan1.close();
        }
        
     
         catch(OverlapTilesException e)
            {
                try
                {
                    if(verbose==true)
                    {
                        System.out.println("Illegal placement,ship crosses another ship");
                        gboard.drawBoards();
                        System.out.println("please give a new row number for the starting tile");
                        newcellX=scan1.nextInt();
                        System.out.println("now please give a new row number for the starting tile");
                        newcellY=scan1.nextInt();
                        System.out.println("horizontal(0)\nvertical(1)\n please enter either 0 or 1");
                        newor=scan1.nextInt();
                        this.placeShip(gboard.board[newcellX][newcellY],newor,gboard,true);
                       
                    }
                    else
                    {
                        this.placeShip(gboard.board[rand.nextInt(8)][rand.nextInt(8)],rand.nextInt(2),gboard,false);
                    }
                }
                catch(InputMismatchException q)
                {
                 System.out.println("Please enter only integers..");
                }
            }
         catch(AdjacentTilesException e)
         {
           try
           {
               if(verbose==true)
               {
                   System.out.println("Illegal placement,other ship near the one you want to place");
                   System.out.println("please give a new row number for the starting tile");
                   newcellX=scan1.nextInt();
                   System.out.println("now please give a new row number for the starting tile");
                   newcellY=scan1.nextInt();
                   System.out.println("horizontal(0)\nvertical(1)\n please enter either 0 or 1");
                   newor=scan1.nextInt();
                   this.placeShip(gboard.board[newcellX][newcellY],newor,gboard,true);
                   
                }
                else
                {
                    this.placeShip(gboard.board[rand.nextInt(8)][rand.nextInt(8)],rand.nextInt(2),gboard,false);
                }
           }
           catch(InputMismatchException q)
           {
                 System.out.println("Please enter only integers..");
           }
         }
         catch(ArrayIndexOutOfBoundsException e)
         {
             try
             {
                 if(verbose==true)
                 {
                     System.out.println("Illegal placement,ship goes out of board");
                     System.out.println("please give a new row number for the starting tile");
                     newcellX=scan1.nextInt();
                     System.out.println("now please give a new row number for the starting tile");
                     newcellY=scan1.nextInt();
                     System.out.println("horizontal(0)\nvertical(1)\n please enter either 0 or 1");
                     newor=scan1.nextInt();
                     this.placeShip(gboard.board[newcellX][newcellY],newor,gboard,true);
                    
                    }
                    else
                    {
                        this.placeShip(gboard.board[rand.nextInt(8)][rand.nextInt(8)],rand.nextInt(2),gboard,false);
                    }
             }
             catch (InputMismatchException q)
             {
                 System.out.println("Please enter only integers..");
             }
        }
        
    }
 }