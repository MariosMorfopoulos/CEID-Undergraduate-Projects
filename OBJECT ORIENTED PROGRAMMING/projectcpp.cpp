#include <iostream>
#include <exception>
#include <vector>
#include <stdlib.h>

using namespace std;

class Board;
class Ship;

enum Type {
    sea, ship, hit, miss 
};

enum Orientation {
    horizontal, vertical
};



class Tile 
{
 
 	private:   
       int x,y;
        Type shiptype;
    public:        
        Tile()
        {
            x=0; y=0; shiptype=sea;
        }
        
        Tile(int x1,int y1, Type S)
        {
            x=x1; y=y1;
            shiptype=S;
        }
        
        void draw(bool hidden)
        {
            switch (shiptype)
            {
                case sea:
                cout<<"~";
                break;
                case ship:
                if(!hidden) cout<<"s";
                break;
                case hit:
                cout<<"X";
                break;
                case miss:
                cout<<"o";
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
};


class OversizeException:public exception
{
 
    virtual const char* what() const throw()
    {
       cout<<"Error Oversize Array"<<endl;
    }
};

class OverlapTilesException: public exception
{
    virtual const char* what() const throw()
    {
        cout<<"Error OvelLapTile "<<endl;
    }
};

class AdjacentTilesException: public exception
{
  virtual const char* what() const throw()
    {
        cout<<"Error  AdjacentTiles "<<endl;
    }
};



class Ship
{
    private:
	Tile point;
    Orientation H; // katefthinsi
    
    protected:
    int L; // megethos
    
    public:
    Ship()
    {
        point=Tile();
        H=horizontal;
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
    
    void placeShip(Board B) 
    {
        vector<Tile> S;
     
            S=B.getAdjacentTiles(point);
            
            for (int j=0;j<S.size();j++)
            {
                Tile t1=S[j];
                if (t1.getType()!=sea) {
                    throw new AdjacentTilesException();
                }
                
            }
            
        for (int i=0;i<L;i++)
        {
            if (H==horizontal)
            {
                int x=point.getX();
                 int y=point.getY();
                if (x+i>6) {
                    throw new OversizeException();
                }
                
                if (B.A[x+i][y].getType()!=sea)
                {
                    throw new OverlapTilesException();
                }
            }
            if (H==vertical)
            {
                int y=point.getY();
                if (y+i>6) {
                    throw new OversizeException();
                }

        
            }
            
           
            
            
        }
        
         for (int i=0;i<L;i++)
        {
            if (H==horizontal)
            {
                int x=point.getX();
                 int y=point.getY();
                 
                 B.A[x+i][y].setType(ship);
            }
            if (H==vertical)
            {
                int x=point.getX();
                 int y=point.getY();
                 
                 B.A[x][y+i].setType(ship);
            }
            
        }
        
    }        
    
            
};

class Carrier :public  Ship
{
	public:
    Carrier():Ship()
    {
        
        L=5;        
    }
    
      Carrier(Tile T, Orientation h):Ship(T,h)
      {
         
          L=5;
          
      }
};

class Battleship :public  Ship
{
		public:
    Battleship():Ship()
    {
       
        L=4;        
    }
    
      Battleship(Tile T, Orientation h):Ship(T,h)
      {
         
          L=4;
          
      }
};

class Cruiser:public  Ship
{
		public:
    Cruiser():Ship()
    {
       
        L=3;        
    }
    
      Cruiser(Tile T, Orientation h):Ship(T,h)
      {
          
          L=3;
          
      }
};

class Submarine :public  Ship
{
		public:
    Submarine():Ship()
    {
        
        L=3;        
    }
    
      Submarine(Tile T, Orientation h):Ship(T,h)
      {
          
          L=3;
          
      }
};

class Destroyer :public  Ship
{
		public:
    Destroyer():Ship()
    {
        
        L=2;        
    }
    
      Destroyer(Tile T, Orientation h):Ship(T,h)
      {
         
          L=2;
          
      }
};

class Board
{
		public:
    Tile A[7][7];
    
    Board()
    {
        for (int i=0;i<7;i++)
            for (int j=0;j<7;j++)
                A[i][j]=Tile();
        
    }
    
    // ektyposi tou pinaka tou paikti kai tou antipallou OP
    void drawboards(Board OP)
    {
        cout<<" - - - Y O U - -     - O P P O N E N T -"<<endl;
        cout<<"  0 1 2 3 4 5 6         0 1 2 3 4 5 6 "<<endl;
        for (int i=0;i<7;i++)
        {
            cout<<i+" ";
            for (int j=0;j<7;j++)
            {
                
                A[i][j].draw(false);
                cout<<" ";
            }
            cout<<"      "<<i<<" ";
            for (int j=0;j<7;j++)
            {
                A[i][j].draw(true);
                cout<<" ";
            }
            cout<<" "<<endl;
                
        }
    }
    
    
    // vazoume se ena arraylist ta geitonika simeia tou keliou B
    vector<Tile> getAdjacentTiles(Tile B)
    {
      vector<Tile> Lst;
      int x=B.getX();
      int y=B.getY();
      if (x>0){
          Lst.push_back(A[x-1][y]);
          
      }
      if (x<6){
          Lst.push_back(A[x+1][y]);
          
      }
      if (y>0){
          Lst.push_back(A[x][y-1]);
          
      }
      if (y<6){
          Lst.push_back(A[x][y+1]);
          
      }
      return Lst;
    }
    
    
    void placeAllShips()
    {
        
        Orientation h2= horizontal;
       
        bool f;
        
        do {
            int x=rand()%7; int y=rand()%7;
            int h=rand()%2;
            if (h==0) h2= horizontal;
            if (h==1) h2= vertical;
            Tile T(x,y, sea);
            Carrier S1(T,h2);
            try {
                S1.placeShip(*this);
                f=false;
            } catch (exception e)
            {
                f=true;
            }
        } while(f);
        
        
         do {
             int x=rand()%7; int y=rand()%7;
            int h=rand()%2;
            if (h==0) h2=horizontal;
            if (h==1) h2=vertical;
            Tile T(x,y,sea);
            Destroyer S1(T,h2);
            try {
                S1.placeShip(*this);
                f=false;
            } catch (exception e)
            {
                f=true;
            }
        } while(f);
         
        do {
             int x=rand()%7; int y=rand()%7;
            int h=rand()%2;
            if (h==0) h2=horizontal;
            if (h==1) h2=vertical;
            Tile T(x,y, sea);
            Cruiser S1(T,h2);
            try {
                S1.placeShip(*this);
                f=false;
            } catch (exception e)
            {
                f=true;
            }
        } while(f);
         
        
        do {
             int x=rand()%7; int y=rand()%7;
            int h=rand()%2;
            if (h==0) h2= horizontal;
            if (h==1) h2= vertical;
            Tile T(x,y, sea);
            Submarine S1(T,h2);
            try {
                S1.placeShip(*this);
                f=false;
            } catch (exception e)
            {
                f=true;
            }
        } while(f);
        
          do {
             int x=rand()%7; int y=rand()%7;
            int h=rand()%2;
            if (h==0) h2= horizontal;
            if (h==1) h2= vertical;
            Tile T(x,y, sea);
            Battleship S1(T,h2);
            try {
                S1.placeShip(*this);
                f=false;
            } catch (exception e)
            {
                f=true;
            }
        } while(f);
         
    }
    
    bool allShipsSunk(Board B){
        int i,j;
        
        for (i=0;i<7;i++)
            for (j=0;j<7;j++)
            {
                if(B.A[i][j].getType()== ship) return false;
            }
        return true;
    } 
    
};



class Player
{
		public:
    Board B;
    string onoma;
    int voles;
    int astoxies;
    int efstoxies;
    int epanalipseis;
    
    static int svoles;
    static int sastoxies;
    static int sefstoxies;
    static int sepanalipseis;
    
    Player()
    {
    	
	}
    
    Player(string Name)
    {
        onoma=Name;
        B=Board();
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
        cout<<"Name player:"<<onoma;
        cout<<"Voles:"<<voles;
        cout<<"Astoxies:"<<astoxies;
        cout<<"Efstoxies:"<<efstoxies;
        cout<<"Epanalipseis:"<<epanalipseis;
    }

};


class Game
{
		public:
    Player P1, P2;
    Game()
    {
       P1=Player("paiktis");
       P2=Player("ypologistis");
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
    
    int *getInput()
    {
        
        int P[2];
        cout<<"give coordinates (x,y) (ex. 10 2):";
        cin>>P[0];
        
        cin>>P[1];
        
        return P;
    }
    
    int* getRandInput()
    {
       
        int P[2];
        P[0]=rand()%7;
        P[1]=rand()%7;
        
        return P;
    }
    
    Orientation  getOrienation()
    {
       
        do {
            cout<<"Do you want random Ships or not?";
            string S;
            cin>>S;
            if(S=="H")
                return  horizontal;
            if(S=="V")
                return  vertical;
            cout<<"Error input";
        }while(true);
        
        
    }
    
    bool randomPlace()
    {
        
        do {
         cout<<"Do you want random Ships (Y/N)?";
        string S;
        cin>>S;
        if(S=="Y")
            return true;
        if(S=="N")
            return false;
        }while(true);
        
    }   
};


int main()
{

    
   
      Game G;
      G.Main();
       
   
return 1;    
}

